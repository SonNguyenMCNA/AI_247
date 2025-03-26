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
    
    prompt = 'Từ bài báo, hãy tóm tắt nội dung chính của bài báo. Tóm tắt ngắn gọn vào kết quả bắt buộc phải theo định dạng sau: Tiêu đề, Tác giả, Ngày xuất bản, URL, Giọng điệu, Tóm tắt. Lưu ý tất cả kết quả trả ra bắt buộc phải ở dạng bảng (kể cả phần Tóm tắt). Tác giả phải là người viết bài báo, chứ không phải là chủ của file được tải lên. Ngày xuất bản phải ở định dạng dd/mm/yyyy.'

    if st.button("Trích xuất"):
        print(prompt)
        request_gpt(uploaded_file, prompt, 'gpt-4o-mini')

elif source == "Link Web":
    link = st.text_input("Điền link của bài báo:")

    if not link:
        st.stop()

    prompt = f'Từ bài báo tại link sau: "{link}", hãy tóm tắt nội dung chính của bài báo. Tóm tắt ngắn gọn vào kết quả bắt buộc phải theo định dạng sau: Tiêu đề, Tác giả, Ngày xuất bản, URL, Giọng điệu, Tóm tắt. Lưu ý tất cả kết quả trả ra bắt buộc phải ở dạng bảng (kể cả phần Tóm tắt). Tác giả phải là người viết bài báo, chứ không phải là chủ của file được tải lên. Ngày xuất bản phải ở định dạng dd/mm/yyyy.'

    if st.button("Trích xuất"):
        print(prompt)
        chat_completion('gpt-4o-mini-search-preview', prompt)


# lịnk = st.text_input("Điền đường dẫn của bài báo:")

# if not lịnk:
#     st.stop()


