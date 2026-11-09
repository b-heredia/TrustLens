TrustLens — Digital Trust Analyzer

TrustLens is a beginner-friendly Python web application that analyzes URL structures and identifies potential warning indicators.

The goal is to help users become more aware of characteristics that may deserve closer attention before interacting with unfamiliar links.

The Problem
Suspicious links can be designed to look legitimate, making it difficult for users to recognize potential warning signs.
TrustLens provides an accessible way to examine URL structures and understand predefined indicators that may warrant further review.

Features
URL input and analysis through a web interface
Six predefined URL detection categories
Individual explanations for detected warning indicators
Warning summary based on the number of indicators found
Input validation for HTTP and HTTPS URLs

Clear Results functionality
Automated tests for URL analysis and application behavior

Detection Categories
TrustLens examines URLs using six predefined Python checks:
HTTPS Detection: Identifies whether a URL uses HTTPS.

IP Address Detection: Identifies URLs that use an IP address instead of a domain name.

URL Length Detection: Flags URLs longer than 100 characters.
Username Information Detection: Identifies username information embedded in a URL.

URL Shortener Detection: Recognizes selected URL shortening services.

Domain Ending Detection: Flags selected domain endings, including .xyz, .top, and .click.

Technologies Used
Python
Flask
HTML
CSS
Python unittest framework
Project Structure
TrustLens/
│
├── app.py
├── analyzer.py
├── test_analyzer.py
├── test_app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md
Installation and Setup
1. Clone the repository
git clone YOUR_REPOSITORY_URL
cd TrustLens
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment (Windows CMD)
venv\Scripts\activate.bat
4. Install Flask
pip install Flask
5. Run the application
python app.py
Open the following address in your browser:
http://127.0.0.1:5000

Running Tests
Run the automated test suite using:
python -m unittest
The project currently includes 13 automated tests covering URL analysis and Flask application behavior.

Current Limitations
TrustLens uses predefined Python rules to identify potential warning indicators.

It currently does not:
Connect to live threat intelligence databases.
Scan website content.
Verify website reputation.
Guarantee whether a website is safe or malicious.
A warning indicator does not automatically mean a website is malicious. Likewise, finding no warning indicators does not guarantee that a website is safe.
Always verify unfamiliar links before sharing personal information.

Future Development
Potential future improvements include:
Integration with threat intelligence databases.
Domain reputation checks.
More advanced URL analysis.
Additional detection rules.

Project Purpose
TrustLens was developed as a hands-on learning project to build practical experience with Python, Flask, web development, input validation, and automated testing.