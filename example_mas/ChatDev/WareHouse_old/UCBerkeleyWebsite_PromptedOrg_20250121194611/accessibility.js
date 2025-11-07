'''
DOCSTRING: JavaScript to ensure accessibility features on UC Berkeley's landing page.
'''
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.setAttribute('tabindex', '0');
    });
    // Implement keyboard navigation for the navigation menu
    document.addEventListener('keydown', (event) => {
        const focusedElement = document.activeElement;
        if (focusedElement.tagName === 'A' && focusedElement.parentElement.parentElement.parentElement.tagName === 'NAV') {
            let index = Array.from(navLinks).indexOf(focusedElement);
            if (event.key === 'ArrowRight') {
                index = (index + 1) % navLinks.length;
                navLinks[index].focus();
            } else if (event.key === 'ArrowLeft') {
                index = (index - 1 + navLinks.length) % navLinks.length;
                navLinks[index].focus();
            }
        }
    });
});