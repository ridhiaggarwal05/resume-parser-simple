def extract_text_from_resume(uploaded_file):
    text = uploaded_file.read().decode("utf-8", errors="ignore")
    return text
