import streamlit as st
import os
from utils import extract_text, load_model, summarize_text, save_summary_pdf

st.set_page_config(page_title="📄 LLaMA 3 Summarizer", layout="centered")
st.title("📄 Summarize PDF or Text using LLaMA 3 (Offline)")
st.markdown("Upload a `.pdf` or `.txt` file, and get a summary using **LLaMA 3** running locally.")

uploaded_file = st.file_uploader("📤 Upload File", type=["pdf", "txt"])

if uploaded_file:
    with st.spinner("📖 Extracting text..."):
        try:
            full_text = extract_text(uploaded_file)
            st.text_area("📚 Extracted Content (first 3K chars)", full_text[:3000] + "...", height=250)
        except Exception as e:
            st.error(f"❌ Error extracting file: {e}")
            st.stop()

    if st.button("🧠 Generate Summary"):
        with st.spinner("🚀 Summarizing... this may take 20–60 seconds..."):
            try:
                llm = load_model()
                summary = summarize_text(llm, full_text)
                st.success("✅ Summary Generated")
                st.text_area("📄 Summary Output", summary, height=200)

                # Save summary as PDF
                filename = uploaded_file.name.rsplit('.', 1)[0]
                output_path = os.path.join("output", f"{filename}_summary.pdf")
                save_summary_pdf(summary, output_path)

                st.success(f"📁 Saved summary to: {output_path}")

                with open(output_path, "rb") as f:
                    st.download_button(
                        label="📥 Download Summary PDF",
                        data=f,
                        file_name=f"{filename}_summary.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"❌ Error during summarization: {e}")
else:
    st.info("Please upload a `.pdf` or `.txt` file to start.")
