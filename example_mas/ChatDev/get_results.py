from human_eval.data import write_jsonl, read_problems
problems = read_problems()
for task_id in problems:
    print(task_id)

max_task_id = 164

samples = []
for j in range(6):
    counter = 0
    for task_id in problems:    
        name = task_id
        if counter < max_task_id:
            completion = open(f"data_og/{name.replace('/', '_')}_{j}.py", "r").read()
        else:
            completion = ""
        samples.append(dict(task_id=task_id, completion=completion))
        counter += 1
        # if counter == max_task_id:
        #     break
    

def get_completion(task_id, j):
    completion = open(f"data/{task_id.replace('/', '_')}_{j}.py", "r").read()
    return completion

# samples = [
#     dict(task_id=task_id, completion=get_completion(task_id, j)) for task_id in problems
#     for j in range(6)
# ]
write_jsonl("samples_og_full.jsonl", samples)

