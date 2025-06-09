🚀 One-Minute Startup Builder
[][python-url]
[][streamlit-url]
[][openai-url]
[][license-url]

➡️ Watch the Project Demo on YouTube: https://www.youtube.com/watch?v=BYyOgT41pM8 ⬅️

&lt;br>

A sophisticated AI co-pilot that transforms a one-sentence idea into a comprehensive, actionable startup plan.

🎯 The Goal
Millions of people have brilliant ideas but get stuck on the first step. This project solves that initial friction by acting as an instant "founder's mentor," turning a raw thought into a structured, achievable plan.

✨ The Solution
The One-Minute Startup Builder is an interactive web app that takes a single idea and generates a complete business kit. This includes a financial snapshot, a personalized 30-day action plan, and even a script to interview potential customers.

🧠 The Innovation
The core of this project is a meticulously engineered multi-module prompt for GPT-4o. Instead of using a static template, the app instructs the AI on how to think—acting as a consultant, product manager, and mentor to dynamically generate a relevant business strategy and technical roadmap for any idea.

Key Features:

- Instant Startup Brief: Generates a company name, tagline, problem/solution, and target audience.
- Detailed Financial Snapshot: Outlines potential revenue streams and key operational costs.
- Personalized 30-Day Action Plan: A week-by-week checklist that guides a user from idea to validated concept.
- Built-in Customer Interview Guide: Provides a user persona and expertly crafted, non-leading questions to help founders talk to real users.
- Polished & Responsive UI: Features a custom-styled green button that is disabled during processing for clear user feedback.

🛠️ Tech Stack
Technology	Purpose
Python	Core programming language for application logic.
Streamlit	Web framework for building the interactive user interface.
OpenAI API (gpt-4o)	The AI engine for all text generation and dynamic reasoning.
Custom CSS	Injected via st.markdown to create custom button styles.
Git & GitHub	Version control and hosting the public code repository.
Streamlit Community Cloud	Platform for deploying and hosting the live web application.

🚀 Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites

Python 3.8+
An OpenAI API Key
Installation

Clone the repository:

Bash
git clone [https://github.com/JosephVn272/-One-Minute-Startup-Builder-.git](https://github.com/JosephVn272/-One-Minute-Startup-Builder-.git)
cd -One-Minute-Startup-Builder-
 Create and activate a virtual environment:

Bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Bash
# For Windows
python -m venv venv
.\venv\Scripts\activate
 Install the required dependencies:

Bash
pip install -r requirements.txt
 Set up your OpenAI API Key:

Create a file at this path: .streamlit/secrets.toml
Add your API key to the file like this:
Ini, TOML
OPENAI_API_KEY = "your-sk-key-here"
 Run the application:

Bash
streamlit run app.py
🧭 Future Roadmap

[ ] User Accounts: Allow users to save, edit, and manage their generated startup plans.
[ ] PDF Export: Add a feature to download the plan as a beautifully formatted PDF pitch document.
[ ] DALL-E Integration: Re-integrate image generation for creating logos or app mockups.
⚖️ Licensing

Distributed under the MIT License. You will need to create a LICENSE.txt file if you wish to include one.

🧑‍💻 Contact
Hao Tran - LinkedIn - josephvn272@gmail.com

Project Link: https://github.com/JosephVn272/-One-Minute-Startup-Builder-

[]: #
[python-url]: https://www.python.org/
[]: #
[streamlit-url]: https://streamlit.io/
[]: #
[openai-url]: https://openai.com/
[]: #
[license-url]: https://www.google.com/search?q=https://github.com/JosephVn272/-One-Minute-Startup-Builder-/blob/main/LICENSE.txt
