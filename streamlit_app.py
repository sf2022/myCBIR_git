import cv2
import numpy as np
import streamlit as st
from PIL import Image
from retrieval import image_retrieval


def retrieval_page_show():
    """
    检索页面
    :return: void
    """
    st.sidebar.title('CBIR')
    st.sidebar.write('----------------')
    uploaded_file = st.sidebar.file_uploader("上传图片", type="jpg")
    if uploaded_file is not None:
        # 将传入的文件转为Opencv格式
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        # 展示原图片
        # st.write("待检索图片:", uploaded_file.name)
        # imgClass = uploaded_file.name[:-15]
        # st.write("图片所属的类:", imgClass)

        st.image(opencv_image, width=300, channels="BGR")

    number = st.sidebar.number_input('检索结果数量：', min_value=1, max_value=100, step=1)

    start_retrieval_btn = st.sidebar.button("开始检索")
    if start_retrieval_btn and uploaded_file:
        start_retrieval(opencv_image, number)


# 检索
def start_retrieval(opencv_image, limit):
    resultData = image_retrieval(opencv_image, limit)
    # 取出检索结果中图片的路径
    image_paths_list = [data["imgPath"] for data in resultData]
    # 一行显示4张图片
    for i in range(0, limit, 4):
        images_in_row = 4
        row = st.columns(images_in_row)
        for j in range(images_in_row):
            if j + i >= len(image_paths_list):
                break
            image_path = image_paths_list[i + j]
            image = Image.open(image_path)
            with row[j]:
                st.image(image, use_column_width=True)


if __name__ == "__main__":
    retrieval_page_show()
