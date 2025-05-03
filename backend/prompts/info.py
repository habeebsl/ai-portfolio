chattersort_project =  \
"""
Chattersort is an extension-based web app that helps users organize and manage their AI chatbot conversations (e.g., ChatGPT, Gemini, and Claude). Its features include:  
- Sorting conversations at the click of a button.  
- Note creation directly within the chatbot interface.  
- Prompt storage for quick reuse.  
- Full chat history organization.  

I’m working on this project alongside three colleagues. My role involves building the backend system, developing the Chrome extension, and implementing the API linking the frontend and backend.  
The backend is built using Django and Python, while the API is implemented with Django Rest Framework (DRF). The Chrome extension is primarily developed with JavaScript, seamlessly integrating with the web app.

- Achievements: Within 10 days of launching our landing page, we gained 40+ superusers, with 10 acquired through my outreach efforts.  
- Outcome: This project highlights my teamwork, problem-solving abilities, and marketing skills.  

Landing Page: https://www.chattersort.com/ 
GitHub: (Code available upon request) 
"""

keypoint_project = \
"""
Keypoint:
Keypoint is a web app that extracts and highlights the most critical information from a text. It identifies key sentences, paragraphs, and terms, and provides Wikipedia-based tooltips for important words, allowing users to access more information instantly. The app also includes a redirect link to the relevant Wikipedia page for further exploration.  

This project was built using Python, Django, HTML, CSS, and JavaScript, leveraging Google’s Gemini-1.5-Pro model for its cutting-edge NLP capabilities. I also used PostgreSQL for session-based storage.  

I created Keypoint as a productivity tool for students, researchers, and professionals who need to quickly extract insights from dense texts. Its utility lies in helping users absorb information efficiently without reading through the entire document.  

- Challenges: Determining which parts of the text to highlight required extensive trial and error to balance contextual accuracy and user expectations.  
- Outcome: This tool is particularly useful for researchers managing large volumes of information.  

Website: https://keypoint-coral.vercel.app/  
GitHub: https://github.com/habeebsl/keypoint
Demo Video: https://drive.google.com/file/d/1qWoG1yyhYIEKWkIdAHjFYKooixFEyzP4/preview
"""

therapist_project = \
"""
AI Therapist:
This is one of my favorite projects—a web-based AI therapist built around Cognitive Behavioral Therapy (CBT) principles. The app mimics a real therapy session by engaging users through the three key stages of CBT: initial, middle, and final. Each stage is tailored with handcrafted prompts designed to address specific therapeutic goals.  

The app was built using Python, Flask, HTML, CSS, and JavaScript, with Redis for managing chat session storage. I chose Mistral AI's mistral-large-2411 model for its advanced capabilities, ensuring an empathetic and effective user experience.  

I created this project to provide an affordable alternative to therapy for individuals struggling with psychological conditions but unable to access professional help. Building it required extensive research and prompt engineering to ensure conversations felt natural and meaningful.  

- Challenges: The hardest part of this project was crafting prompts that effectively simulated a therapist’s responses while keeping sessions coherent and productive.  
- Outcome: This project showcases my ability to combine AI expertise with real-world problem-solving.  

Website: https://ai-therapist-rho.vercel.app/ 
GitHub: https://github.com/habeebsl/ai-therapist
Demo Video: https://drive.google.com/file/d/1jtoB3mc04WJb-5uFgAFGu3TPy0dHz618/preview
"""

translator_project = \
"""
AI Translator:
This is my latest project, offering multilingual real-time transcription of audio data, as well as real-time translation into multiple languages. Additionally, users can play back the translated text in a natural and intuitive human-like voice.

The project is built using HTML, CSS, JavaScript, TypeScript, Vue, Pinia, and FastAPI. It leverages:

- OpenAI's Whisper-1 model for audio transcription
- OpenAI's TTS-1 model for generating speech from translated text
- GPT-4o Mini for verifying transcribed text
- DeepL for text translation

Website: https://ai-translator-beryl.vercel.app/
Github: https://github.com/habeebsl/ai-translator
Demo Video: https://www.loom.com/embed/ab7bb5645b234762b2abd23d1cb12c6b?sid=dee405ab-fa36-4bec-bdc2-575a5df74aa4
"""

