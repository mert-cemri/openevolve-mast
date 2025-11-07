'''
Handles command-line interactions for the file archiver application.
'''
class CLI:
    def __init__(self, archiver):
        self.archiver = archiver
    def run(self):
        '''
        Starts the CLI interface for user interaction.
        '''
        print("Welcome to the CLI File Archiver")
        while True:
            command = input("Enter command (create/extract/exit): ").strip().lower()
            if command == "create":
                zip_name = input("Enter the name of the ZIP file to create: ")
                files = input("Enter the files/directories to add (comma-separated): ").split(',')
                self.archiver.create_zip(zip_name, [f.strip() for f in files])
                print(f"Created {zip_name}")
            elif command == "extract":
                zip_name = input("Enter the name of the ZIP file to extract: ")
                extract_to = input("Enter the directory to extract files to: ")
                self.archiver.extract_zip(zip_name, extract_to)
                print(f"Extracted {zip_name} to {extract_to}")
            elif command == "exit":
                print("Exiting CLI File Archiver")
                break
            else:
                print("Invalid command. Please try again.")