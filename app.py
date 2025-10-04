import os


import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

# PDF parsing
import pdfplumber

llm = ChatOpenAI(model=selected_model, temperature=temperature)


#PDF Upload
# --------------------------
uploaded = st.file_uploader("\desktop\zhang_2024_Data_AIin_Food_copy.pdf", type=["pdf"])

if uploaded is not None:
    if uploaded.type != "application/pdf":
        st.error("Sadece PDF dosyaları kabul edilir.")
        st.stop()

    size_mb = uploaded.size / (1024 * 1024)
    if size_mb > max_file_mb:
        st.error(f"Dosya çok büyük ({size_mb:.2f} MB). Maksimum {10_mb} MB.")
        st.stop()

    # Try extraction
    try:
        st.session_state.pdf_name = uploaded.name
        file_bytes = BytesIO(uploaded.read())
        full_text, page_texts, page_count = extract_text_with_pdfplumber(file_bytes)
        st.session_state.document_text = full_text
        st.session_state.page_texts = page_texts
        st.session_state.page_count = page_count

        st.success(f"'{uploaded.name}' başarıyla okundu.")
        st.info(f"Toplam sayfa: {page_count}. Okunan sayfalar: {', '.join(str(i) for i in range(1, page_count+1))}")

        # Preview
        with st.expander("📄 PDF Önizleme (1. sayfa metni)"):
            first_page_text = page_texts[0][:2000] if page_texts else ""
            st.write(first_page_text if first_page_text.strip() else "(İlk sayfada metin çıkarılamadı)")

        # Full text in expander (can be long)
        with st.expander("🧾 Çıkarılan Metnin Tamamını Göster"):
            st.text_area("Metin", value=full_text, height=300)

        # Stats
        chars = len(full_text)
        words = len(re.findall(r"\w+", full_text))
        st.caption(f"Karakter: {chars:,} • Kelime: {words:,}")

    except Exception as e:
        st.error(f"PDF işlenirken hata: {e}")
        st.stop()


