# Stone Pile Builder

This software is designed to create a pile of stones with a specified number of levels. Each level of the pile contains a specific number of stones, determined by the rules outlined below.

## Main Functionality

The main function of this software is `make_a_pile(n)`, which constructs a pile of stones with `n` levels. The number of stones in each level is determined as follows:

- The first level contains `n` stones.
- For each subsequent level, the number of stones is:
  - The next odd number if the current number of stones is odd.
  - The next even number if the current number of stones is even.

### Example

For example, calling `make_a_pile(3)` will return `[3, 5, 7]`, meaning:
- Level 1 has 3 stones.
- Level 2 has 5 stones (the next odd number after 3).
- Level 3 has 7 stones (the next odd number after 5).

## Installation

To use this software, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: If you haven't already, download and install Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the `main.py` file to your local machine.

3. **Set Up Environment**: Although there are no specific dependencies listed in `requirements.txt`, ensure your Python environment is set up correctly.

## Usage

To use the software, follow these steps:

1. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

2. **Run the Script**: Execute the script by running the following command:
   ```bash
   python main.py
   ```

3. **Example Usage**: The script includes an example usage of the `make_a_pile` function. You can modify the `n` value in the script to test different scenarios.

## Customization

You can customize the script by changing the input value `n` in the `make_a_pile` function call within the `main.py` file. This allows you to generate stone piles with different numbers of levels.

## Support

For any issues or questions regarding the software, please contact our support team at support@chatdev.com.

---

This user manual provides a comprehensive guide to using the Stone Pile Builder software. Follow the instructions carefully to ensure a smooth setup and usage experience.