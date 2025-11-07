# User Manual for `get_closest_vowel` Function

## Introduction

The `get_closest_vowel` function is a Python utility designed to identify the closest vowel in a given word that stands between two consonants, starting from the right side of the word. This function is case-sensitive and excludes vowels at the beginning and end of the word from consideration. If no such vowel is found, the function returns an empty string.

### Key Features

- **Case Sensitivity**: The function respects the case of the letters, distinguishing between uppercase and lowercase vowels.
- **Exclusion of Edge Vowels**: Vowels at the beginning and end of the word are not considered.
- **Right-to-Left Processing**: The function processes the word from right to left, ensuring the closest vowel is identified.

## Installation

This function does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

## Usage

To use the `get_closest_vowel` function, follow these steps:

1. **Copy the Code**: Copy the function code into your Python script or interactive environment.

    ```python
    def get_closest_vowel(word):
        """You are given a word. Your task is to find the closest vowel that stands between 
        two consonants from the right side of the word (case sensitive).
        Vowels in the beginning and ending doesn't count. Return empty string if you didn't
        find any vowel met the above condition. 
        You may assume that the given string contains English letter only.
        Example:
        get_closest_vowel("yogurt") ==> "u"
        get_closest_vowel("FULL") ==> "U"
        get_closest_vowel("quick") ==> ""
        get_closest_vowel("ab") ==> ""
        """
        vowels = "aeiouAEIOU"
        length = len(word)
        # Iterate from the second last character to the second character
        for i in range(length - 2, 0, -1):
            if word[i] in vowels:
                # Check if the surrounding characters are consonants
                if word[i-1] not in vowels and word[i+1] not in vowels:
                    return word[i]
        return ""
    ```

2. **Call the Function**: Use the function by passing a word as an argument.

    ```python
    result = get_closest_vowel("yogurt")
    print(result)  # Output: "u"
    ```

3. **Interpret the Result**: The function will return the closest vowel between two consonants from the right side of the word. If no such vowel exists, it will return an empty string.

## Examples

- `get_closest_vowel("yogurt")` returns `"u"`.
- `get_closest_vowel("FULL")` returns `"U"`.
- `get_closest_vowel("quick")` returns `""`.
- `get_closest_vowel("ab")` returns `""`.

## Conclusion

The `get_closest_vowel` function is a simple yet effective tool for identifying specific vowel patterns within words. Its straightforward implementation and lack of dependencies make it easy to integrate into larger projects or use in standalone scripts.