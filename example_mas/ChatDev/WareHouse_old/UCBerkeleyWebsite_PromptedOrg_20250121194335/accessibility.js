'''
JavaScript to enhance accessibility features on the UC Berkeley landing page.
'''
document.addEventListener('DOMContentLoaded', function() {
    // Ensure keyboard navigation
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('focus', function() {
            this.style.outline = '2px solid #ffb300';
        });
        link.addEventListener('blur', function() {
            this.style.outline = 'none';
        });
    });
    // Add ARIA roles
    document.querySelector('nav').setAttribute('role', 'navigation');
    document.querySelector('main').setAttribute('role', 'main');
    document.querySelector('footer').setAttribute('role', 'contentinfo');
});