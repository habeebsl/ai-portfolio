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

avox_project = \
"""
Avox AI:
Avox AI solves the challenge of creating culturally relevant advertisements for different markets worldwide. Generic ads often fail to connect with local audiences, but Avox automatically generates culturally-aware audio advertisements tailored to specific locations.

The project features a Cultural Intelligence Engine that analyzes local music, movie preferences, trends, weather, and regional slang using Qloo's Taste API and Google Trends. It includes advanced voice cloning capabilities where users can clone their voice in any language or let AI choose the perfect culturally-fit voice. The system provides complete audio production, generating scripts, background music, and broadcast-ready audio ads with real-time generation via WebSocket streaming.

Technical Innovation includes a multi-source intelligence pipeline combining cultural data, trends, and weather conditions, ElevenLabs voice cloning with Redis-backed slot management system, AI-driven content generation with specialized cultural prompts, and MusicGen for contextually appropriate background music.

The tech stack includes Python, FastAPI, React, TypeScript, Redis, ElevenLabs API, OpenAI GPT-4, Qloo Taste API, Google Trends API, Serper API, Weather API, and MusicGen.

Impact: Brands can create dozens of localized ad variants in minutes instead of weeks, ensuring authentic resonance with each target market while maintaining their core brand identity.

Website: https://avox-sepia.vercel.app
GitHub: https://github.com/habeebsl/Avox
Demo Video: https://www.youtube.com/embed/Xde9mr1_Kxo
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

marketer_project = \
"""
Email Marketing Automation Tool:
There where a variety of algorithms to choose from, including the UCB and Epsilon-greedy algorithms. They were also good options but they had some randomizing factor to them, which hinders the self-learning algorithm’s progression and balance between exploration & exploitation.

The Thompson Sampling algorithm perfectly balances these aspects, and it’s design allows the model to get better in the long run , hence why I selected it.

My Solution: The model selects the email template to send as well as the ICP to send it to, based on data given.

Template and ICP Generation
We’re making use of a GPT model, coupled with a few prompts to generate a number of templates and ICPs. I added this to make the process feel fully automated and easy to setup.

How Everything Would Work
Ideally we would be making use of an API service like apollo.io to get these ICPs and their data. We’ll be sending a specified number of emails everyday automatically, and for the learning aspect:

A model we’ll be in charge of generating new email templates, updating existing templates and updating the ICPs, depending on the overall metrics collected every 3-4 days.
We count link clicks as successes and no clicks as failures.
Other Ideas
We could add email opens as a metric, but I ultimately decided not to because to do that we would need to add an invisible image to the email in order to track the opens. The problem is that email provider platforms like Gmail and the like, make the user go through an extra step when opening the emails, which makes the email seem suspicious and untrustworthy, hence why I did not include it.

Tech Stack
Frontend: React + Typescript + Zustand + Vite
Backend: FastAPI + Python
Database: PostgreSQL
Model: GPT 4.1
Algorithm: Thompson Sampling

Github: https://github.com/habeebsl/email-marketer
Demo Video: https://www.loom.com/embed/2d2f23e526424e10a144333c75de1ff1?sid=c340343b-4b55-493b-b99a-17ee9d81b696
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

    "technical_skills": "**Skills**\nC, Python, JavaScript, Typescript, SQL, HTML, CSS, Node.js, Express.js, Vue.js, React.js, Next.js, GraphQL, Matter.js, Pinia, Vite, TailwindCSS, Flask, Django, FastAPI, SQLAlchemy, Pytest, Postman, Redis, PostgreSQL, MySQL, SQLite, Docker, AWS, Pinecone, RAG, Langchain, FAISS, HayStack, Render, Vercel, Heroku, Tembo, Supabase, Railway, Firebase, Git, GitHub, Gemini, GPT-4, Mistral, Prompt Engineering, Robotic Process Automation, Web Scraping, Backend Development",

    "ai_therapist": therapist_project,

    "avox": avox_project,

    "keypoint": keypoint_project,

    "chattersort": chattersort_project,
    
    "activity_builder": activity_builder_project,

    "ai_translator": translator_project,
    
    "email_marketer": marketer_project,

    "projects": f"**Projects**\n{avox_project}\n\n{keypoint_project}\n\n{chattersort_project}\n\n{therapist_project}\n\n{activity_builder_project}\n\n{translator_project}\n\n{marketer_project}",

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


