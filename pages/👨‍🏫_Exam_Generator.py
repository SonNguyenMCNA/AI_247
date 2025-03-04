import streamlit as st
from io import BytesIO
from base import request_gpt
import PyPDF2

st.set_page_config(
    page_title="Exam Generator", 
    page_icon="🤖",
)

st.write("# Exam Generator 👨‍🏫")

language = st.selectbox(
    "Choose language:",
    ("English", "Tiếng Việt"),
    index=None
)

if not language:
    st.stop()

if language == "English":
    uploaded_file = st.file_uploader("Upload file")

    if not uploaded_file:
        st.stop()

    num_question = st.text_input("Choose number of questions:")

    if not num_question:
        st.stop()

    question_type = st.selectbox(
        "Choose question type:",
        ("Multiple choice", "True/False", "Fill in the blank"),
        index=None
        )

    if not question_type:
        st.stop()

    difficulty = st.selectbox(
        "Choose difficulty level:",
        ("Easy", "Medium", "Hard"),
        index=None
        )

    if not difficulty:
        st.stop()

    limit = st.selectbox(
        "Limit the content in the file?",
        ('Yes', 'No'),
        index=None
    )

    if not limit:
        st.stop()

    prompt = f"From the input file, generate a test with {num_question} questions of type {question_type} with difficulty level {difficulty}."

    if limit == 'Yes':
        limit_type = st.selectbox(
            "Choose how to limit content:",
            ('By Page Range', 'By Chapters'),
            index=None
        )

        if not limit_type:
            st.stop()

        if limit_type == 'By Page Range':
            pdfReader = PyPDF2.PdfFileReader(BytesIO(uploaded_file.read()))
            num_pages = pdfReader.getNumPages()

            limit_range = st.slider("Choose the page range of the file:", 1, num_pages, (1, num_pages))
            st.markdown(f"Content range: {limit_range[0]} - {limit_range[1]}")
            extra_prompt = f" Limit the content in the file from page {limit_range[0]} to page {limit_range[1]}."

        elif limit_type == 'By Chapters':
            chapters = st.text_area("Enter the chapter numbers or titles")
            if not chapters:
                st.warning("Please enter at least one chapter number or title.")
                st.stop()
            extra_prompt = f" Limit the content to chapter {chapters} in the file."


        prompt = prompt + extra_prompt

    prompt = prompt + " At the end of the test, add a new section to provide the correct answer and detailed explanation for each question. Also refer to the page number in the file for each question and quote the relevant text."

    # st.markdown(prompt)

    if st.button("Generate Exam"):
        print(prompt)
        request_gpt(uploaded_file, prompt, "test")
        

elif language == "Tiếng Việt":
    uploaded_file = st.file_uploader("Tải lên tệp") 

    if not uploaded_file:
        st.stop()

    num_question = st.text_input("Điền số lượng câu hỏi:")

    if not num_question:
        st.stop()

    question_type = st.selectbox(
        "Chọn loại câu hỏi:",
        ("Trắc nghiệm", "Đúng/Sai", "Điền từ vào chỗ trống"),
        index=None
        )

    if not question_type:
        st.stop()

    difficulty = st.selectbox(
        "Chọn mức độ khó:",
        ("Dễ", "Trung bình", "Khó"),
        index=None
        )

    if not difficulty:
        st.stop()

    limit = st.selectbox(
        "Giới hạn nội dung trong tệp?",
        ('Có', 'Không'),
        index=None
    )

    if not limit:
        st.stop()
    

    prompt = f"Từ tệp đầu vào, tạo bài kiểm tra với {num_question} câu hỏi loại {question_type} với mức độ {difficulty}."

    if limit == 'Có':
        limit_type = st.selectbox(
            "Chọn cách giới hạn nội dung:",
            ('Theo Phạm Vi Trang', 'Theo Chương'),
            index=None
        )

        if not limit_type:
            st.stop()

        if limit_type == 'Theo Phạm Vi Trang':
            pdfReader = PyPDF2.PdfFileReader(BytesIO(uploaded_file.read()))
            num_pages = pdfReader.getNumPages()

            limit_range = st.slider("Chọn khoảng trang cần giới hạn trong tệp:", 1, num_pages, (1, num_pages))
            st.markdown(f"Trang: {limit_range[0]} - {limit_range[1]}")
            extra_prompt = f" Giới hạn nội dung trong tệp từ trang {limit_range[0]} đến trang {limit_range[1]}."

        elif limit_type == 'Theo Chương':
            chapters = st.text_area("Nhập số chương hoặc tiêu đề")
            if not chapters:
                st.warning("Vui lòng nhập ít nhất một số chương hoặc tiêu đề.")
                st.stop()
            extra_prompt = f" Giới hạn nội dung trong tệp ở chương {chapters}."

        prompt = prompt + extra_prompt
    prompt = prompt + " Cuối bài kiểm tra, thêm một phần mới để cung cấp câu trả lời đúng và giải thích chi tiết cho mỗi câu hỏi. Trích dẫn số trang trong tệp cho mỗi câu hỏi và trích dẫn văn bản, nội dung liên quan."
    # st.markdown(prompt)

    if st.button("Tạo bài kiểm tra"):
        print(prompt)
        request_gpt(uploaded_file, prompt, "test")
        