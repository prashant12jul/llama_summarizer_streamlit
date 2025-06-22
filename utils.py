import os
import fitz  # PyMuPDF
from fpdf import FPDF
from llama_cpp import Llama

def extract_text(file):
    ext = os.path.splitext(file.name)[1].lower()
    if ext == ".pdf":
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return " ".join(page.get_text() for page in doc)
    elif ext == ".txt":
        return file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file type")

def load_model(model_path="models/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf"):
    return Llama(model_path=model_path, n_ctx=2048, n_threads=8, verbose=False)

def summarize_text(llm, text):
    prompt = f"### Instruction:\nSummarize the following text:\n\n{text}\n\n### Response:"
    output = llm(prompt, max_tokens=512, stop=["###"] or ["User:", "Assistant:"])
    return output["choices"][0]["text"].strip()

def save_summary_pdf(summary_text: str, input_filename: str, output_dir: str = "Output"):
    os.makedirs(output_dir, exist_ok=True)
    input_name = os.path.splitext(os.path.basename(input_filename))[0]
    output_path = os.path.join(output_dir, f"{input_name}_summary.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in summary_text.splitlines():
        pdf.multi_cell(0, 10, line)

    pdf.output(output_path)
    return output_path