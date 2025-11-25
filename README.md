## 🎓 **AI Career Guidance Web App**

## 🚀 Live Demo (Streamlit)

Try the deployed app here:  
[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-ff416c?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-career-guidance-byparadox.streamlit.app/)


- We the Team Paradox made this project for  3-day national-level hackathon organized by Gateway Education in collaboration with ImaginXP (CollegeDekho Group)


An AI powered career guidance webapp built with Streamlit and Google Gemini API, designed to help students discover their ideal career paths based on their skills, interests, and personality.

✨Our App analyzes user inputs using Gemini 2.5 Pro and provides personalized recommendations with confidence levels, suggested skills, and future opportunities — in English or Hinglish, depending on input.

## 🚀 Features

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

## 🧠 Tech Stack

Frontend/UI:	Streamlit + Custom CSS

Backend (AI):	Google Generative AI (Gemini 2.5 Pro)

Language:	Python 3.x

Frameworks:	Streamlit

API Integration by google-generativeai library

Environment Variables	my_secrets.py for secure API key storage

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository

git clone https://github.com/yourusername/ai-career-guidance.git

cd ai-career-guidance

### 2️⃣ Create a virtual environment (recommended)

python -m venv venv

venv\Scripts\activate   # On Windows

source venv/bin/activate   # On Mac/Linux


### 3️⃣ Install dependencies

pip install streamlit google-generativeai

### 4️⃣ Create a my_secrets.py file in the same directory

my_secrets.py

API_KEY = "YOUR_GEMINI_API_KEY_HERE"

💡 Get your API key from [Google AI Studio](https://aistudio.google.com/prompts/new_chat)

### 5️⃣ Run the app

streamlit run filename.py

## 🖼️ Preview

### 💻 Main Interface


A modern, gradient-themed dashboard with input form and AI result cards.

<img width="1276" height="627" alt="image" src="https://github.com/user-attachments/assets/64075777-0faf-4a4c-a1d8-1f87bf0f9046" />
<img width="1189" height="716" alt="image" src="https://github.com/user-attachments/assets/c324a8e0-3902-4be9-b022-ea840270d0c9" />

## Results
<img width="585" height="619" alt="image" src="https://github.com/user-attachments/assets/526bc4fd-c370-4812-8f55-408a06d200a6" />
<img width="586" height="581" alt="image" src="https://github.com/user-attachments/assets/5295bf34-e823-4a9d-b35e-8d7cb69e82a8" />
<img width="655" height="726" alt="image" src="https://github.com/user-attachments/assets/53e89ff4-4d66-4eb3-8b3f-83731bf6a6a3" />



## 🧩 How It Works

User fills the form with details like subjects, skills, interests, and goals.

App sends data to Gemini AI by prompt engineering.

Gemini processes the profile and returns:

🎯 Top 5 career paths

📚 Suggested stream

🧰 Skills to develop

🌐 Future opportunities

📈 Confidence percentage for each path

Result is displayed beautifully in-app and can be downloaded.

## 🧑‍💻 Developer Info:-

👨‍🎓 Developed by: Paradox

💡 Purpose: To help students to make informed, AI-backed career decisions.

❤️ Made with: Python, Streamlit, and Google Gemini API.

## 📜 License

This project is licensed under the MIT License — you’re free to modify and use it with attribution.

## Contributors

[Me](https://github.com/AdityaKr015)

[Vaibhav](https://github.com/vaibhav410)

## 🌟 Support

If you like this project:

⭐ Star the repo on GitHub

🐛 Report bugs or suggest improvements via Issues

💬 Share it with your college friends or hackathon teammates!
