import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Arefin's Protfolio", page_icon="🗂️", layout="wide")

#this for the animation load
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coder = load_lottieurl("https://lottie.host/c42e7bb5-cd2a-4ccb-8142-83c1e0196cb4/ygGJHLVAl0.json")
lottie_contact = load_lottieurl("https://lottie.host/ad701a82-571f-45fd-8a50-572ad2ed2a41/FbERxWJDOM.json")

image1 = Image.open("image/project1.png")
image2 = Image.open("image/project2.png")
image3 = Image.open("image/project3.png")
image4 = Image.open("image/project4.png")
image5 = Image.open("image/project5.png")
#image6 = Image.open("iamge\project6.jpg")

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
        options = ["About", "Skills", "Projects", "Publication", "Contact"],
        icons = ['person', 'gear', 'code-slash', 'pencil-square', 'chat-left-text-fill'],
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
            - 🔬 Research Focus:
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
            with st.expander("🎓 Education", expanded=True):
                st.markdown("""
                **🏫 Harbin Institute of Technology, Shenzhen**  
                *2024 - Present*  
                🔹 **M.Sc Computer Science and Technology**  
                - Research: Computer Vision & NLP  
                - GPA: 3.4/4.0  
                - Advisor: Prof. Wen Jie  
                
                **📚 Southwest University of Science and Technology**  
                *2019 - 2023*  
                🔹 **B.Sc Computer Science and Technology**  
                - Thesis: Tansformer Based Graph Convolutional Networks for Skeleton-Based Action Recognition. 
                - Honors: Sichuan Government Scholarship  
                """)

        with col4:
            with st.expander("💼 Professional Experience", expanded=True):
                st.markdown("""
                **🔍 Research Assistant | Bio Computing Research Lab | HITSZ**  
                *2024 - Present*  
                - Developed assistive CV tools using:  
                🐍 Python | 🔍 PaddleOCR | 🗣️ Pyttsx3  
                - Achievements:  
                ✅ Improved text recognition accuracy by 32%  
                ✅ Reduced inference latency to <200ms    
                """)
                
                # Project chips
                st.markdown("**✨ Key Projects**")
                cols = st.columns(3)
                with cols[0]:
                    st.markdown("![CV](https://img.shields.io/badge/Computer-Vision-blue)")
                with cols[1]:
                    st.markdown("![NLP](https://img.shields.io/badge/NLP-Green)")
                with cols[2]:
                    st.markdown("![Accessibility](https://img.shields.io/badge/Accessibility-Important)")
                
                # Dynamic content
                if st.checkbox("Show publication details"):
                    st.markdown("""
                    **📜 Publications:**  
                    - *[Paper Title]*, IEEE CVPR 2024  
                    - *[Paper Title]*, ACM MM 2023  
                    """)

    st.write("---")       
    with st.chat_message("user"):
        st.write("🤖 **AI Internship Candidate Alert**")
        st.write("""
        I'm actively seeking roles where I can:
        - Build **transformative CV/NLP systems** 🧠
        - Optimize **real-world AI deployments** ⚡
        - Contribute to **global AI innovation** 🌍
        """)
        if st.toggle("Show contact preference"):
            st.info("""
            **Availability**: Summer 2025  
            **Location**: Shenzhen/Remote  
            **Contact**: arefin.swust@gmail.com
            """)

# for the skill part

if selected == "Skills":
    with st.container():
        st.header("🛠️ Technical Skills", divider="rainbow")
        col5, col6 = st.columns(2)
    
    with col5:
        st.subheader("</> Programming")
        st.markdown("""
        - **Python** (Advanced)
          - TensorFlow, PyTorch, OpenCV
          - Pandas, NumPy, Scikit-learn
        - **C/C++** (Intermediate)
          - System programming
          - Algorithm optimization
        """)
        
        st.subheader("🧰 Tools")
        st.markdown("""
        - NVIDIA CUDA, Jupyter Notebooks, Google Colab 
        - Git, Github 
        - Streamlit
        """)

    with col6:
        st.subheader("⚡AI/ML Specialization")
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
        
        st.subheader("🗣️Languages")
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
        st.header("🌟 My Projects", divider="rainbow")
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

if selected == "Publications":
    with st.container():
        st.header("📚 Publications", divider="rainbow")
        col5, col6 = st.columns(2)
    
        with col5:
            st.subheader("📊 Conference Proceedings")
            st.markdown("""
            - **ML-MT: A Study of e-Health Application Framework by Machine Learning Techniques**  
              *Publisher:  2022 IEEE 4th International Conference on Cybernetics, Cognition and Machine Learning Applications (ICCCMLA)*
              - This research paper aims to increase efficiency by providing an easy-to-use platform that not only works as a bridge between the doctors and the patients but also expedites the diagnosis process with the assistance of machine learning.  
              - The proposed framework is composed of mainly two core components which are the patient management system and the doctor management system.
              - The patient management system allows patients to request an appointment, collects and monitors patient data, and predicts the chances of the patient having heart disease, kidney disease, liver disease, cancer, and diabetes. 
            - [Poster](https://ieeexplore.ieee.org/document/9989049)
            """)

        with col6:
            st.subheader("📚 Theses")
            st.markdown("""
            - **B.Sc. Thesis**  
              *Tansformer Based Graph Convolutional Networks for Skeleton-Based Action Recognition.*  
              - Advisor: Prof. He Gang 
              - SWUST Library, 2023  
              [View Abstract](your-link-here)
            """)

if selected == "Contact":
    with st.container():
        st.header("📬 Let's Connect!", divider="rainbow")
        
        # Contact cards with icons
        cols = st.columns(3)
        with cols[0]:
            st.markdown("""
            ### 📧 Email
            **Professional:**  
            [arefin.swust@gmail.com](mailto:arefin.swust@gmail.com)  
            
            **Academic:**  
            [arefin@stu.hit.edu.cn](mailto:arefin@stu.hit.edu.cn)
            """)
            
        with cols[1]:
            st.markdown("""
            ### 🔗 Professional
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](http://www.linkedin.com/in/nazmul-arefin)
            
            [![Google Scholar](https://img.shields.io/badge/Google_Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white)](your-google-scholar-url)
            """)
            
        with cols[2]:
            st.markdown("""
            ### 💻 Coding
            [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nazmul-Arefin)
            
            [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](your-kaggle-url)
            """)
        
        # Interactive map
        st.subheader("📍 Find Me")
        with st.expander("Open Map"):
            st.markdown("""
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3691.689487092637!2d113.9663683153551!3d22.58123494832035!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3403f8d5a5d5d5d5%3A0x5e6a01a1bcbe7f47!2sHarbin%20Institute%20of%20Technology%2C%20Shenzhen!5e0!3m2!1sen!2sus!4v1620000000000!5m2!1sen!2sus" 
            width="100%" height="300" style="border:0; border-radius:8px;" allowfullscreen loading="lazy"></iframe>
            """, unsafe_allow_html=True)
        
        
        # Social media carousel
        st.subheader("🌍 Social Media")
        platforms = {
            "Facebook": "https://twitter.com/yourhandle",
            "Instagram": "https://instagram.com/yourhandle",
            #"WeChat": "wechat-qr-code.jpg"
        }
        
        selected_platform = st.selectbox("Choose platform:", list(platforms.keys()))
        if "WeChat" in selected_platform:
            st.image(platforms[selected_platform], width=150)
        else:
            st.markdown(f"[Open {selected_platform}]({platforms[selected_platform]})")
