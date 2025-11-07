import argparse
import logging
import os
import sys

from camel.typing import ModelType

root = os.path.dirname(__file__)
sys.path.append(root)

from chatdev.chat_chain import ChatChain
import time
try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version
    print(
        "Warning: Your OpenAI version is outdated. \n "
        "Please update as specified in requirement.txt. \n "
        "The old API interface is deprecated and will no longer be supported.")


def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('--config', type=str, default="Default",
                    help="Name of config, which is used to load configuration under CompanyConfig/")
parser.add_argument('--org', type=str, default="DefaultOrganization",
                    help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
parser.add_argument('--task', type=str, default="Develop a basic Gomoku game.",
                    help="Prompt of software")
parser.add_argument('--name', type=str, default="unspecified",
                    help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
parser.add_argument('--sample_num', type=str, default="unspecified",
                    help="Sample num")
parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
                    help="GPT Model, choose from {'GPT_3_5_TURBO', 'GPT_4', 'GPT_4_TURBO', 'GPT_4O', 'GPT_4O_MINI'}")
parser.add_argument('--path', type=str, default="",
                    help="Your file directory, ChatDev will build upon your software in the Incremental mode")
args = parser.parse_args()


args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO,
             'GPT_4': ModelType.GPT_4,
            #  'GPT_4_32K': ModelType.GPT_4_32k,
             'GPT_4_TURBO': ModelType.GPT_4_TURBO,
            #  'GPT_4_TURBO_V': ModelType.GPT_4_TURBO_V
            'GPT_4O': ModelType.GPT_4O,
            'GPT_4O_MINI': ModelType.GPT_4O_MINI,
             }
if openai_new_api:
    args2type['GPT_3_5_TURBO'] = ModelType.GPT_3_5_TURBO_NEW



prompt = '''
            Write a Python function that calculates the Fibonacci sequence up to n terms.
            The function should return a list of numbers.
            '''
my_dict = {"task_id": "HumanEval/0", "prompt": "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n", "entry_point": "has_close_elements", "canonical_solution": "    for idx, elem in enumerate(numbers):\n        for idx2, elem2 in enumerate(numbers):\n            if idx != idx2:\n                distance = abs(elem - elem2)\n                if distance < threshold:\n                    return True\n\n    return False\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False\n    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True\n    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True\n    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False\n\n"}

custom_prompt = '''
            Write the software code that is neccessary to solve the following task or fix the following code. In the main.py file, only write the necessary code, nothing more. Do not implement a GUI interface or anything redundant. make sure the code piece works as desired.
            '''
prompt = custom_prompt + my_dict["prompt"]

from human_eval.data import write_jsonl, read_problems
problems = read_problems()
num_samples_per_task = 1

samples = []
counter = 0
# for _ in range(num_samples_per_task):
#     results = []
#     for task_id in problems:
task_id = args.name
print(task_id)
prompt = custom_prompt + problems[task_id]["prompt"]
args.name = task_id.replace("/", "_")
config_path, config_phase_path, config_role_path = get_config(args.config)

chat_chain = ChatChain(config_path=config_path,
                    config_phase_path=config_phase_path,
                    config_role_path=config_role_path,
                    task_prompt=prompt,
                    project_name=args.name,
                    org_name=args.org,
                    model_type=args2type[args.model],
                    code_path=args.path)
# print("****** LOG FILE PATH ******")
# print(chat_chain.log_filepath)
# time.sleep(4)
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")
chat_chain.pre_processing()
chat_chain.make_recruitment()
chat_chain.execute_chain()
# result = chat_chain.execute_prompt(prompt, language="python")
chat_chain.post_processing()

my_path = chat_chain.log_filepath.replace(".log", "")
my_path = my_path + "/main.py"
with open(my_path, 'r', encoding='utf-8') as file:
    completion = file.read()
f = open(f"data_og/{args.name}_{args.sample_num}.py", "w")
f.write(completion)
f.close()

#         results.append(dict(task_id=task_id, completion=completion))
#     samples.append(results)
#     counter += 1
#     if counter > 3:
#         break
# write_jsonl("samples.jsonl", samples)

# print(result)
# f = open("result2.txt", "w")
# f.write(result)
# f.close()
# print(chat_chain.chat_env.env_dict)


