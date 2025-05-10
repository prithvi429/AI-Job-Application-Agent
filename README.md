# CV Analyzer & Cover Letter Generator

This project is a web-based application that helps users analyze their CVs, search for jobs, and generate tailored cover letters. It provides an intuitive interface for uploading CVs, entering job-related details, and running various tasks using an AI-powered agent.

## Features
- **Upload CV**: Upload your CV in PDF format.
- **Job Search**: Search for jobs based on keywords and location.
- **CV Analysis**: Analyze your CV to match it with job listings.
- **Cover Letter Generation**: Generate a personalized cover letter.
- **Full Workflow**: Perform all tasks in sequence (Search → Analyze → Generate).

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AI-Job-Application-Agent.git
   cd AI-Job-Application-Agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   streamlit run app.py
   ```
2. Open the application in your browser at `http://localhost:8501`.

## File Structure
- **index.html**: Frontend HTML file for the web interface.
- **styles.css**: CSS file for styling the application.
- **search.py**: Backend logic for job searching.
- **cv_analyzer.py**: Backend logic for CV analysis.
- **app.py**: Main Streamlit application file.

## Requirements
- Python 3.8 or higher
- Streamlit
- Required Python libraries (see `requirements.txt`)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
