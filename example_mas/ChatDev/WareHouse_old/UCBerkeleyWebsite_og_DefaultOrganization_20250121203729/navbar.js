'''
This JavaScript file defines the Navbar component, which provides navigation links to major sections of the UC Berkeley Landing Page.
'''
import React from 'react';
function Navbar() {
    return (
        <nav aria-label="Main Navigation">
            <a href="#admissions" aria-label="Admissions Section">Admissions</a>
            <a href="#academics" aria-label="Academics Section">Academics</a>
            <a href="#research" aria-label="Research Section">Research</a>
            <a href="#news" aria-label="News Section">News</a>
        </nav>
    );
}
export default Navbar;