'''
DOCSTRING: JavaScript to manage the news or events section on UC Berkeley's landing page.
'''
document.addEventListener('DOMContentLoaded', () => {
    const newsContainer = document.getElementById('news-container');
    const newsItems = [
        { title: 'Event 1', date: '2023-10-01', description: 'Description of event 1.' },
        { title: 'Event 2', date: '2023-10-15', description: 'Description of event 2.' },
    ];
    newsItems.forEach(item => {
        const newsElement = document.createElement('div');
        newsElement.classList.add('news-item');
        newsElement.innerHTML = `<h3>${item.title}</h3><p>${item.date}</p><p>${item.description}</p>`;
        newsContainer.appendChild(newsElement);
    });
});