activity_builder_project = \
"""
Interactive Math Learning Game (Built for a hiring challenge, completed in 2 weeks)
A web-based educational game that teaches addition through visual intuition for younger learners. It features a balance scale mechanic, where students match numbers to a target sum. If their answer is close but incorrect, the scale tilts to indicate whether the sum is too large or too small. Teachers can create and structure activities by defining custom problems, adding hints, and controlling problem order.

This project was built using HTML, CSS, TailwindCSS, JavaScript, Typescript, Matter.js, Vue, FastAPI (including Pydantic, SQLAlchemy), Pytest, Firebase (For Authentication), Pinia (State Management), MySQL, Railway, Vercel, Docker

Website: https://balance-scale-activity.vercel.app/ 
GitHub: https://github.com/habeebsl/Balance-Scale-Activity/
Demo Video: https://drive.google.com/file/d/1yltd1TW-TTagoBW8HNnLlyoYeLsoQUXD/

Challenges & Solutions: I documented key challenges and how I solved them here - https://github.com/habeebsl/Balance-Scale-Activity/blob/main/LEARNING.md
Outcome: The company recognized my implementation and effort, leading to a referral at a startup. More details available on request.
"""

documents = {
    "personal_info": "**Personal Info**\nMy name is Habeeb Salami, and I am an web developer with AI expertise with over 2 years of experience, based in Edo State, Nigeria. I specialize in building innovative projects and have a keen interest in AI. I enjoy solving complex problems and integrating AI into products to foster groundbreaking innovation. My future goals include leveraging AI to boost client product traction and creating transformative solutions that redefine industries.",

    "technical_skills": "**Skills**\nC, Python, JavaScript, Typescript, SQL, HTML, CSS, Node.js, Express.js, Vue.js, React.js, Matter.js, Pinia, Vite, TailwindCSS, Flask, Django, FastAPI, SQLAlchemy, Pytest, Postman, Redis, PostgreSQL, MySQL, SQLite, Docker, AWS, Pinecone, RAG, Langchain, FAISS, HayStack, Render, Vercel, Heroku, Tembo, Supabase, Railway, Firebase, Git, GitHub, Gemini, GPT-4, Mistral, Prompt Engineering, Robotic Process Automation, Web Scraping, Backend Development",

    "ai_therapist": therapist_project,

    "keypoint": keypoint_project,

    "chattersort": chattersort_project,
    
    "activity_builder": activity_builder_project,

    "ai_translator": translator_project,

    "projects": f"**Projects**\n{keypoint_project}\n\n{chattersort_project}\n\n{therapist_project}\n\n{activity_builder_project}\n\n{translator_project}",

    "education": """
    **Education**
    - Degree: Bachelor of Medicine and Surgery  
    - Institution: Igbinedion University Okada, Nigeria  
    - Duration: 2021–2027  
    """,

    "work_experience": """
    **Work Experience**
    1. Comini Learning 
    - Role: Software Developer Intern 
    - Achievements: Building Interesting games to make learning more interactive and fun for children 
    - Duration: 2025–present  

    2. Chattersort
    - Role: Backend Developer, Prompt Engineer, Chrome Extension Developer  
    - Achievements: Secured 10+ power users by implementing innovative AI solutions.  
    - Duration: 2023–2024 

    2. Google Developer Student Club  
    - Role: Python Instructor  
    - Achievements: Trained over 20 students in Python, enabling them to start careers in web development.  
    - Duration: 2022–2023  
    """, 
    "contact": """
    **Contact**
    - Email: habeebsalami09@gmail.com  
    - Phone: +234 9064561437  

    Quick Links:
    - LinkedIn: https://www.linkedin.com/in/habeeb-salami-688870290/ 
    - X (formerly Twitter): https://x.com/habeebslm
    - GitHub: https://github.com/habeebsl
    """
}


