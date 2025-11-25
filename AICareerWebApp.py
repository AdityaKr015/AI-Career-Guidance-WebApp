#The AI Career Guidance Web Application

# Import important libraries
import streamlit as st
import google.generativeai as genai
import my_secrets

# Configure the Generative AI model
genai.configure(api_key=my_secrets.API_KEY)
model = genai.GenerativeModel("gemini-2.5-pro")

# Streamlit App Configuration
st.set_page_config(
    page_title="AI Career Guidance",
    layout="centered",
    page_icon="🎓",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container styling - dark blue-black gradient */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        padding: 2rem;
    }
    
    /* Card-like container for form - white with blue accents */
    .stForm {
        background: white;
        padding: 2.5rem;
        border-radius: 24px;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(59, 130, 246, 0.1);
    }
    
    /* Title styling - white with blue glow */
    h1 {
        color: white !important;
        text-align: center;
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 0 0 30px rgba(59, 130, 246, 0.5), 0 0 60px rgba(59, 130, 246, 0.3);
        letter-spacing: -1px;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: #e0e7ff;
        text-align: center;
        font-size: 1.25rem;
        margin-bottom: 2.5rem;
        font-weight: 500;
    }
    
    /* Input labels - dark blue-black */
    label {
        font-weight: 600 !important;
        color: #1e293b !important;
        font-size: 1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Text inputs and textareas - white with blue focus */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        border-radius: 12px !important;
        border: 2px solid #e2e8f0 !important;
        padding: 0.875rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        background: white !important;
        color: #1e293b !important;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus, .stSelectbox select:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
        outline: none !important;
    }
    
    /* Submit button - blue gradient */
    .stFormSubmitButton button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        padding: 1rem 2rem !important;
        border-radius: 14px !important;
        border: none !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        margin-top: 1.5rem !important;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
    }
    
    .stFormSubmitButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4) !important;
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%) !important;
    }
    
    /* Download button - white with blue border */
    .stDownloadButton button {
        background: white !important;
        color: #3b82f6 !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 0.75rem 1.5rem !important;
        border: 2px solid #3b82f6 !important;
        transition: all 0.3s ease !important;
    }
    
    .stDownloadButton button:hover {
        background: #3b82f6 !important;
        color: white !important;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3) !important;
    }
    
    /* Success message - blue theme */
    .stSuccess {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%) !important;
        color: #1e40af !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-weight: 600 !important;
        border-left: 4px solid #3b82f6 !important;
    }
    
    /* Error message */
    .stError {
        background: #fee2e2 !important;
        color: #991b1b !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border-left: 4px solid #ef4444 !important;
    }
    
    /* Response card - white with blue border */
    .response-card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        margin-top: 2rem;
        border: 2px solid #3b82f6;
    }
    
    /* Icon styling */
    .icon {
        font-size: 4rem;
        text-align: center;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 20px rgba(59, 130, 246, 0.5));
    }
    
    /* Spinner customization - blue */
    .stSpinner > div {
        border-top-color: #3b82f6 !important;
    }
    
    /* Feature cards - white with blue accents */
    .feature-card {
        background: white;
        padding: 1.75rem;
        border-radius: 18px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        border: 2px solid rgba(59, 130, 246, 0.2);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.3);
        border-color: #3b82f6;
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
    }
    
    .feature-title {
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    
    .feature-text {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.5;
    }
    
    /* Section headers in form */
    h3 {
        color: #1e293b !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 0.75rem !important;
        border-bottom: 3px solid #3b82f6 !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: #f1f5f9 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        color: #1e293b !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main App Content
st.markdown('<div class="icon">🎓✨</div>', unsafe_allow_html=True)
st.title("AI Career Guidance")
st.markdown('<p class="subtitle">Get personalized career suggestions based on your interests and skills!</p>', unsafe_allow_html=True)

# Feature Highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Personalized</div>
            <div class="feature-text">Tailored guidance just for you</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered</div>
            <div class="feature-text">Advanced AI analysis</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Data-Driven</div>
            <div class="feature-text">Based on your profile</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Career Guidance Form
with st.form("career_form"):
    st.markdown("### 📝 Tell Us About Yourself")
    
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("👤 Your Name", placeholder="Enter your full name")
    
    with col2:
        grade = st.selectbox(
            "🎓 Your Current Class/Grade",
            ["10th", "11th", "12th", "Undergraduate", "Postgraduate", "Other"]
        )
    
    subjects = st.text_area(
        "📚 Subjects and Marks",
        placeholder="e.g., Math: 90, Physics: 85, Chemistry: 88 or CGPA: 8.5",
        height=100
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        interests = st.text_area(
            "❤️ Your Interests",
            placeholder="e.g., coding, biology, design, public speaking, traveling",
            height=120
        )
    
    with col2:
        skills = st.text_area(
            "💪 Your Skills",
            placeholder="e.g., Python, drawing, teamwork, leadership",
            height=120
        )
    
    col1, col2 = st.columns(2)
    
    with col1:
        personality = st.text_area(
            "🧠 Personality Traits",
            placeholder="e.g., Introvert, Extrovert, Analytical",
            height=100
        )
    
    with col2:
        goals = st.text_area(
            "🎯 Career Goals (Optional)",
            placeholder="e.g., Want to become a software engineer",
            height=100
        )
    
    submit = st.form_submit_button("🚀 Get My Career Guidance")

# Prompt Generation and AI Interaction
if submit:
    if not name or not subjects or not interests or not skills:
        st.error("⚠️ Please fill in all required fields (Name, Subjects, Interests, and Skills)")
    else:
        with st.spinner("🧠 Analyzing your profile and generating personalized guidance... 🚀"):
            prompt = f"""
            You are an expert career counselor.

            Important Instructions:
            - First, check if the input has any Hindi words (like 'padhna', 'daudana', 'khelna') written in Roman script.
            - Even if English proportion is high, but any Hindi words exist, TREAT the whole input as Hinglish.
            - Hinglish means replying in a natural mix of Hindi and English, using Roman script (not Devanagari).
            - If 100% English input, reply in English.
            - If 100% Hindi in Devanagari script, reply in Hindi.
            - Do NOT change the user's original language feel.

            Student Profile:
            Name: {name}
            Class: {grade}
            Subjects and Marks: {subjects}
            Interests: {interests}
            Skills: {skills}
            Personality: {personality}
            Career Goals: {goals}

            Response Instructions:
            - Suggest Top 5 career paths.
            - Recommend suitable stream.
            - Suggest important skills to develop.
            - Give future opportunities.
            - Keep tone sweet, motivating and friendly.
            - Use natural Hinglish phrasing if Hinglish detected (example: "tumhe coding aur design me career banana chahiye").
            - Give a confidence percentage (0-100%) for each recommended career based on user's interests and skills.

            WARNING: 
            - Use English only when script is in English
            - NO Devanagari script allowed in Hinglish case.
            - NO pure English allowed in Hinglish case.
            - Use easy friendly Hinglish words throughout.
            - Strictly obey these language rules, no matter what.

            Start responding now.
            """

            try:
                response = model.generate_content(prompt)
                
                st.success("✨ Here's your personalized career guidance!")
                
                st.markdown(response.text)
                
                #Download Butoon
                st.markdown("<br>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.download_button(
                        label="📥 Download Career Guidance",
                        data=response.text,
                        file_name=f"career_guidance_{name.replace(' ', '_')}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )

            except Exception as e:
                st.error("❌ Something went wrong while generating guidance. Please check your API key or try again later.")
                with st.expander("View Error Details"):
                    st.exception(e)

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; color: #e0e7ff; padding: 1rem;'>
        <p style='margin: 0; font-weight: 600; font-size: 1.1rem;'>💡 Powered by AI | Made By Paradox with ❤️ for Students</p>
        <p style='margin: 0.5rem 0 0 0; font-size: 0.95rem; opacity: 0.9;'>Your future starts here! 🌟</p>
    </div>
""", unsafe_allow_html=True)

# If it doesn't run and gives MainThread missing errors then, run this in terminal -> "streamlit run FILE_NAME.py"

