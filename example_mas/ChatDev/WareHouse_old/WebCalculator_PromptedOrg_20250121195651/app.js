'''
DOCSTRING: This file initializes the calculator and handles event listeners for user interactions.
'''
import Calculator from './calculator.js';
document.addEventListener('DOMContentLoaded', () => {
    const displayElement = document.getElementById('display');
    const calculator = new Calculator(displayElement);
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const value = button.getAttribute('data-value');
            if (value >= '0' && value <= '9' || value === '.') {
                calculator.appendNumber(value);
                calculator.updateDisplay();
            } else if (value === '+' || value === '-' || value === '*' || value === '/') {
                calculator.chooseOperation(value);
                calculator.updateDisplay();
            } else if (value === '=') {
                calculator.compute();
                calculator.updateDisplay();
            } else if (value === 'C') {
                calculator.clear();
                calculator.updateDisplay();
            }
        });
    });
});