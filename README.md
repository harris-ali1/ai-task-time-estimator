# AI Time Estimator for Coding Tasks

An interactive Streamlit app that uses a local AI model (Mistral via Ollama) to estimate the time, difficulty, and suggested steps for coding tasks.

---

## Features

- Dark / Light mode toggle with smooth transitions  
- Animated typewriter effect for AI responses  
- Subtle animated gradient background  
- Adjustable AI parameters: temperature and max tokens  
- Caching of AI responses for faster repeated queries  
- History panel to view and recall previous tasks and results  
- Clean, formatted AI output with suggested steps  

---

## Demo

![image](https://github.com/user-attachments/assets/49cbe7d0-c958-4833-b773-90af28d1ab18)


---

## Getting Started

### Prerequisites

- Python 3.10+  
- [Ollama](https://ollama.com/) installed and running locally with the `mistral` model  
- `streamlit` and `openai` Python packages  

### Installation

1. Clone the repo:

```bash
git clone https://github.com/harrisali/ai-time-estimator.git
cd ai-time-estimator

```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Run the app
```bash
streamlit run app.py
```
## Usage
- Paste your coding task description into the text area

- Adjust temperature and max tokens from the sidebar for response variation

- Click Estimate Time to get the AI's estimate

- Toggle Dark/Light mode as preferred

- View your previous queries and responses in the sidebar history panel

## Notes
- Make sure Ollama is running locally and the mistral model is available

- Your .env file or API key should be properly configured (if applicable)

- The app caches results to improve performance on repeated queries

## License
MIT License © Harris Ali

## Acknowledgements
- Built using Streamlit

- Powered by Ollama Mistral

- Inspired by modern AI UX best practices
