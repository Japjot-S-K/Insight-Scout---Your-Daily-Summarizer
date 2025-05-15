# Insight Scout: AI-Powered News Research Tool

Tired of understanding large asticles without finding any baseline? Wanna ask questions about an article but are butchered by the character limit in other AI tools?
I bring to you Insight Scout.
Insight Scout is a streamlined, AI-driven tool designed for extracting and interacting with news content. Users can input article URLs and ask questions to receive AI-generated insights directly from the article content.

![](insight_scout.jpg)

## 🚀 Features

- Enter up to 3 news URLs to extract and process their content.
- Uses LangChain's `UnstructuredURLLoader` to load content from webpages.
- Splits and embeds content using HuggingFace sentence-transformer models.
- Stores processed content in a FAISS vector store for similarity-based retrieval.
- Interacts with the locally loaded **TeapotLLM** to generate answers for user queries.
- Includes a Lottie-powered animated UI, dark theme, and modern layout with expandable app info section.

---

## 🛠 Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/insight-scout.git
```

2. Navigate to the project directory:
```bash
cd insight-scout
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

---

## 💡 Usage

1. Start the Streamlit app:
```bash
streamlit run main.py
```

2. In the web interface:
   - Enter up to three article/converted notepad/md links.
   - Click **Process URLs** to fetch and embed article content.
   - Ask any question in the input box like "What's the main topic?" or "Who is mentioned in the article?".
   - View AI-generated responses based on the content.

3. Click the “📘 What’s this app about?” section to learn more from this README file within the app.

---

## 🔥 Screenshots

### Homepage
![Homepage](screenshots/homepage.png)

### Question & Answer Interface
![Q&A Interface](screenshots/question_answer.png)


## 📁 Project Structure

- `main.py` – Streamlit app code with UI + backend logic.
- `requirements.txt` – List of Python dependencies.
- `README.md` – Documentation file loaded inside the app.
- `.streamlit/config.toml` – Custom theme settings.
- `faiss_store_openai.pkl` – FAISS index file for cached embeddings (optional).

---
## 📁 Other important things

- Keep in mind the project uses the free hugging face offline model to work and is not as accurate
- To assure higher accuracy, use your own OPEN Ai API key in the .env folder and replace the main.py file currently in the folder with the main.py in OPEN AI folder
- Assure that you have important libraries installed as prompted by cmd if you are working on any API in this model other than huggingFace offline to use the model
- Thank you for viewing the project
- THIS PROJECT IS NOT FOR PUBLIC USE
## 🙌 Author

**Project by Japjot Singh Kashyap**
