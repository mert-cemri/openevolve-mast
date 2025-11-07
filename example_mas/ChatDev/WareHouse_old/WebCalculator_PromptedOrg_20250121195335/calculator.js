'''
DOCSTRING: JavaScript logic for the responsive web-based calculator.
'''
document.addEventListener('DOMContentLoaded', initCalculator);
function initCalculator() {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', handleButtonClick);
    });
}
let expression = '';
function handleButtonClick(event) {
    const value = event.target.getAttribute('data-value');
    const display = document.getElementById('display');
    if (value === 'C') {
        clearDisplay();
    } else if (value === '=') {
        calculateResult();
    } else {
        expression += value;
        display.textContent = expression;
    }
}
function calculateResult() {
    const display = document.getElementById('display');
    try {
        const result = eval(expression);
        display.textContent = result;
        expression = result.toString();
    } catch (error) {
        display.textContent = 'Error';
        expression = '';
    }
}
function clearDisplay() {
    const display = document.getElementById('display');
    expression = '';
    display.textContent = '0';
}