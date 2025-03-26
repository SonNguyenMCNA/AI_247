import streamlit as st
from io import BytesIO
from base import request_gpt, chat_completion

st.set_page_config(
    page_title="Article Extraction", 
    page_icon="🤖",
)

st.write("# Article Extraction 📝")

source = st.selectbox(
    "Chọn loại tài liệu:",
    ("File", "Link Web"),
    index=None
)

if not source:
    st.stop()

if source == "File":
    uploaded_file = st.file_uploader("Upload file", accept_multiple_files=True)
    if not uploaded_file:
        st.stop()
    
    prompt = 'Từ bài báo, hãy tổng hợp các biến độc lập được sử dụng để xây dựng mô hình. Kết quả bắt buộc phải theo định dạng sau: Tên biến, Mô tả, Công thức. Lưu ý tất cả kết quả trả ra bắt buộc phải ở dạng bảng.'

    if st.button("Trích xuất"):
        print(prompt)
        request_gpt(uploaded_file, prompt, 'gpt-4o-mini')

elif source == "Link Web":
    link = st.text_input("Điền link của bài báo:")

    if not link:
        st.stop()

    prompt = f'Từ bài báo tại link sau: "{link}", hãy tổng hợp các biến độc lập được sử dụng để xây dựng mô hình. Kết quả bắt buộc phải theo định dạng sau: Tên biến, Mô tả, Công thức. Lưu ý tất cả kết quả trả ra bắt buộc phải ở dạng bảng.'

    if st.button("Trích xuất"):
        print(prompt)
        chat_completion('gpt-4o-mini-search-preview', prompt)


# lịnk = st.text_input("Điền đường dẫn của bài báo:")

# if not lịnk:
#     st.stop()


