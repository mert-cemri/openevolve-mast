python run.py --task "Design a simple 2048 game with 4*4 grids. It should be playable from Linux Terminal, and does not require me to access a dedicated UX or GUI platform, i.e. print the results on terminal at each stage and let me play it there by entering inputs." --name "2048_linux" --model "GPT_4O" --config "Prompted" --org "PromptedOrg" 

python run.py --task "Design a tic-tac-toe game with a user-friendly interface, allowing two players to take turns and determining the winner. It should be playable from Linux Terminal, and does not require me to access a dedicated UX or GUI platform, i.e. print the results on terminal at each stage and let me play it there by entering inputs." --name "TicTacToe_linux" --model "GPT_4O" --config "Prompted" --org "PromptedOrg" 

python run.py --task "Design a chess game, allowing two players to take turns and determining the winner. It should be playable from Linux Terminal, and does not require me to access a dedicated UX or GUI platform, i.e. print the results on terminal at each stage and let me play it there by entering inputs (formal chess notation such as Ke8)." --name "Chess_linux" --model "GPT_4O"

python run.py --task "Design a chess game, allowing two players to take turns and determining the winner. It should be playable from Linux Terminal, and does not require me to access a dedicated UX or GUI platform, i.e. print the results on terminal at each stage and let me play it there by entering inputs (formal chess notation such as Ke8)." --name "Chess_linux_new" --model "GPT_4O" --config "Prompted" --org "PromptedOrg" 

python run.py --task "Design a simple 2048 game with 4*4 grids. It should be playable from Linux Terminal, and does not require me to access a dedicated UX or GUI platform, i.e. print the results on terminal at each stage and let me play it there by entering inputs." --name "2048_linux_new" --model "GPT_4O" --config "Prompted" --org "PromptedOrg" 

python eval.py --name "human_eval_0" --model "GPT_4O" --config "Prompted" --org "PromptedOrg" 

python eval.py --name "HumanEval/0" --sample_num 0 --model "GPT_4O" --config "Prompted" --org "PromptedOrg" 