
# Read project descriptions from file
# Read project names into an array
mapfile -t project_names < project_names.txt

# Counter to track current project name
counter=0

# Read project descriptions into array
mapfile -t project_descriptions < project_descriptions.txt

for ((i=3; i<${#project_names[@]}; i++)); do
    for j in {0..2}; do
        python run.py --task "${project_descriptions[$i]}" --name "${project_names[$i]}_og" --sample_num "$j" --model "GPT_4O"
        # python run.py --task "${project_descriptions[$i]}" --name "${project_names[$i]}" --sample_num "$j" --model "GPT_4O" --config "Prompted" --org "PromptedOrg"
    done
done
