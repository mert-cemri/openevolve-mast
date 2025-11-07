# Read project descriptions from file
# Read project names into an array
# Counter to track current project name
counter=0

# Read project descriptions into array
mapfile -t project_names < project_names.txt
mapfile -t project_descriptions < project_descriptions.txt


for ((i=0; i<${#project_names[@]}; i++)); do
    # script "${project_names[$i]}".txt
    # conda activate multiagent
        python examples/build_customized_multi_agents.py --idea "${project_descriptions[$i]}"
        # python run.py --task "${project_descriptions[$i]}" --name "${project_names[$i]}_og" --sample_num "$j" --model "GPT_4O"
        # python run.py --task "${project_descriptions[$i]}" --name "${project_names[$i]}" --sample_num "$j" --model "GPT_4O" --config "Prompted" --org "PromptedOrg"
    # exit
done
