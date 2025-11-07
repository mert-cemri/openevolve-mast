'''
Header component that includes the university's brand elements and navigation links.
'''
import React from 'react';
function Header() {
  return (
    <header className="header">
      <div className="brand">
        <img src="ucb-logo.png" alt="UC Berkeley Logo" />
        <h1>UC Berkeley</h1>
      </div>
      <nav aria-label="Main Navigation">
        <ul>
          <li><a href="#admissions" aria-label="Admissions Section">Admissions</a></li>
          <li><a href="#academics" aria-label="Academics Section">Academics</a></li>
          <li><a href="#research" aria-label="Research Section">Research</a></li>
          <li><a href="#news" aria-label="News and Events Section">News</a></li>
        </ul>
      </nav>
    </header>
  );
}
export default Header;