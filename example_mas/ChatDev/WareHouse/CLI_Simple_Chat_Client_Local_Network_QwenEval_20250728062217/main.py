'''
Main entry point for the CLI chat client.
Initializes the chat client and UI, and starts the UI loop.
'''
import chat_client
import chat_ui
def main():
    server_ip = '127.0.0.1'  # Localhost
    server_port = 12345      # Arbitrary non-privileged port
    client = chat_client.ChatClient(server_ip, server_port)
    ui = chat_ui.ChatUI(client)
    ui.start()
if __name__ == '__main__':
    main()