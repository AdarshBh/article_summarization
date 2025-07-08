---
title: Hindi News Summarizer 🇮🇳
emoji: 📰
colorFrom: pink
colorTo: red
sdk: gradio
sdk_version: "4.28.1"
app_file: app.py
pinned: false
---

# Hindi News Summarizer 🇮🇳📰

This Space demonstrates an **abstractive Hindi text summarizer** fine-tuned on the **ILSUM 2024 Hindi dataset** using `ai4bharat/IndicBART`. It takes a Hindi article as input and generates a concise summary using a Transformer-based sequence-to-sequence model.

---

## 📌 Model Details

- **Base model**: [`ai4bharat/IndicBART`](https://huggingface.co/ai4bharat/IndicBART)
- **Task**: Abstractive Summarization (Hindi)
- **Trained on**: ILSUM 2024 (Hindi split)
- **Framework**: Transformers + Gradio

---

## 🚀 Usage

### 🔹 Input
Paste any **long-form Hindi article** (e.g., news, blog, report) into the textbox.

### 🔹 Output
A short, fluent **abstractive summary** in Hindi.

---

## 🧪 Try It Live

👉 Open the app:  
**[Hindi News Summarizer on Hugging Face Spaces](https://huggingface.co/spaces/adarshbhardwaj/indicbart-hindi-summarizer)**

---

## 🛠️ Tech Stack

- Python
- Hugging Face Transformers
- Gradio
- PyTorch
- ILSUM 2024 dataset

---

## 🧠 Sample Input/Output

**Input (Hindi Article):**
```
हिंदुस्तान में मानसून ने दस्तक दे दी है और कई इलाकों में भारी बारिश हो रही है जिससे जनजीवन प्रभावित हो रहा है...
```

**Generated Summary:**
```
मानसून की शुरुआत के साथ देश के कई हिस्सों में भारी बारिश से जनजीवन प्रभावित।
```

---

## 📦 How to Run Locally

```bash
git clone https://huggingface.co/spaces/Adarsh921/indicbart-hindi-summarizer
cd indicbart-hindi-summarizer
pip install -r requirements.txt
python app.py
```

---

## 🤝 Acknowledgements

- [AI4Bharat](https://ai4bharat.org/)
- [Gradio](https://gradio.app/)
- Hugging Face 🤗

---
