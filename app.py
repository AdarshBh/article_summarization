import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load from Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("Adarsh921/indicbart-hindi-summarizer")
model = AutoModelForSeq2SeqLM.from_pretrained("Adarsh921/indicbart-hindi-summarizer")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Inference function
def generate_summary(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=512,
        truncation=True,
        padding="max_length"
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    summary_ids = model.generate(
        inputs["input_ids"]
        num_beams=4,
        no_repeat_ngram_size=3
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Gradio UI
gr.Interface(
    fn=generate_summary,
    inputs=gr.Textbox(lines=10, label="Paste Hindi Article"),
    outputs=gr.Textbox(label="Generated Summary"),
    title="Hindi Article Summarizer",
    description="Summarizer fine-tuned on ILSUM 2024 using IndicBART"
).launch(share=True)
