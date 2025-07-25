import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")

#this for the animation load
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coder = load_lottieurl("https://lottie.host/c42e7bb5-cd2a-4ccb-8142-83c1e0196cb4/ygGJHLVAl0.json")
lottie_contact = load_lottieurl("https://lottie.host/ad701a82-571f-45fd-8a50-572ad2ed2a41/FbERxWJDOM.json")

image1 = Image.open("image\project1.png")
image2 = Image.open("image\project2.png")
image3 = Image.open("image\project3.png")
image4 = Image.open("image\project4.png")
image5 = Image.open("image\project5.png")

# Intro page
st.write("##")
st.subheader("Hey guys :wave:")
st.title("My Portfolio Website")
st.write(
    """
    🚀 Welcome to My Digital Hub!

    Hi, I’m Nazmul Arefin, an AI enthusiastic, passionate about turning ideas into impactful solutions. Here, you’ll find my projects, skills, and creative experiments—each crafted with code, curiosity, and a dash of coffee. ☕
    """)
st.write("Let’s connect and create something remarkable!")
st.write("[LinkedIn](http://www.linkedin.com/in/nazmul-arefin)",   "[Github](https://github.com/Nazmul-Arefin)")
st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ["About", "Skills", "Projects", "Contact"],
        icons = ['person', 'gear', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.title("I am Nazmul Arefin")
            st.subheader("Sloving Real-World Problems " \
            "with 🧑‍💻 Code, 👁️ Vision, and 🧠 Intelligence")
            st.markdown("""
            - I am studying Computer Sciece and Technology at Harbin Institute of Technology, Shenzhen, China. 
            - HITSZ is a premier research institution in the Greater Bay Area, HITsz provides cutting-edge labs and industry partnerships that fuel my work in intelligent systems.
            - 🔬 Research Focus
                - Computer Vision: Developing an OCR to Speech system to aid visually impaired users and support educational accessibility.
                - NLP: Convert static images to enable real-time text-to-speech conversion.
            """)
        with col2:
            st.write("##")
            st_lottie(lottie_coder, height=400, width=500,)

    st.write("---")  

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            🏫Education
            - Harbin Institute of Technolgy, Shenzhen, China
                - Masters of Computer Science and Technolgy
                - Research Field: Computer Vision, Natural Language Processing
            - Southwest University of Science and Technology, Sichuan, China
                - Bachelor of Computer Science and Technology
            """)
        with col4:
            st.subheader("""
            🧩Experience
            - Research Assistant
                - Researched computer vision applications for assistive technology, developing Python-based solutions with PaddleOCR and Pyttsx3 to enhance accessibility tools for visually impaired users.
    
            """)

    st.write("---")       
    st.write("👉Seeking an internship opportunity to apply and expand my knowledge in Artificial Intelligence, while " \
            "contributing to the development of cutting-edge AI technologies in a global innivation-driven environments.") 

# for the skill part

if selected == "Skills":
    with st.container():
        st.header("🛠️ Technical Skills")
        col5, col6 = st.columns(2)
    
    with col5:
        st.subheader("Programming")
        st.markdown("""
        - **Python** (Advanced)
          - TensorFlow, PyTorch, OpenCV
          - Pandas, NumPy, Scikit-learn
        - **C/C++** (Intermediate)
          - System programming
          - Algorithm optimization
        """)
        
        st.subheader("Tools")
        st.markdown("""
        - NVIDIA CUDA, Jupyter Notebooks, Google Colab 
        - Git, Github 
        - Streamlit
        """)

    with col6:
        st.subheader("AI/ML Specialization")
        st.markdown("""
        - **Computer Vision**
          - Library: OpenCV, PaddleOCR
          - Image Classification
        - **Natural Language Processing**
          - LangChain, OpenAI API, RAG 
          - Prompt Engineering
          - BERT, GPT fine-tuning
        - **Model Deployment**
          - FastAPI
          - Flask
        """)
        
        st.subheader("Languages")
        st.markdown("""
        - English (Full Professional Proficiency)
        - Chinese (HSK-3)
        - Bangle (Native)
        """)

    # Optional: Add progress bars for visual impact
    with st.expander("📊 Skill Proficiency Metrics"):
        st.subheader("🚀 Skill Proficiency", divider="rainbow")

        skills = {
            "Python": 90,
            "TensorFlow/PyTorch": 85,
            "Computer Vision": 88,
            "Natural language Processing": 80
        }

        for skill, percent in skills.items():
            st.write(f"**{skill}**")
            st.progress(percent, text=f"{percent}%")
            st.write("")  # Add small space between skills

# for the Project Part  
if selected == "Projects":
    with st.container():
        st.header("🌟 My Projects")
        st.write("---")
        col7, col8 = st.columns((1,2))
        with col7:
            st.image(image1, width=250)      
        with col8:
            st.subheader("Vision-Speak: Real-time OCR and TTS")
            st.write("🐍 Python 🔍 PaddleOCR 🗣️ Pyttsx3")
            st.write("""
            - Developed an OCR-to-speech system using PaddleOCR and pyttsx3 to convert book page images into natural sounding audio. 
            - Trained a DB Ner for text detection and SVTR for recognition model on the Total Text dataset for accurate English text extraction. 
            - Designed a pipeline for processing static images to enable real-time text-to-speech conversion. 
            = Built a practical tool to aid visually impaired users and support educational accessibility through audio rendering of printed content. 
            """)
            st.markdown("[Visit Github Repo](https://github.com/Nazmul-Arefin/vision-speak)")
        st.write("---")

        col9, col10 = st.columns((1,2))
        with col9:
            st.image(image2, width=250)      
        with col10:
            st.subheader("Image Classifier (Streamlit Deployment)")
            st.write("🐍 Python 👁️ OpenCV 📊 TensorFlow")
            st.write("""
            - Built a CNN-based classifier (ResNet50) to analyze and predict any image class with high accuracy.  
            - Deployed the classifier as an interactive web application using Streamlit, enabling real-time image uploads and predictions with optimized inference speed. 
            """)
            st.markdown("[Visit Github Repo](https://github.com/Nazmul-Arefin/Image-Classifier)")
        st.write("---")

        col9, col10 = st.columns((1,2))
        with col9:
            st.image(image3, width=250)      
        with col10:
            st.subheader("Resume Critiquer (GPT-Powered)")
            st.write("🐍 Python 🧠 OpenAI 🛠️ Streamlit")
            st.write("""
            - Developed a web app (Streamlit) analyzing PDF/DOCX resumes using GPT-4, providing actionable feedback (e.g., ATS optimization, skill gaps).
            - Key Achievement: Cut average resume review time from 30 mins to 2 mins per user.
            """)
            st.markdown("[Visit Github Repo](https://github.com/Nazmul-Arefin/Resume-Critiquer)")
        st.write("---")

        col9, col10 = st.columns((1,2))
        with col9:
            st.image(image4, width=250)      
        with col10:
            st.subheader("AI Agent with Tool Integration")
            st.write("🐍 Python 🔗 LangChain 🧠 OpenAI")
            st.write("""
            - Built a rule-based AI assistant using LangChain and OpenAI API that answers questions and performs basic tasks like math calculations.  
            - Designed a pipeline for tool integration, allowing seamless switching between tasks like computations and conversational responses. 
            - Implemented error handling to manage invalid inputs and improving reliability.
            """)
            st.markdown("[Visit Github Repo](https://github.com/Nazmul-Arefin/AI-Agent)")
        st.write("---")

        col9, col10 = st.columns((1,2))
        with col9:
            st.image(image5, width=250)      
        with col10:
            st.subheader("IMDB Sentiment Classification (LSTM)")
            st.write("🐍 Python 🔥 PyTorch")
            st.write("""
            - Trained an LSTM model on 50K IMDB reviews, achieving 89% accuracy via hyperparameter tuning (dropout, learning rate scheduling). 
            - Implemented text preprocessing (tokenization, padding) and embedding layers (GloVe) to handle variable-length sequences. 
            """)
            st.markdown("[Visit Github Repo](https://github.com/Nazmul-Arefin/IMDB-Sentiment-Classification)")
        st.write("---")

if selected == "Contact":
    st.header("📬 Get in Touch!")
    
    
    left_col, right_col = st.columns((2, 1))
    with left_col:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name*", placeholder="Your name")
            email = st.text_input("Email*", placeholder="your@email.com")
            message = st.text_area("Message*", placeholder="Your message...", height=150)
        
            # FormSubmit.co integration
            st.markdown("""
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_next" value="https://yourportfolio.streamlit.app/Thank_You">
            """, unsafe_allow_html=True)
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                # Process form data (example using FormSubmit.co)
                form_data = {
                    "name": name,
                    "email": email,
                    "message": message
                }
                
                try:
                    response = requests.post(
                        "https://formsubmit.co/ajax/arefin.swust@gmail.com", 
                        json=form_data
                    )
                    st.success("Message sent successfully!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")

    with right_col:
        st_lottie(lottie_contact, height=500)

    st.write("---")
    st.markdown("""
    <p style='text-align: center;'>
        @ 2025 Personal Portfolio | 📧 arefin.swust@gmail.com | 🏠 Shenzhen, Guangdong, China
    </p>
    """, unsafe_allow_html=True)