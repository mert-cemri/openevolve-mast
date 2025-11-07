'''
JavaScript for interactive elements on the UC Berkeley landing page.
'''
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('nav');
    const menuItems = nav.querySelectorAll('ul li a');
    hamburger.addEventListener('click', function() {
        const isActive = nav.classList.toggle('active');
        hamburger.setAttribute('aria-expanded', isActive);
        if (isActive) {
            menuItems.forEach(item => item.setAttribute('tabindex', '0'));
        } else {
            menuItems.forEach(item => item.setAttribute('tabindex', '-1'));
        }
    });
    hamburger.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' || event.key === ' ') {
            const isActive = nav.classList.toggle('active');
            hamburger.setAttribute('aria-expanded', isActive);
            if (isActive) {
                menuItems.forEach(item => item.setAttribute('tabindex', '0'));
            } else {
                menuItems.forEach(item => item.setAttribute('tabindex', '-1'));
            }
        }
    });
    // Example of dynamic content loading
    const newsSection = document.getElementById('news');
    fetchNews().then(news => {
        newsSection.innerHTML += news.map(item => `<p>${item}</p>`).join('');
    });
});
async function fetchNews() {
    // Simulate fetching news data
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(['News Item 1', 'News Item 2', 'News Item 3']);
        }, 1000);
    });
}