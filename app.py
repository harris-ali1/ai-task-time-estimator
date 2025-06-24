import streamlit as st
import time
from main import get_estimate

# Session state init
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
if "history" not in st.session_state:
    st.session_state.history = []

# Dark/light toggle handler
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# CSS for styling & animations (same as before)
def local_css():
    css = f"""
    <style>
    @keyframes gradientBG {{
      0% {{background-position: 0% 50%;}}
      50% {{background-position: 100% 50%;}}
      100% {{background-position: 0% 50%;}}
    }}

    body {{
      margin:0;
      background: linear-gradient(-45deg, #121212, #1a1a1a, #121212, #1a1a1a);
      background-size: 400% 400%;
      animation: gradientBG 20s ease infinite;
      transition: background-color 0.5s ease;
      color: {'#e0e0e0' if st.session_state.dark_mode else '#121212'};
    }}

    .stApp {{
        background-color: {'#121212' if st.session_state.dark_mode else '#f0f0f0'} !important;
        color: {'#e0e0e0' if st.session_state.dark_mode else '#121212'} !important;
        transition: background-color 0.5s ease, color 0.5s ease;
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }}

    .stTextArea > div > div > textarea {{
        background-color: {'#1e1e1e' if st.session_state.dark_mode else '#fff'};
        color: {'#e0e0e0' if st.session_state.dark_mode else '#121212'};
        transition: background-color 0.5s ease, color 0.5s ease;
    }}

    .stButton > button {{
        background-color: {'#333' if st.session_state.dark_mode else '#ddd'} !important;
        color: {'#e0e0e0' if st.session_state.dark_mode else '#121212'} !important;
        border: none;
        padding: 0.5rem 1.2rem;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: {'#555' if st.session_state.dark_mode else '#bbb'} !important;
    }}

    .stCodeBlock {{
        background-color: {'#1e1e1e' if st.session_state.dark_mode else '#eee'};
        color: {'#e0e0e0' if st.session_state.dark_mode else '#121212'};
        border-radius: 5px;
        padding: 1rem;
        font-size: 0.9rem;
        white-space: pre-wrap;
        transition: background-color 0.5s ease, color 0.5s ease;
    }}

    details {{
        background-color: {'#222' if st.session_state.dark_mode else '#fafafa'};
        padding: 0.75rem 1rem;
        border-radius: 5px;
        margin-top: 0.5rem;
        color: {'#ddd' if st.session_state.dark_mode else '#444'};
        transition: background-color 0.5s ease, color 0.5s ease;
    }}

    .css-1d391kg {{
        background-color: {'#1e1e1e' if st.session_state.dark_mode else '#fff'} !important;
        color: {'#e0e0e0' if st.session_state.dark_mode else '#121212'} !important;
        transition: background-color 0.5s ease, color 0.5s ease;
    }}

    .switch {{
      position: relative;
      display: inline-block;
      width: 50px;
      height: 28px;
    }}

    .switch input {{
      opacity: 0;
      width: 0;
      height: 0;
    }}

    .slider {{
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #ccc;
      transition: .4s;
      border-radius: 28px;
    }}

    .slider:before {{
      position: absolute;
      content: "";
      height: 22px;
      width: 22px;
      left: 3px;
      bottom: 3px;
      background-color: white;
      transition: .4s;
      border-radius: 50%;
    }}

    input:checked + .slider {{
      background-color: #2196F3;
    }}

    input:checked + .slider:before {{
      transform: translateX(22px);
    }}

    .history-card {{
      background-color: {'#222' if st.session_state.dark_mode else '#fafafa'};
      margin: 0.5rem 0;
      padding: 0.75rem 1rem;
      border-radius: 8px;
      cursor: pointer;
      box-shadow: 0 2px 5px rgba(0,0,0,0.3);
      transition: background-color 0.3s ease;
    }}

    .history-card:hover {{
      background-color: {'#444' if st.session_state.dark_mode else '#ddd'};
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Typewriter effect line-by-line for clean formatting
def typewriter_lines(text, placeholder, delay=0.05):
    placeholder.empty()
    lines = text.split('\n')
    displayed = ""
    for line in lines:
        displayed += line + "\n"
        placeholder.code(displayed)
        time.sleep(delay)

local_css()

st.set_page_config(page_title="AI Time Estimator (Animated Dark/Light Mode)", layout="centered")

with st.sidebar:
    st.header("Settings")
    st.checkbox("Dark Mode", value=st.session_state.dark_mode, on_change=toggle_dark_mode)
    temperature = st.slider("Temperature (creativity)", 0.0, 1.0, 0.4, 0.05)
    max_tokens = st.slider("Max Tokens (response length)", 50, 500, 300, 25)

st.title("🧠 AI Time Estimator for Coding Tasks")

st.markdown("""
<p style="color:#bbbbbb; font-size:16px;">
This tool uses a local AI model (Mistral) to estimate the time, difficulty, and steps needed to complete your coding task.<br>
Paste your task description below and click 'Estimate Time' to get started.
</p>
""", unsafe_allow_html=True)

task_description = st.text_area("Paste your coding task below:", height=200)

from main import get_estimate

@st.cache_data(show_spinner=False)
def cached_estimate(prompt: str, temperature: float, max_tokens: int) -> str:
    return get_estimate(prompt, temperature=temperature, max_tokens=max_tokens)

result_placeholder = st.empty()

def show_result(result: str):
    # Use typewriter effect line-by-line for smooth clean display
    typewriter_lines(result, result_placeholder)

def add_to_history(task: str, response: str):
    st.session_state.history.insert(0, {"task": task, "response": response})
    if len(st.session_state.history) > 10:
        st.session_state.history.pop()

def show_history():
    st.sidebar.markdown("### History")
    for i, entry in enumerate(st.session_state.history):
        if st.sidebar.button(f"Task #{i+1}: {entry['task'][:30]}..."):
            show_result(entry["response"])

if st.button("Estimate Time"):
    if not task_description.strip():
        st.warning("Please enter a task.")
    else:
        with st.spinner("Estimating..."):
            prompt = f"""
You are a senior software engineer. Given the following task description, estimate:

1. Time to complete (in hours or days)
2. Difficulty (Easy / Medium / Hard)
3. Steps to complete

Respond exactly in this format:
- Estimated time: ...
- Difficulty: ...
- Suggested steps:
  1. ...
  2. ...
  3. ...

Task:
\"\"\"
{task_description}
\"\"\"
"""
            try:
                result = cached_estimate(prompt, temperature, max_tokens)
                add_to_history(task_description, result)
                show_result(result)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

show_history()
