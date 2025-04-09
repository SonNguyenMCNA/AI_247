import streamlit as st

st.set_page_config(
    page_title="Quant Retail AI",
    page_icon="🤖",
)

st.write("# Quant Retail AI 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    #### Giới thiệu: 
    -    Bản Beta Quant Retail AI được xây dựng với mục đích thử nghiệm.
    -    Các chức năng hiện có:
            + Tạo bài kiểm tra từ tài liệu.
            + Trích xuất thông tin từ bài báo.
            \n
    #### Hướng dẫn sử dụng:\n
    - B1: Chọn chức năng muốn sử dụng
    - B2: Upload file hoặc điền thông tin theo chức năng từ máy tính/điện thoại
    - B3: Ấn nút gửi yêu cầu và kết quả sẽ được in lên màn hình\n
    Powered by: OpenAI, Streamlit
"""
)

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )
