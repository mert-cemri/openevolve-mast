'''
Main entry point for the interactive storytelling game.
'''
from story import Story
from player import Player
def main():
    print("Welcome to the Interactive Storytelling Game!")
    player = Player()
    story = Story(player)
    story.load_story()
    current_node = story.get_start_node()
    while current_node:
        print("\n" + current_node.text)
        if current_node.is_end_node():
            print("\n--- THE END ---")
            break
        for idx, choice in enumerate(current_node.choices, 1):
            print(f"{idx}. {choice['text']}")
        valid_choice = False
        while not valid_choice:
            try:
                choice_input = int(input("Choose an option: "))
                if 1 <= choice_input <= len(current_node.choices):
                    valid_choice = True
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        chosen_choice = current_node.choices[choice_input - 1]
        current_node = story.get_next_node(chosen_choice)
if __name__ == "__main__":
    main()