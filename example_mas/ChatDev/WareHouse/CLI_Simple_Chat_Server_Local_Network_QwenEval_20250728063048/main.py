'''
This module contains the implementation of a simple CLI chat server and client.
The server listens for connections from chat clients and broadcasts messages to all connected clients.
The client connects to the server, sends messages, and receives messages from the server.
'''
import asyncio
import time
class ChatServer:
    def __init__(self, host='127.0.0.1', port=65432):
        '''
        Initialize the chat server with a host and port.
        '''
        self.host = host
        self.port = port
        self.clients = set()
    async def handle_client(self, reader, writer):
        '''
        Handle a client connection.
        Add the client to the set of clients, receive messages, and broadcast them.
        '''
        self.clients.add(writer)
        try:
            while True:
                data = await reader.read(100)
                if not data:
                    break
                message = data.decode()
                print(f'Received: {message}')
                await self.broadcast(message, writer)
        except Exception as e:
            print(f'Error handling client: {e}')
        finally:
            writer.close()
            await writer.wait_closed()
            self.clients.remove(writer)
    async def broadcast(self, message, sender):
        '''
        Broadcast a message to all connected clients except the sender.
        Handle exceptions that might occur during writing and draining.
        '''
        for client in self.clients:
            if client != sender:
                try:
                    client.write(message.encode())
                    await client.drain()
                except Exception as e:
                    print(f'Error broadcasting message: {e}')
    async def run(self):
        '''
        Start the chat server.
        Listen for incoming connections and handle them asynchronously.
        '''
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')
        async with server:
            await server.serve_forever()
class ChatClient:
    def __init__(self, host='127.0.0.1', port=65432):
        '''
        Initialize the chat client with a host and port.
        '''
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None
    async def connect(self):
        '''
        Connect to the chat server with a retry mechanism.
        '''
        max_retries = 5
        retry_delay = 2  # seconds
        for attempt in range(max_retries):
            try:
                self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
                print(f'Connected to {self.host}:{self.port}')
                return
            except ConnectionRefusedError:
                print(f'Attempt {attempt + 1} to connect failed. Retrying in {retry_delay} seconds...')
                await asyncio.sleep(retry_delay)
        raise ConnectionRefusedError(f'Failed to connect to {self.host}:{self.port} after {max_retries} attempts.')
    async def send_message(self, message):
        '''
        Send a message to the server.
        '''
        self.writer.write(message.encode())
        await self.writer.drain()
    async def receive_messages(self):
        '''
        Receive messages from the server.
        Handle exceptions that might occur during reading.
        '''
        while True:
            try:
                data = await self.reader.read(100)
                if not data:
                    print('Server disconnected.')
                    break
                message = data.decode()
                print(f'Received: {message}')
            except Exception as e:
                print(f'Error receiving message: {e}')
                break
    async def run(self):
        '''
        Run the chat client.
        Connect to the server, send messages, and receive messages concurrently.
        '''
        await self.connect()
        reader_task = asyncio.create_task(self.receive_messages())
        try:
            while True:
                try:
                    message = await asyncio.to_thread(input, 'Enter message: ')
                except KeyboardInterrupt:
                    print('Exiting chat.')
                    break
                await self.send_message(message)
        finally:
            print('Closing connection')
            self.writer.close()
            await self.writer.wait_closed()
            reader_task.cancel()
            await reader_task
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'server':
        server = ChatServer()
        asyncio.run(server.run())
    else:
        client = ChatClient()
        asyncio.run(client.run())