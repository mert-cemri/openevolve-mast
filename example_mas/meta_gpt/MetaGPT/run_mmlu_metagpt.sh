
# Counter to track current project name
counter=0

# for j in {0..1}; do
for ((i=0; i<30; i++)); do
    # python run.py --task "$(cat mmlu_prompts/prompt_without_answer_$i.txt)" --name "mmlu_$i" --sample_num "$j" --model "GPT_4O"
    python3 examples/build_customized_multi_agents.py --idea "$(cat /home/mert/mlsys/ChatDev/mmlu_prompts/prompt_without_answer_$i.txt)" --log_file="/home/mert/mlsys/meta_gpt/MetaGPT/logs/mmlu_$i.txt"
done
# done

python examples/build_customized_multi_agents.py --log_file "agent_communication.txt"
