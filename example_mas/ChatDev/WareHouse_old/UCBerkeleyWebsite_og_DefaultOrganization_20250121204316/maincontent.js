'''
MainContent component that renders the main sections of the website.
'''
import React from 'react';
import NewsSection from './NewsSection';
function MainContent() {
  return (
    <main className="main-content">
      <section id="admissions" aria-labelledby="admissions-heading">
        <h2 id="admissions-heading">Admissions</h2>
        <p>Information about admissions...</p>
      </section>
      <section id="academics" aria-labelledby="academics-heading">
        <h2 id="academics-heading">Academics</h2>
        <p>Information about academics...</p>
      </section>
      <section id="research" aria-labelledby="research-heading">
        <h2 id="research-heading">Research</h2>
        <p>Information about research...</p>
      </section>
      <NewsSection />
    </main>
  );
}
export default MainContent;