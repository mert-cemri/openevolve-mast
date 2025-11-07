'''
Handles the conversion of Markdown text to HTML.
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
        text = re.sub(r'^\*\s+(.+)', r'<li>\1</li>', text, flags=re.MULTILINE)
        # Wrap the list items with <ul> tags
        text = re.sub(r'(<li>.*?</li>)', r'<ul>\n\1\n</ul>', text, flags=re.DOTALL)
        # Ensure that multiple list items are grouped under a single <ul> tag
        text = re.sub(r'(<ul>\n<li>.*?</li>\n</ul>)(\n<ul>\n<li>.*?</li>\n</ul>)+', lambda m: f"<ul>\n{''.join(re.findall(r'<li>.*?</li>', m.group(0)))}\n</ul>", text, flags=re.DOTALL)
        return text
    def convert_links(self, text):
        text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', text)
        return text
    def convert(self, markdown_text):
        html_text = self.convert_headers(markdown_text)
        html_text = self.convert_bold(html_text)
        html_text = self.convert_italics(html_text)
        html_text = self.convert_lists(html_text)
        html_text = self.convert_links(html_text)
        return html_text