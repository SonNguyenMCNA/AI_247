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
    uploaded_file = st.file_uploader("Upload file", accept_multiple_files=True)

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

    prompt = f"From the input file, generate a test with {num_question} questions of type {question_type} with difficulty level {difficulty}."

    prompt = prompt + " At the end of the test, add a new section to provide the correct answer and detailed explanation for each question. Also refer to the page number in the file for each question and quote the relevant text."

    model_ai = st.selectbox(
        "Choose a model:",
        ("gpt-4o-mini", "gpt-3.5-turbo"),
        index=None
    )

    if not model_ai:
        st.stop()

    # st.markdown(prompt)

    if st.button("Generate Exam"):
        print(prompt)
        request_gpt(uploaded_file, prompt, "test", model_ai)
        

elif language == "Tiếng Việt":
    uploaded_file = st.file_uploader("Tải lên tệp", accept_multiple_files=True) 

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
    

    prompt = f"Từ tệp đầu vào, tạo bài kiểm tra với {num_question} câu hỏi loại {question_type} với mức độ {difficulty}."

    prompt = prompt + " Cuối bài kiểm tra, thêm một phần mới để cung cấp câu trả lời đúng và giải thích chi tiết cho mỗi câu hỏi. Trích dẫn số trang trong tệp cho mỗi câu hỏi và trích dẫn văn bản, nội dung liên quan."
    # st.markdown(prompt)

    model_ai = st.selectbox(
        "Chọn model:",
        ("gpt-4o-mini", "gpt-3.5-turbo"),
        index=None
    )

    if not model_ai:
        st.stop()

    # st.markdown(prompt)

    if st.button("Tạo bài kiểm tra"):
        print(prompt)
        request_gpt(uploaded_file, prompt, "test", model_ai)