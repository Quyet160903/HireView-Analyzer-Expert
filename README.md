# HireView Analyzer Expert

## 📄 Overview
HireView Analyzer Expert is an AI-powered resume screening tool designed to assist job seekers and recruiters in evaluating resumes against job descriptions. The tool leverages cutting-edge AI models, such as OpenAI's GPT-4o and Google's Gemini, to analyze resumes, provide detailed insights, and offer improvement suggestions.

## ✨ Features
- **AI-Powered Resume Analysis**: Extracts key information from resumes and compares them with job descriptions.
- **Match Percentage Calculation**: Determines how well a resume aligns with the job requirements.
- **Insightful Feedback & Suggestions**: Highlights strengths and areas for improvement.
- **Multiple AI Model Support**: Choose between OpenAI's GPT-4o and Google's Gemini-2.0-flash.
- **User-Friendly Interface**: Built with Streamlit for an intuitive user experience.
- **Exportable Reports**: Download analysis results for future reference.

## 🚀 Installation
### Prerequisites
- Python 3.8+
- Git
- Virtual environment (recommended)

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Quyet160903/HireView-Analyzer-Expert.git
   cd HireView-Analyzer-Expert
   ```
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv  # Create a virtual environment
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up API keys**
   - Create a `.env` file in the project root and add your API keys:
     ```ini
     OPENAI_API_KEY=your_openai_api_key_here
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

## 🏃‍♂️ Usage
1. **Run the application**
   ```bash
   streamlit run main.py
   ```
2. **Upload your resume (PDF format)**
3. **Paste the job description**
4. **Select an AI model for analysis**
5. **Click 'Analyze Resume' to receive feedback**
6. **Download the analysis report if needed**

## 📂 Project Structure
```
HireView-Analyzer-Expert/
│── main.py                 # Streamlit UI
│── utils.py                # Helper functions and AI model integration
│── requirements.txt        # Required dependencies
│── .env                    # API keys (ignored in Git)
│── README.md               # Project documentation
```

## 🛠 Technologies Used
- **Python** (Backend Processing)
- **Streamlit** (Web Interface)
- **OpenAI API** (GPT-4o Analysis)
- **Google Generative AI API** (Gemini Analysis)
- **PyPDF2** (PDF Text Extraction)
- **Loguru** (Logging)

## 📌 Future Improvements
- Add support for additional file formats (e.g., DOCX, TXT)
- Enhance analysis with more AI models
- Improve UI with more customization options

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

## 📬 Contact
For questions or feedback, reach out to **[Your Contact Information]**.

