'''
Contains the MarkdownConverter class for converting Markdown to HTML.
'''
import re
class MarkdownConverter:
    def convert_headers(self, text):
        text = re.sub(r'^(#{1,6})\s*(.+)', lambda m: f"<h{len(m.group(1))}>{m.group(2)}</h{len(m.group(1))}>", text, flags=re.MULTILINE)
        return text
    def convert_bold(self, text):
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        return text
    def convert_italics(self, text):
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        return text
    def convert_lists(self, text):
        # Convert list items
        text = re.sub(r'^\s*-\s+(.+)', r'<li>\1</li>', text, flags=re.MULTILINE)
        # Wrap each list in <ul> tags
        text = re.sub(r'((?:<li>.+?</li>\n?)+)', r'<ul>\1</ul>', text)
        return text
    def convert_links(self, text):
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
        return text
    def convert(self, markdown_text):
        html_text = markdown_text
        html_text = self.convert_headers(html_text)
        html_text = self.convert_bold(html_text)
        html_text = self.convert_italics(html_text)
        html_text = self.convert_lists(html_text)
        html_text = self.convert_links(html_text)
        return html_text