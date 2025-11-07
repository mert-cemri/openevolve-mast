for i in {162..163}; do
    # Inner loop for sample_num values from 0 to 5
    for j in {0..5}; do
        # Construct the name value and execute the Python script
        name="HumanEval/$i"
        python eval_og.py --name "$name" --sample_num $j --model "GPT_4O"
    done
done
