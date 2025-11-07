# Markdown to HTML Converter

A simple command-line interface (CLI) application for converting Markdown files to HTML format.

## Introduction

The Markdown to HTML Converter is a tool designed to transform Markdown files into HTML format. It supports common Markdown syntax, including headers, bold, italics, lists, and links. This tool is perfect for users who want to quickly convert their Markdown documents into HTML for web publishing or other purposes.

## Features

- **Headers**: Convert Markdown headers (e.g., `#`, `##`, `###`) into HTML header tags (`<h1>`, `<h2>`, `<h3>`, etc.).
- **Bold Text**: Convert text wrapped in double asterisks (`**bold**`) into HTML `<strong>` tags.
- **Italics**: Convert text wrapped in single asterisks (`*italic*`) into HTML `<em>` tags.
- **Lists**: Convert unordered lists (e.g., `* item`) into HTML `<ul>` and `<li>` tags.
- **Links**: Convert Markdown links (`[text](url)`) into HTML `<a>` tags.

## Installation

### Environment Setup

This project does not require any external dependencies, making it easy to set up and use. Ensure you have Python installed on your system.

### Quick Install

1. **Clone the Repository**: Download or clone the project repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **No External Dependencies**: This project does not require any additional Python packages beyond the standard library. Simply ensure you have Python installed.

## Usage

### Running the Converter

To use the Markdown to HTML Converter, follow these steps:

1. **Open a Terminal**: Navigate to the directory where the project files are located.

2. **Run the Application**: Execute the following command, replacing `<input_file>` with the path to your Markdown file and `<output_file>` with the desired path for the HTML output.

   ```bash
   python main.py <input_file> <output_file>
   ```

   Example:

   ```bash
   python main.py example.md example.html
   ```

3. **Output**: The converted HTML file will be saved at the specified output path. A confirmation message will be displayed in the terminal.

### Example

Given a Markdown file `example.md` with the following content:

```markdown
# Welcome

This is a **bold** statement and this is *italic* text.

* Item 1
* Item 2

[Visit ChatDev](https://chatdev.com)
```

Running the converter will produce an HTML file `example.html` with the following content:

```html
<h1>Welcome</h1>
<p>This is a <strong>bold</strong> statement and this is <em>italic</em> text.</p>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<p><a href="https://chatdev.com">Visit ChatDev</a></p>
```

## Conclusion

The Markdown to HTML Converter is a straightforward tool for converting Markdown documents into HTML format. With support for common Markdown syntax, it provides a quick and easy way to prepare documents for web publishing. Enjoy using the converter and happy coding!