import streamlit as st
from io import BytesIO
from base import request_gpt, chat_completion

st.set_page_config(
    page_title="Article Extraction", 
    page_icon="🤖",
)

st.write("# Feature Extraction 📝")

st.markdown(
    """
### Hướng dẫn sử dụng công cụ trích xuất Feature từ tài liệu:

##### Bước 1: Chọn loại dữ liệu đầu vào
Người dùng lựa chọn hình thức đầu vào phù hợp với nhu cầu:
- Tải lên tệp tài liệu (định dạng PDF, DOCX). 
- Nhập đường link website chứa nội dung cần trích xuất

##### Bước 2: Cung cấp nội dung đầu vào
- Nếu chọn tệp, nhấn nút “Browse files” để chọn và tải lên tài liệu từ thiết bị. Lưu ý chỉ nên sử dụng các tài liệu có độ dài dưới 20 trang để đảm bảo hệ thống xử lý nhanh và chính xác.
- Nếu chọn link web, dán đường dẫn vào ô nhập tương ứng.

##### Bước 3: Trích xuất thông tin đặc trưng
Sau khi cung cấp đầu vào, nhấn nút “Trích xuất” để hệ thống tiến hành phân tích nội dung và tự động xác định các biến độc lập có liên quan đến mô hình hóa. Sau đó kết quả sẽ được hiển thị trên màn hình dưới dạng bảng.
"""
)

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
    
    prompt = 'Từ bài báo, hãy tổng hợp các biến độc lập được sử dụng để xây dựng mô hình. Kết quả bắt buộc phải theo định dạng sau: Tên biến, Mô tả, Công thức, Ý nghĩa kinh tế kỳ vọng (có mối quan hệ cùng chiều hay ngược chiều với biến phụ thuộc), Nguồn (bài báo nào, trang bao nhiêu, trích dẫn). Lưu ý tất cả kết quả trả ra bắt buộc phải ở dạng bảng. Bắt buộc phải tổng hợp đầy đủ tất cả các biến, không được bỏ sót biến nào.'

    if st.button("Trích xuất"):
        print(prompt)
        request_gpt(uploaded_file, prompt, 'gpt-4o-mini')

elif source == "Link Web":
    link = st.text_input("Điền link của bài báo:")

    if not link:
        st.stop()

    prompt = f'Từ bài báo tại link sau: "{link}", hãy tổng hợp các biến độc lập được sử dụng để xây dựng mô hình. Kết quả bắt buộc phải theo định dạng sau: Tên biến, Mô tả, Công thức, Ý nghĩa kinh tế kỳ vọng (có mối quan hệ cùng chiều hay ngược chiều với biến phụ thuộc), Nguồn (bài báo nào, trang bao nhiêu, trích dẫn). Lưu ý tất cả kết quả trả ra bắt buộc phải ở dạng bảng. Bắt buộc phải tổng hợp đầy đủ tất cả các biến, không được bỏ sót biến nào.'

    if st.button("Trích xuất"):
        print(prompt)
        chat_completion('gpt-4o-search-preview', prompt)


# lịnk = st.text_input("Điền đường dẫn của bài báo:")

# if not lịnk:
#     st.stop()


