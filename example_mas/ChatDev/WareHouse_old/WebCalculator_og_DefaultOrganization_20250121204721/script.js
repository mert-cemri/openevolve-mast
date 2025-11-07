'''
Implements the logic for handling user interactions and performing calculations.
'''
document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('display');
    let currentInput = '';
    let operator = null;
    let firstOperand = null;
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', () => {
            const value = button.getAttribute('data-value');
            if (value === '=') {
                if (firstOperand !== null && operator !== null) {
                    currentInput = calculate(firstOperand, currentInput, operator);
                    display.innerText = currentInput;
                    firstOperand = null;
                    operator = null;
                }
            } else if (['+', '-', '*', '/'].includes(value)) {
                if (currentInput === '' && firstOperand === null) return; // Prevent starting with an operator
                if (operator !== null && currentInput === '') return; // Prevent consecutive operators
                if (firstOperand === null) {
                    firstOperand = currentInput;
                    operator = value;
                    currentInput = '';
                } else if (operator !== null) {
                    firstOperand = calculate(firstOperand, currentInput, operator);
                    operator = value;
                    currentInput = '';
                    display.innerText = firstOperand;
                }
            } else if (value === '.') {
                if (!currentInput.includes('.')) {
                    currentInput += value;
                    display.innerText = currentInput;
                }
            } else {
                if (currentInput === '0') currentInput = ''; // Remove leading zero
                currentInput += value;
                display.innerText = currentInput;
            }
        });
    });
    function calculate(first, second, operator) {
        const num1 = parseFloat(first);
        const num2 = parseFloat(second);
        switch (operator) {
            case '+':
                return (num1 + num2).toString();
            case '-':
                return (num1 - num2).toString();
            case '*':
                return (num1 * num2).toString();
            case '/':
                if (num2 === 0) {
                    return "Error"; // Handle division by zero
                }
                return (num1 / num2).toString();
            default:
                return second;
        }
    }
});