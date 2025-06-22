# 📄 LLaMA Summarizer - Streamlit App

This project is a **local/offline PDF & Text Summarizer** powered by **Meta LLaMA 3 8B Instruct GGUF** model, wrapped in a **Streamlit UI**. It allows you to upload `.pdf` or `.txt` files and generates a concise summary, also saving the output to a **PDF in the `Output/` folder**.

---

## 📁 Directory Structure

```
llama_summarizer_streamlit/
├── app.py                # Streamlit UI entrypoint
├── utils.py              # File parsing, LLM interaction, and PDF saving utilities
├── requirements.txt      # Required Python dependencies
├── models/               # Contains the GGUF LLaMA model file
│   └── Meta-Llama-3-8B-Instruct-Q4_K_M.gguf
├── Output/               # Summarized PDFs are saved here
└── README.md             # You're reading it now
```

---

## 🚀 Features

- 📤 Upload PDF or TXT
- 📚 View extracted content (first 3K characters)
- 🧠 Summarize using LLaMA 3 (running locally)
- 📄 Save summary as `<input_filename>_summary.pdf` in the `Output` folder

---

## 🧑‍💻 Setup Instructions

### 1. ✅ Clone the Repository

```bash
git clone https://github.com/prashant12jul/llama_summarizer_streamlit.git
cd llama_summarizer_streamlit
```

### 2. 📦 Create Virtual Environment

```bash
python -m venv venv
.env\Scriptsctivate      # Windows
# OR
source venv/bin/activate     # macOS/Linux
```

### 3. 🔧 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🤖 Download the LLaMA Model (Offline)

Download from Hugging Face and place the `.gguf` model file into `models/`:

```bash
pip install huggingface_hub
huggingface-cli download bartowski/Meta-Llama-3-8B-Instruct-GGUF Meta-Llama-3-8B-Instruct-Q4_K_M.gguf   --local-dir ./models --local-dir-use-symlinks False
```

> Ensure the final path looks like:  
> `models/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf`

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

- Go to: `http://localhost:8501`
- Upload a file → Click "Generate Summary" → View and Save the result

---

## 📝 Example Output

After summarization, you'll get a PDF saved as:

```
Output/
├── your_uploaded_file_summary.pdf
```

---

## 📦 Requirements

Minimal `requirements.txt`:

```
streamlit
fpdf
llama-cpp-python>=0.2.24
PyMuPDF
huggingface_hub
```

---

## 🙋‍♂️ Author

**Prashant Kumar**  
🔗 GitHub: [@prashant12jul](https://github.com/prashant12jul)

---

## 📄 License

This project is for educational and local inference purposes only. All model rights belong to their respective owners (Meta AI).
