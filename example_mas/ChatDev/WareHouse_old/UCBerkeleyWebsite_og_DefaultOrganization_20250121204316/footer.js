'''
Footer component that includes contact details and social media links.
'''
import React from 'react';
function Footer() {
  return (
    <footer className="footer" role="contentinfo">
      <p>Contact us: info@berkeley.edu</p>
      <div className="social-media">
        <a href="https://facebook.com/ucberkeley" aria-label="UC Berkeley Facebook Page">Facebook</a>
        <a href="https://twitter.com/ucberkeley" aria-label="UC Berkeley Twitter Page">Twitter</a>
      </div>
    </footer>
  );
}
export default Footer;