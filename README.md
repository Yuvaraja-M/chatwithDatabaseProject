# 🗃️ LangChain Chat with SQL Database

A powerful Streamlit web application that enables natural language conversations with SQL databases using LangChain and Azure OpenAI. Ask questions in plain English and get intelligent SQL queries executed automatically!

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![LangChain](https://img.shields.io/badge/langchain-latest-green.svg)

## ✨ Features

- 🤖 **Natural Language to SQL**: Ask questions in plain English
- 🗃️ **SQLite Integration**: Built-in support for SQLite databases
- 🔄 **Interactive Chat Interface**: Streamlit-powered conversational UI
- 🧠 **Smart Query Generation**: Powered by Azure OpenAI GPT models
- 📊 **Sample Database**: Includes a student database for testing
- 🛡️ **Secure Configuration**: Environment-based API key management

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatwithdbproject.git
cd chatwithdbproject
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv chatsqlenv

# Activate it
# On Windows:
chatsqlenv\Scripts\activate
# On macOS/Linux:
source chatsqlenv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r req.txt
```

### 4. Create Sample Database (Optional)

```bash
python createdb.py
```

This creates a `student.db` file with sample student data.

### 5. Configure Azure OpenAI

You have two options:

**Option A: Environment Variables (Recommended)**
```bash
# Create a .env file (not tracked by git)
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
OPENAI_API_VERSION=2025-01-01-preview
OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

**Option B: Streamlit Sidebar**
- Enter your Azure OpenAI credentials in the app's sidebar when running

### 6. Run the Application

```bash
streamlit run appp.py
```

The app will open in your browser at `http://localhost:8501`

## 💬 How to Use

1. **Select Database**: Choose "Use SQLite3 Database - student.db" from the sidebar
2. **Enter API Key**: If not using environment variables, enter your Azure OpenAI API key
3. **Start Chatting**: Ask questions about your data in natural language!

### Example Queries

```
"Show me all students"
"What's the average marks of students in class 10?"
"List students with marks greater than 90"
"How many students are in section A?"
"Who is the top performer in class 9?"
```

## 📁 Project Structure

```
chatwithdbproject/
├── appp.py              # Main Streamlit application
├── createdb.py          # Script to create sample student database
├── req.txt              # Python dependencies
├── student.db           # Sample SQLite database (created by createdb.py)
├── README.md            # This file
└── chatsqlenv/          # Virtual environment (not in git)
```

## 🛠️ Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **LangChain**: Framework for building AI applications
- **LangChain Community**: Additional LangChain tools and integrations
- **LangChain OpenAI**: OpenAI integration for LangChain
- **SQLAlchemy**: SQL toolkit and ORM

### Architecture

1. **Frontend**: Streamlit provides the web interface
2. **AI Agent**: LangChain creates an intelligent SQL agent
3. **Database**: SQLite database with student information
4. **LLM**: Azure OpenAI GPT models for natural language understanding

## 🔧 Configuration

### Azure OpenAI Setup

You'll need:
- Azure OpenAI API key
- Azure OpenAI endpoint URL
- Deployment name for your GPT model

### Database Schema

The sample `student.db` contains a `students` table:

| Column  | Type    | Description           |
|---------|---------|----------------------|
| id      | INTEGER | Primary key          |
| name    | TEXT    | Student name         |
| class   | TEXT    | Class/Grade          |
| section | TEXT    | Section (A, B, C)    |
| marks   | INTEGER | Student marks        |

## 🚨 Important Security Notes
 
⚠️ **API Key Security**: Never commit your actual API keys to version control. The current `appp.py` contains a hardcoded key that should be replaced with environment variables before pushing to GitHub.

**To secure your code:**
1. Remove the hardcoded API key from line 22 in `appp.py`
2. Use environment variables instead: `os.getenv("AZURE_OPENAI_API_KEY")`
3. Add `.env` to your `.gitignore` file

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the amazing AI framework
- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework
- [Azure OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service) for the powerful language models

**Made with ❤️ by Yuvaraja M**
