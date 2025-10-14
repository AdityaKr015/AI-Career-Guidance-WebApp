We the Team Paradox made this project for  3-day national-level hackathon organized by Gateway Education in collaboration with ImaginXP (CollegeDekho Group)

🎓 AI Career Guidance Web App

An AI powered career guidance webapp built with Streamlit and Google Gemini API, designed to help students discover their ideal career paths based on their skills, interests, and personality.

✨ The app analyzes user inputs using Gemini 2.5 Pro and provides personalized recommendations with confidence levels, suggested skills, and future opportunities — in English or Hinglish, depending on input.

🚀 Features

✅ Personalized Career Recommendations
Tailored suggestions based on your strengths, interests, and personality.

🤖 AI-Powered Insights
Uses Google Gemini for career prediction.

📊 Data-Driven Guidance
Considers subjects, marks, and skills for accurate recommendations.

🎨 Modern UI Design
Sleek gradient interface, glassy cards, and intuitive layout built with Streamlit and custom CSS.

🗣️ Multilingual Mode
Automatically detects if user input is in English, Hinglish, or Hindi, and replies accordingly.

📥 Download Option
Export your personalized guidance as a .txt file.

🧠 Tech Stack
Frontend/UI:	Streamlit + Custom CSS
Backend (AI):	Google Generative AI (Gemini 2.5 Pro)
Language:	Python 3.x
Frameworks:	Streamlit

API Integration by google-generativeai library
Environment Variables	my_secrets.py for secure API key storage

⚙️ Installation & Setup

1️⃣ Clone this repository

git clone https://github.com/yourusername/ai-career-guidance.git

cd ai-career-guidance

2️⃣ Create a virtual environment (recommended)

python -m venv venv

venv\Scripts\activate   # On Windows

source venv/bin/activate   # On Mac/Linux


3️⃣ Install dependencies

pip install streamlit google-generativeai

4️⃣ Create a my_secrets.py file in the same directory

my_secrets.py

API_KEY = "YOUR_GEMINI_API_KEY_HERE"

💡 Get your API key from [Google AI Studio](https://aistudio.google.com/prompts/new_chat)

5️⃣ Run the app

streamlit run filename.py

🖼️ Preview

💻 Main Interface


A modern, gradient-themed dashboard with input form and AI result cards.

<img width="1276" height="627" alt="image" src="https://github.com/user-attachments/assets/64075777-0faf-4a4c-a1d8-1f87bf0f9046" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/9fb0921b-4f4e-46af-9fe8-6dfce538daa0" />



🧩 How It Works

User fills the form with details like subjects, skills, interests, and goals.

App sends data to Gemini AI by prompt engineering.

Gemini processes the profile and returns:

🎯 Top 5 career paths

📚 Suggested stream

🧰 Skills to develop

🌐 Future opportunities

📈 Confidence percentage for each path

Result is displayed beautifully in-app and can be downloaded.

🧑‍💻 Developer Info

👨‍🎓 Developed by: Paradox

💡 Purpose: To help students to make informed, AI-backed career decisions.

❤️ Made with: Python, Streamlit, and Google Gemini API.

📜 License

This project is licensed under the MIT License — you’re free to modify and use it with attribution.

🌟 Support

If you like this project:

⭐ Star the repo on GitHub

🐛 Report bugs or suggest improvements via Issues

💬 Share it with your college friends or hackathon teammates!
