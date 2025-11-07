manual.md

```
# Palindrome Detector

A simple yet powerful Python application designed to detect palindromes within text files. It supports both word-level and phrase-level palindrome detection, providing users with an easy-to-use interface to analyze text files quickly and efficiently.

---

## 🚀 Key Features

- **Word-Level Palindrome Detection:** Identifies individual words that are palindromes.
- **Phrase-Level Palindrome Detection:** Detects palindromic phrases or sentences, ignoring spaces, punctuation, and case sensitivity.
- **User-Friendly Interface:** Easy-to-follow prompts and clear output formatting.
- **No External Dependencies:** Lightweight and easy to set up, requiring only Python.

---

## ⚙️ Installation

### Prerequisites

- Python 3.6 or higher installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone or Download the Repository

Clone the repository using Git:

```bash
git clone <repository-url>
cd <repository-directory>
```

Alternatively, download and extract the ZIP file from the provided source.

### Install Dependencies

This application does not require any external dependencies. However, it is recommended to use a virtual environment for Python projects:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

---

## 🛠️ Usage

### Running the Application

To run the palindrome detector, execute the following command in your terminal:

```bash
python main.py
```

### Analyzing a Text File

Upon running the application, you will be prompted to enter the path to the text file you wish to analyze:

```bash
Enter the path to the text file: example.txt
```

Replace `example.txt` with the path to your text file.

### Example Output

If palindromes are detected, the application will display them clearly separated into word-level and phrase-level categories:

```
Word-level palindromes found in the file:
- civic
- level
- radar

Phrase-level palindromes found in the file:
- A man, a plan, a canal, Panama
- Was it a car or a cat I saw
```

If no palindromes are detected, the application will inform you accordingly:

```
No word-level palindromes found in the file.

No phrase-level palindromes found in the file.
```

---

## 📁 Project Structure

```
PalindromeDetector/
├── main.py                 # Main executable script
├── palindrome_detector.py  # Core palindrome detection logic
├── requirements.txt        # Dependency file (empty, no external dependencies)
└── manual.md               # User manual (this document)
```

---

## 📖 Definitions

- **Palindrome:** A word, phrase, or sequence that reads the same backward as forward, e.g., "madam" or "A man, a plan, a canal, Panama".

---

## ❓ Troubleshooting

### File Not Found Error

If you encounter a "File not found" error, ensure the file path you entered is correct and the file exists in the specified location.

### Unexpected Errors

For any unexpected errors, please check your Python environment and ensure you are using Python 3.6 or higher.

---

## 📞 Support

For further assistance or to report issues, please contact our support team or open an issue in the project's GitHub repository.

Happy palindrome detecting! 🚀
```