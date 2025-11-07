'''
Main application file that renders the entire website layout.
'''
import React from 'react';
import Header from './Header';
import Footer from './Footer';
import MainContent from './MainContent';
import './styles.css';
function App() {
  return (
    <div className="App">
      <Header />
      <MainContent />
      <Footer />
    </div>
  );
}
export default App;