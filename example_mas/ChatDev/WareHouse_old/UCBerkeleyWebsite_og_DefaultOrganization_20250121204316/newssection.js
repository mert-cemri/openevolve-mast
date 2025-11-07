'''
NewsSection component that displays a list of news or events.
'''
import React from 'react';
function NewsSection() {
  return (
    <section id="news" aria-labelledby="news-heading">
      <h2 id="news-heading">News & Events</h2>
      <ul>
        <li>Event 1: Description...</li>
        <li>Event 2: Description...</li>
        <li>Event 3: Description...</li>
      </ul>
    </section>
  );
}
export default NewsSection;