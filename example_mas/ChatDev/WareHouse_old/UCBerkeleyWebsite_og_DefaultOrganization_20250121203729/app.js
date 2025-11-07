'''
This JavaScript file uses React to render the main components of the UC Berkeley Landing Page, including the header, navigation, main content, and footer.
'''
import React from 'react';
import ReactDOM from 'react-dom';
import Navbar from './Navbar';
import NewsSection from './NewsSection';
import Footer from './Footer';
function App() {
    return (
        <div>
            <header>
                <h1>Welcome to UC Berkeley</h1>
            </header>
            <Navbar />
            <main>
                <h2>About UC Berkeley</h2>
                <p>UC Berkeley is a world-renowned university known for its academic excellence and vibrant campus life.</p>
                <NewsSection />
            </main>
            <Footer />
        </div>
    );
}
ReactDOM.render(<App />, document.getElementById('root'));