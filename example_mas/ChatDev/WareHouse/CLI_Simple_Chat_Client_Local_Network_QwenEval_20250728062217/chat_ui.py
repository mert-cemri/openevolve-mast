'''
Handles the user interface, displaying messages and taking user input.
'''
import threading
class ChatUI:
    def __init__(self, chat_client):
        self.chat_client = chat_client
        self.chat_client.set_message_callback(self.display_message)
        self.running = False
    def start(self):
        self.running = True
        self.chat_client.connect()
        # Start a thread to receive messages
        receive_thread = threading.Thread(target=self.chat_client.receive_messages)
        receive_thread.start()
        # Main loop for sending messages
        print("Type 'exit' to quit the chat.")
        while self.running:
            message = self.get_user_input()
            if message.lower() == 'exit':
                self.running = False
                self.chat_client.disconnect()
                break
            self.chat_client.send_message(message)
    def display_message(self, message):
        print(f"Received: {message}")
    def get_user_input(self):
        return input("Enter message: ")