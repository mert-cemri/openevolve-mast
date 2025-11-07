'''
Entry point of the application. Initializes the client and starts the chat session.
'''
from client import ChatClient  # Import the ChatClient class
def main():
    client = ChatClient()
    client.run()
if __name__ == "__main__":
    main()