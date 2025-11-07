'''
Main entry point for the CLI Markdown to HTML converter application.
'''
from app import MarkdownToHtmlApp
if __name__ == "__main__":
    app = MarkdownToHtmlApp()
    app.run()