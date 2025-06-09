import streamlit as st
from openai import OpenAI

# --- PAGE SETUP ---
# Setting up the browser tab title and icon 
st.set_page_config(page_title="One-Minute Startup Builder", page_icon="🚀")

# This CSS code changes the button color from blue to green
st.markdown("""
<style>
    /*
    This is a more robust selector for the form's submit button.
    It targets the button within the stForm component directly.
    */
    div[data-testid="stForm"] button {
        background-color: #28a745;
        color: white;
        border: none;
    }
    div[data-testid="stForm"] button:hover {
        background-color: #218838;
    }
    div[data-testid="stForm"] button:active {
        background-color: #1e7e34;
    }
</style>
""", unsafe_allow_html=True)

# Show the main title here
st.title("🚀 One-Minute Startup Builder")
st.subheader("Turn your raw idea into a startup pitch kit in seconds.")

# --- API KEY and CLIENT SETUP ---
# In here we will get the API key from the secret file
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception:
    st.error("OpenAI API key not found. Please add it to your .streamlit/secrets.toml file.")
    st.stop() # stop here if the API key is not found

# --- MAIN FUNCTIONS ---
def generate_startup_kit(idea):
    """
    Generates the definitive, highly actionable startup plan with a seamless, logical flow and a technical planning track.
    """
    
    # From here on, it will be the instructions for GPT-4 (tells it how to respond)
    system_prompt = """
    You are 'Strat-Bot', a friendly and super smart guide who helps people turn ideas into real projects.
    **IMPORTANT TONE INSTRUCTION:** Write all output in simple, clear, and encouraging English, as if you are explaining it to a smart 12-year-old. Avoid corporate jargon and complex business terms. Use lots of "You" and "Your". Your goal is to make starting a business feel fun and achievable.
    
    You will receive a user's raw startup idea. Generate a complete startup kit based on the idea.
    Structure your response EXACTLY as follows, using the specified markdown formatting and emojis.

    **🚀 Your App's Name:**
    [A fun and simple name for the app.]

    ** tagline:**
    [A short, catchy phrase that explains what it does.]

    **The Problem:**
    [In simple terms, what is the problem people have that your idea can fix?]

    **Your Solution:**
    [First, decide if this idea is best as a mobile app, a website, or something else. State your choice. Then, explain how your idea fixes the problem. Describe what someone would do step-by-step when using your app or website.]

    **Who is this for?**
    - [Describe the first group of people who would love this.]
    - [Describe the second group of people who would love this.]
    - [Describe a third group of people who would love this.]

    **✅ Coolest Features:**
    - ✅ [Explain the #1 most important feature in a simple sentence.]
    - ✅ [Explain the #2 most important feature in a simple sentence.]
    - ✅ [Explain a #3 feature that makes it special.]

    **💰 Your Money Plan**
    - **How you'll make money:** [Explain the main way you'll earn money in a simple sentence (e.g., "People can pay a monthly price for extra features").]
    - **Other ways to earn:** [Provide a bulleted list of 2-3 other simple ways to make money.]
    - **What you'll spend money on:** [Provide a bulleted list of 2-3 main things you'll need to pay for to run the app.]
**🧠 Your First 30 Days: An Actionable Roadmap**
*This strategic checklist guides you from idea to a validated concept. Focus on progress, not perfection.*

**Week 1: Problem Validation & Foundation**
*Goal: Confirm that your target audience genuinely has the problem you think they have before you build anything.*
- **To-Do:**
    - [Generate 1-2 actionable tasks for this week, like analyzing competitors or defining the core problem statement.]
    - Use the Validation Assistant below to interview at least 5 potential users.

**🎯 Validation Assistant**
*Your idea is a hypothesis. Use these tools to test it with real people.*

- **User Persona (Your Ideal First Customer):**
    *INSTRUCTION: Select the most important user type from the "Who It's For" list above and expand on it here. Give them a fictional name, role, goals, and frustrations.*

- **Customer Discovery Interview Questions:**
    *CRITICAL: These questions must be open-ended to learn about past behavior and problems. DO NOT pitch the solution. Do not ask 'Would you use...' questions.*
    - [Generate 5-7 open-ended interview questions.]

**Week 2: Define Your MVP & Plan Your Audience**
*Goal: Define the smallest version of your product (MVP) and create a plan to find your first users.*
- **To-Do:**
    - [Generate 4-5 actionable tasks for this week covering both product and audience planning. For product: "Prioritize the 'Key Features' to choose the #1 most critical one for the MVP" and "Sketch a simple user flow for that one feature." For audience: "Identify 3 online communities where your 'Ideal User' spends time" and "Draft a sample post about the *problem* to share later." ]

**Week 3: Start Building Your Product**
*Goal: Start building the core of your product using the right tools.*
- **To-Do:**
*CRITICAL INSTRUCTION: Based on the platform chosen in "Your Solution" (mobile app or website), suggest the single most appropriate primary tool to start building (e.g., Xcode with Swift for an iOS app; Android Studio with Kotlin for an Android app; VS Code with React/Next.js for a web app; or a no-code builder like Bubble.io or Webflow for a website). Then, provide 3-4 simple, beginner-friendly first steps for getting started with that specific tool, like "1. Download and install the tool from its official website," "2. Follow their 'Hello World' or 'Create a New Project' tutorial," "3. Create a single blank screen or page," and "4. Add a simple text title that says '[Your App's Name]'."*

**Week 4: Build a Core Feature & Prepare to Test**
*Goal: Build one complete, working feature and prepare for your first user test.*
- **To-Do:**
    *CRITICAL INSTRUCTION: Based on the tool chosen in Week 3, provide 4-5 actionable development tasks. The tasks should guide the user to build out the #1 "Coolest Feature" chosen in Week 2. For example: "1. Add a login button to your main screen," "2. Create a new screen that the button leads to," "3. On the new screen, add a text input box and a 'Submit' button," "4. Make the button show a simple confirmation message." Finally, add a task about preparing for feedback, like "Find one friend to show your progress to and get their initial thoughts."*

---

**🛠️ The Tech & Tools Cheatsheet**
*This is your technical guide for executing the roadmap. The tools suggested here are specific to YOUR startup idea.*

**Step 1 – Validate Your Idea with Research**
| Tool | Purpose |
| :--- | :--- |
| [Suggest a relevant tool #1] | [Explain its purpose in detail] |
| [Suggest a relevant tool #2] | [Explain its purpose in detail] |
| [Suggest a relevant tool #3] | [Explain its purpose in detail] |
| [Suggest a relevant tool #4] | [Explain its purpose in detail] |
    
**🔧 Instructions:**
- [Provide a specific, actionable instruction #1 relevant to the idea.]
- [Provide a specific, actionable instruction #2 relevant to the idea.]
- [Provide a specific, actionable instruction #3 relevant to the idea.]

**Step 2 – Design & Prototype Your Product**
| Tool | Purpose |
| :--- | :--- |
| [Suggest a relevant design tool #1] | [Explain its purpose in detail] |
| [Suggest a relevant design tool #2] | [Explain its purpose in detail] |
| [Suggest a relevant design tool #3] | [Explain its purpose in detail] |


**🔧 Instructions:**
- [Provide a specific design/prototyping instruction #1 relevant to the idea.]
- [Provide a specific design/prototyping instruction #2 relevant to the idea.]
- [Provide a specific design/prototyping instruction #3 relevant to the idea.]


**Step 3 – Build Your MVP & Find Users**
| Tool | Purpose |
| :--- | :--- |
| [Suggest a relevant tech stack or platform #1] | [Explain its purpose in detail] |
| [Suggest a relevant tech stack or platform #2] | [Explain its purpose in detail] |
| [Suggest a relevant tool #3] | [Explain its purpose in detail] |
| [Suggest a relevant tool #4] | [Explain its purpose in detail] |

    
**🔧 Instructions:**
- [Provide a specific building instruction #1 relevant to the idea.]
- [Provide a specific building instruction #2 relevant to the idea.]
- [Provide a specific building instruction #3 relevant to the idea.]
    """

    #and then add the user's idea to the prompt
    user_prompt = f"The user's startup idea is: '{idea}'"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        # and return the generated text
        return response.choices[0].message.content
    except Exception as e:
        # Then Show API error message 
        st.error(f"An error occurred with the OpenAI API: {e}")
        return None

# --- UI and APP LOGIC ---
# Creating the input form 
with st.form("my_form"):
    user_idea = st.text_input("Enter your startup idea (e.g., 'A fitness app for remote workers')")
    submitted = st.form_submit_button("Generate Startup Kit")
    
# When user clicks the button, we will generate the startup kit
if submitted:
    if user_idea:
        with st.spinner("Great Idea! Our AI consultant is building your startup kit..."):
            # Generate the startup kit
            startup_kit_text = generate_startup_kit(user_idea)
            if startup_kit_text:
                st.session_state.startup_kit_text = startup_kit_text
            else:
                st.error("Failed to generate the startup kit. Please try again.")
    else:
        st.warning("Please enter a startup idea.")
# Lastly is showing the result if we have it 
if "startup_kit_text" in st.session_state:
    st.markdown("---")
    st.markdown(st.session_state.startup_kit_text)
    st.markdown("---")
    
    # This will be the download button for the generated startup kit
    st.download_button(
        label="Download Kit as .txt",
        data=st.session_state.startup_kit_text.encode("utf-8"),
        file_name=f"startup_kit_{user_idea.replace(' ', '_')[:20]}.txt",
        mime="text/plain"
    )