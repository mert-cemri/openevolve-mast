'''
JavaScript module to create and manage the navigation bar.
'''
function initializeNavbar() {
    const navbar = document.getElementById('navbar');
    navbar.innerHTML = `
        <nav>
            <button id="menu-toggle" aria-label="Toggle navigation menu">☰</button>
            <ul>
                <li><a href="#admissions" aria-label="Admissions">Admissions</a></li>
                <li><a href="#academics" aria-label="Academics">Academics</a></li>
                <li><a href="#research" aria-label="Research">Research</a></li>
                <li><a href="#news" aria-label="News and Events">News & Events</a></li>
            </ul>
        </nav>
    `;
    const menuToggle = document.getElementById('menu-toggle');
    const nav = navbar.querySelector('nav');
    nav.classList.add('active'); // Initially hide the navigation links
    menuToggle.addEventListener('click', () => {
        nav.classList.toggle('active');
    });
}
export { initializeNavbar };