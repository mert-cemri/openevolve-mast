'''
DOCSTRING: JavaScript functionality for the calculator operations and display updates.
'''
document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('display');
    const buttons = document.querySelectorAll('.btn');
    let currentInput = '';
    let operator = '';
    let firstOperand = null;
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const value = this.getAttribute('data-value');
            if (value === null) {
                if (this.id === 'clear') {
                    currentInput = '';
                    operator = '';
                    firstOperand = null;
                    display.textContent = '0';
                } else if (this.id === 'equals') {
                    if (firstOperand !== null && operator !== '' && currentInput !== '') {
                        const secondOperand = parseFloat(currentInput);
                        let result;
                        switch (operator) {
                            case '+':
                                result = firstOperand + secondOperand;
                                break;
                            case '-':
                                result = firstOperand - secondOperand;
                                break;
                            case '*':
                                result = firstOperand * secondOperand;
                                break;
                            case '/':
                                if (secondOperand === 0) {
                                    display.textContent = 'Error';
                                    return;
                                }
                                result = firstOperand / secondOperand;
                                break;
                        }
                        display.textContent = result;
                        currentInput = '';
                        operator = '';
                        firstOperand = null;
                    }
                }
            } else if (this.classList.contains('operator')) {
                if (currentInput !== '') {
                    firstOperand = parseFloat(currentInput);
                    operator = value;
                    currentInput = '';
                }
            } else {
                if (value === '.' && currentInput.includes('.')) {
                    return; // Prevent adding another decimal point
                }
                currentInput += value;
                display.textContent = currentInput;
            }
        });
    });
});