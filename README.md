# DeepOCR - Using MistralAI

DeepOCR is a powerful OCR (Optical Character Recognition) application built with Streamlit and powered by MistralAI. This application allows users to extract text from various document formats, including PDFs and images, or directly from URLs. The extracted text can be viewed and downloaded in multiple formats.

---

## 📌 Features
- **Multi-format Support**: Extract text from PDFs, images (PNG, JPG, JPEG), and URLs.
- **Fast & Accurate OCR**: Leverages MistralAI’s state-of-the-art OCR model.
- **User-Friendly UI**: Intuitive Streamlit-based interface.
- **Multiple Output Formats**: Download results in Text, Markdown, or JSON.
- **Secure Processing**: Uses a secure API key for MistralAI integration.

---

## 🛠️ Installation Guide

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` package manager
- MistralAI API Key

### Step-by-Step Setup
1. **Clone the repository**:
   ```sh
   git clone https://github.com/adityadeshpande03/DeepOCR
   cd DeepOCR
   ```
2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your MistralAI API key:
   ```sh
   MISTRAL_API_KEY=your_api_key_here
   ```

---

## 🚀 Usage Instructions

### Running the Application
Start the Streamlit application by running:
```sh
streamlit run app.py
```

### How to Use
1. **Choose an input method**: Select from `URL`, `PDF Upload`, or `Image Upload`.
2. **Upload a document or enter a URL**.
3. **Click on 'Process Document'** to extract text.
4. **View and download the extracted text** in various formats.

### Output Formats
- **Text (.txt)**: Plain text output.
- **Markdown (.md)**: Well-formatted structured text.
- **JSON (.json)**: Structured data with metadata.

---

## 🏗️ Technologies Used
- **Streamlit**: UI framework for interactive applications.
- **MistralAI**: OCR API for text extraction.
- **Pillow**: Image processing library.
- **python-dotenv**: Environment variable management.

---

## 🙌 Acknowledgments
- [MistralAI](https://mistral.ai) for their powerful OCR API.
- [Streamlit](https://streamlit.io) for providing an easy-to-use UI framework.

