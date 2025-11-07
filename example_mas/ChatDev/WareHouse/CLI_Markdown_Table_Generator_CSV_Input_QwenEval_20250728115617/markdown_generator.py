'''
Markdown generator to convert parsed data into a Markdown table.
'''
class MarkdownGenerator:
    def generate_table(self, data):
        if not data:
            return "No data to generate table."
        headers = data[0].keys()
        header_row = " | ".join(headers)
        separator_row = " | ".join(["---"] * len(headers))
        rows = [header_row, separator_row]
        for row in data:  # Start from the first row as the first is the header
            rows.append(" | ".join(row.values()))
        return "\n".join(rows)