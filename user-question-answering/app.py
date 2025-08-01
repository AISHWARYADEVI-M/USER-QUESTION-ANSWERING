import streamlit as st
from transformers import pipeline

# Load the pre-trained BERT model for QA
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

# Streamlit app setup
st.set_page_config(page_title="📖 Question Answering System", layout="centered")
st.title("📘 User Question Answering System")

# Input fields
context = st.text_area("📜 Paste the paragraph or passage:", height=200, placeholder="Enter a long text or document passage...")
question = st.text_input("❓ Enter your question:", placeholder="Ask a question based on the passage...")

# Answer button
if st.button("🔍 Get Answer"):
    if not context.strip() or not question.strip():
        st.warning("⚠️ Please fill in both the passage and the question.")
    else:
        result = qa_pipeline(question=question, context=context)
        st.success(f"✅ **Answer:** {result['answer']}")
        st.markdown(f"📊 **Confidence Score:** `{result['score']:.2f}`")
