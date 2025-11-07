# UC Berkeley Website Prototype

This user manual provides detailed instructions on how to use the UC Berkeley website prototype. This prototype is designed to be a modern, responsive landing page featuring UC Berkeley's brand elements, navigation for major sections, and a news or events section. It ensures accessibility and mobile-friendly design.

## Main Functions

The UC Berkeley website prototype includes the following main functions:

- **Responsive Design**: The website is designed to be responsive, ensuring it looks good on all devices, including desktops, tablets, and mobile phones.
- **Navigation**: A navigation menu allows users to easily access major sections such as Admissions, Academics, Research, and News & Events.
- **News & Events Section**: A dynamic section that displays the latest news and events related to UC Berkeley.
- **Accessibility Features**: The website includes accessibility features such as keyboard navigation to ensure it is usable by all individuals.

## Installation

To set up the environment and run the UC Berkeley website prototype, follow these steps:

1. **Clone the Repository**: Clone the repository containing the website prototype to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change into the project directory.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Ensure you have a web server to serve the HTML files. You can use a simple HTTP server like `http-server` for Node.js.

   ```bash
   npm install -g http-server
   ```

## Usage

To use the UC Berkeley website prototype, follow these steps:

1. **Start the Server**: Start the HTTP server to serve the website files.

   ```bash
   http-server
   ```

2. **Access the Website**: Open your web browser and navigate to the URL provided by the HTTP server (usually `http://localhost:8080`).

3. **Explore the Website**: Use the navigation menu to explore different sections of the website. The sections include:
   - **Admissions**: Information about UC Berkeley's admissions process.
   - **Academics**: Details about academic programs and offerings.
   - **Research**: Information on research initiatives and projects.
   - **News & Events**: Latest news and upcoming events.

4. **Accessibility**: Use the keyboard to navigate through the website. Use the arrow keys to move between navigation links.

## Additional Information

- **Customization**: You can customize the content and styles by editing the `index.html`, `styles.css`, and JavaScript files (`script.js`, `accessibility.js`, `news.js`).
- **Dynamic Content**: The `news.js` file manages the dynamic content for the News & Events section. You can add or modify news items in this file.

For any further assistance or support, please contact the development team.