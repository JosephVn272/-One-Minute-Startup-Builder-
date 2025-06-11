
🚀 One-Minute Startup Builder

➡️ Watch the Project Demo on YouTube: https://www.youtube.com/watch?v=BYyOgT41pM8 ⬅️

A sophisticated AI co-pilot that transforms a one-sentence idea into a comprehensive, actionable startup plan.

The Goal
Millions of people have brilliant ideas but get stuck on the first step. This project solves that initial friction by acting as an instant "founder's mentor," turning a raw thought into a structured, achievable plan.

The Solution
The One-Minute Startup Builder is an interactive web app that takes a single idea and generates a complete business kit. This includes a financial snapshot, a personalized 30-day action plan, and even a script to interview potential customers.

The Innovation
The core of this project is a meticulously engineered multi-module prompt for GPT-4o. Instead of using a static template, the app instructs the AI on how to think—acting as a consultant, product manager, and mentor to dynamically generate a relevant business strategy and technical roadmap for any idea.

Key Features
* Instant Startup Brief: Generates a company name, tagline, problem/solution, and target audience.
* Detailed Financial Snapshot: Outlines potential revenue streams and key operational costs.
* Personalized 30-Day Action Plan: A week-by-week checklist that guides a user from idea to validated concept.
* Built-in Customer Interview Guide: Provides a user persona and expertly crafted, non-leading questions to help founders talk to real users.
* Polished & Responsive UI: Features a custom-styled green button that is disabled during processing for clear user feedback.

How to Use
1. Enter your startup idea - Type a simple one-sentence description (e.g., "A fitness app for remote workers")
2. Click "Generate Startup Kit" - The AI processes your idea and creates a comprehensive business plan
3. Review your complete plan - Browse through your personalized startup brief, financial projections, and action items
4. Download your kit - Export everything as a text file for future reference

Installation & Setup
Prerequisites
* Python 3.7 or higher
* OpenAI API key

Step-by-Step Installation
1. Clone the repository bash git clone https://github.com/yourusername/one-minute-startup-builder.git
2. cd one-minute-startup-builder 
3. Install dependencies bash pip install streamlit openai 
4. Set up your OpenAI API key Create a .streamlit/secrets.toml file in your project directory: toml OPENAI_API_KEY = "your-openai-api-key-here" Or set it as an environment variable:  bash export OPENAI_API_KEY="your-openai-api-key-here" 
5. Run the application bash streamlit run app.py 
6. Open your browser and navigate to http://localhost:8501

Project Structure
one-minute-startup-builder/
├── app.py                 # Main application logic and Streamlit interface
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .streamlit/
    └── secrets.toml      # OpenAI API key configuration (create this file)

Tech Stack
* Python: Core programming language for application logic
* Streamlit: Web framework for building the interactive user interface
* OpenAI API (gpt-4o): The AI engine for all text generation and dynamic reasoning
* Custom CSS: Injected via st.markdown to create custom button styles
* Git & GitHub: Version control and hosting the public code repository
* Streamlit Community Cloud: Platform for deploying and hosting the live web application

What I Learned
Building this project taught me that effective AI integration goes far beyond simple API calls. The real challenge was crafting prompts that could consistently generate business-quality output across diverse industries and idea types. I spent a lot of time on prompt engineering, learning how to structure instructions that guide AI reasoning rather than just requesting information.
The project also reinforced the importance of user experience in AI applications - even the most sophisticated backend is useless if users can't easily interact with it.


Contact
Hao Tran - LinkedIn - josephvn272@gmail.com
