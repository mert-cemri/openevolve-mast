
# Read project descriptions from file
# Read project names into an array
mapfile -t project_names < project_names.txt

# Counter to track current project name
counter=0

# Read project descriptions into array
mapfile -t project_descriptions < project_descriptions.txt

for j in {0..1}; do
    for ((i=0; i<30; i++)); do
        python run.py --task "$(cat mmlu_prompts/prompt_without_answer_$i.txt)" --name "mmlu_$i" --sample_num "$j" --model "GPT_4O"
    done
done
