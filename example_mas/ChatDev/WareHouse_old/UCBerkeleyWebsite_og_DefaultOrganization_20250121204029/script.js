'''
JavaScript file for interactivity on UC Berkeley's landing page prototype.
'''
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });
        });
    });
    // Load news/events dynamically
    const newsContainer = document.getElementById('news-container');
    fetch('https://jsonplaceholder.typicode.com/posts') // Using a mock API for demonstration
        .then(response => response.json())
        .then(data => {
            data.slice(0, 5).forEach(newsItem => { // Limiting to 5 items for brevity
                const newsElement = document.createElement('div');
                newsElement.className = 'news-item';
                newsElement.innerHTML = `<h3>${newsItem.title}</h3><p>${newsItem.body}</p>`;
                newsContainer.appendChild(newsElement);
            });
        })
        .catch(error => console.error('Error fetching news:', error));
});