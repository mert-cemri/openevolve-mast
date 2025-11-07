'''
Handles file operations for reading Markdown and writing HTML.
'''
class FileHandler:
    def read_markdown(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    def write_html(self, file_path, html_content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)