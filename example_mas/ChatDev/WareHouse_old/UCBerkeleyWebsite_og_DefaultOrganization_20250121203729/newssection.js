'''
This JavaScript file defines the NewsSection component, which displays a list of news items and events for UC Berkeley.
'''
import React from 'react';
function NewsSection() {
    const newsItems = [
        { id: 1, title: 'New Research Breakthrough', date: '2023-10-01' },
        { id: 2, title: 'Upcoming Campus Events', date: '2023-10-05' },
        { id: 3, title: 'Alumni Success Stories', date: '2023-10-10' }
    ];
    return (
        <div className="news-section">
            <h2>News & Events</h2>
            {newsItems.map(item => (
                <div key={item.id} className="news-item">
                    <h3>{item.title}</h3>
                    <p>Date: {item.date}</p>
                </div>
            ))}
        </div>
    );
}
export default NewsSection;