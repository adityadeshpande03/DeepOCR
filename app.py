import streamlit as st
import base64
import tempfile
import os
from mistralai import Mistral
from PIL import Image
import io
from dotenv import load_dotenv
import json
import time
from config.config import upload_pdf, process_ocr, display_pdf

load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")

def main():
    st.set_page_config(
        page_title="DeepOCR - Using MistralAI",
        page_icon="📄",
        layout="wide"
    )

    # Initialize API client
    api_key = mistral_api_key
    if not api_key:
        st.error("❌ Mistral API key not found! Please check your .env file.")
        st.stop()
    
    client = Mistral(api_key=api_key)

    # Sidebar
    with st.sidebar:
        st.title("📚 Instructions")
        st.markdown("""
        ### How to use:
        1. 🔍 Select input type:
           - URL: Paste a direct link to your document
           - PDF: Upload a PDF file
           - Image: Upload an image file
        
        2. 📤 Upload your document
        
        3. ⚡ Click 'Process Document'
        
        4. 📥 Download results in:
           - Text format
           - Markdown format
           - JSON format
        
        ### Supported Formats:
        - 📄 PDF documents
        - 🖼️ Images (PNG, JPG, JPEG)
        - 🔗 Direct URLs
        """)
        
    # Main content
    st.title("📄 DeepOCR - Using MistralAI ")
    st.markdown("### Extract text from documents and images using AI")
    
    input_method = st.radio(
        "🎯 Select Input Type:",
        ["URL", "PDF Upload", "Image Upload"],
        help="Choose how you want to input your document"
    )
    
    document_source = None
    
    if input_method == "URL":
        url = st.text_input("Document URL:")
        if url:
            document_source = {
                "type": "document_url",
                "document_url": url
            }
    
    elif input_method == "PDF Upload":
        uploaded_file = st.file_uploader("Choose PDF file", type=["pdf"])
        if uploaded_file:
            content = uploaded_file.read()
            document_source = {
                "type": "document_url",
                "document_url": upload_pdf(client, content, uploaded_file.name)
            }
    
    elif input_method == "Image Upload":
        uploaded_image = st.file_uploader("Choose Image file", type=["png", "jpg", "jpeg"])
        if uploaded_image:
            image = Image.open(uploaded_image)
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            document_source = {
                "type": "image_url",
                "image_url": f"data:image/png;base64,{img_str}"
            }
    
    if document_source and st.button("⚡ Process File ", type="primary"):
        with st.spinner("🔄 Processing document..."):
            try:
                ocr_response = process_ocr(client, document_source)
                
                if ocr_response and ocr_response.pages:
                    extracted_content = "\n\n".join(
                        [f"**Page {i+1}**\n{page.markdown}" 
                         for i, page in enumerate(ocr_response.pages)]
                    )
                    
                    st.success("✅ Document processed successfully!")
                    st.subheader("📝 Extracted Content")
                    
                    with st.expander("📄 View Content", expanded=True):
                        st.markdown(extracted_content)
                    
                    plain_text_content = "\n\n".join(
                        [f"Page {i+1}\n{page.markdown}" 
                         for i, page in enumerate(ocr_response.pages)]
                    )
                    
                    st.subheader("⬇️ Download Options")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.download_button(
                            label="📄 Download as Text",
                            data=plain_text_content,
                            file_name="extracted_content.txt",
                            mime="text/plain"
                        )
                    with col2:
                        st.download_button(
                            label="📝 Download as Markdown",
                            data=extracted_content,
                            file_name="extracted_content.md",
                            mime="text/markdown"
                        )
                    with col3:
                        json_content = {
                            "document_info": {
                                "total_pages": len(ocr_response.pages),
                                "extraction_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                            },
                            "pages": [
                                {
                                    "page_number": i + 1,
                                    "content": page.markdown
                                }
                                for i, page in enumerate(ocr_response.pages)
                            ]
                        }
                        st.download_button(
                            label="🔍 Download as JSON",
                            data=json.dumps(json_content, indent=4, ensure_ascii=False),
                            file_name="extracted_content.json",
                            mime="application/json"
                        )
                    
                    with st.expander("🔍 Raw API Response"):
                        st.json(ocr_response.model_dump())
                else:
                    st.warning("⚠️ No content extracted.")
            
            except Exception as e:
                st.error(f"❌ Processing error: {str(e)}")

if __name__ == "__main__":
    main()