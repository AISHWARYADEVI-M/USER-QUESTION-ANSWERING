# 📘 Question Answering System

## 📌 Project Overview
This project is an AI-powered Question Answering system built using a pre-trained BERT model.  
It allows users to input a paragraph and ask questions based on that text, and the system extracts the most relevant answer.

The application is built using Streamlit, providing a simple and interactive interface for real-time question answering.

---

## 🎯 Objective
- Build an NLP-based Question Answering system  
- Extract answers from unstructured text  
- Provide confidence scores for predictions  
- Demonstrate the use of transformer-based models  

---

## 🛠 Tools & Technologies
- **Python** – Core programming  
- **Streamlit** – Web interface  
- **Hugging Face Transformers** – NLP framework  
- **BERT Model** – Pre-trained QA model  

---

## 🧠 Model Details
- Model: `bert-large-uncased-whole-word-masking-finetuned-squad`  
- Task: Extractive Question Answering  
- Dataset: SQuAD  

---

## ✨ Features
- 📜 Input any paragraph or text  
- ❓ Ask questions based on the text  
- 🤖 AI-generated answers using BERT  
- 📊 Confidence score display  
- ⚡ Fast and interactive UI  
- 🧠 No training required (pre-trained model)  

---

## 🚀 How It Works
1. User enters a paragraph (context)  
2. User inputs a question  
3. The BERT model processes both inputs  
4. The system extracts the most relevant answer  
5. Displays answer with confidence score  

---

## 📁 Project Structure
- `app.py` – Main Streamlit application  
- `requirements.txt` – Dependencies  

---

## 💻 Installation
```bash
git clone https://github.com/your-username/question-answering-system.git
cd question-answering-system
pip install -r requirements.txt
```

---

## ▶️ Usage
```bash
streamlit run app.py
```

---

## 📊 Example
**Context:**  
Python is a high-level programming language used for web development, data science, and AI.

**Question:**  
What is Python used for?

**Output:**  
- Answer: web development, data science, and AI  
- Confidence Score: 0.92  

---

## 📌 Applications
- Educational tools  
- Chatbots  
- Document analysis  
- Information retrieval systems  

---

## ⚠️ Limitations
- Works only on given context  
- Cannot answer outside the text  
- Accuracy depends on input quality  

---

## 🔮 Future Enhancements
- PDF/document upload support  
- Multi-language support  
- Improved UI/UX  
- Advanced QA models  

---

## 📌 Disclaimer
This project is for educational purposes only.  
The answers generated may not always be 100% accurate.
