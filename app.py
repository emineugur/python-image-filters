import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io


st.set_page_config(
    page_title="Görüntüyü Gri Formata Dönüştürücü",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_image(image_file):
    img = Image.open(image_file)
    return img


def convert_to_grayscale(img):
    img_array = np.array(img)

    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        return img.convert("L")
    else:
        return img


def apply_filter(img, filter_type, intensity=1.0):
    img_array = np.array(img)

    if filter_type == "Bulanıklaştırma":
        kernel_size = int(intensity * 5)
        if kernel_size % 2 == 0:
            kernel_size += 1

        filtered_img = cv2.GaussianBlur(
            img_array, (kernel_size, kernel_size), 0
        )

    elif filter_type == "Keskinleştirme":
        kernel = np.array([
            [-1, -1, -1],
            [-1,  9, -1],
            [-1, -1, -1]
        ]) * intensity

        filtered_img = cv2.filter2D(img_array, -1, kernel)

    elif filter_type == "Kenar Algılama":
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array

        edges = cv2.Canny(gray, int(50 * intensity), int(150 * intensity))
        filtered_img = edges

    elif filter_type == "Negatif":
        filtered_img = 255 - img_array

    else:
        filtered_img = img_array

    filtered_img = np.clip(filtered_img, 0, 255).astype(np.uint8)

    if len(filtered_img.shape) == 2:
        return Image.fromarray(filtered_img, mode="L")
    else:
        return Image.fromarray(filtered_img)


def add_custom_css():
    st.markdown("""
    <style>
        .main-header{
            font-size:2.5rem;
            color:#4527A0;
            text-align:center;
            margin-bottom:1rem;
        }
        .sub-header{
            font-size:1.5rem;
            color:#5E35B1;
            margin-top:1rem;
            margin-bottom:0.5rem;
        }
        .info-text{
            font-size:1rem;
            color:#333;
            margin-bottom:1rem;
        }
        .stButton>button{
            background-color:#5E35B1;
            color:white;
            font-weight:bold;
            border-radius:5px;
            padding:0.5rem 1rem;
            border:none;
        }
        .stButton>button:hover{
            background-color:#4527A0;
        }
    </style>
    """, unsafe_allow_html=True)


def sidebar_content():
    st.sidebar.title("Hakkında")
    st.sidebar.info(
        "Bu uygulama bir resmi gri renge dönüştürmek için tasarlanmıştır. "
        "Amacımız görüntü işleme konusunda bilgilerimizi pekiştirmektir."
    )

    st.sidebar.title("Nasıl Kullanılır?")
    st.sidebar.markdown("""
    1-) Sol taraftaki 'Bir görüntü yükleyin' butonuna tıklayınız  
    2-) Bilgisayarınızdan bir görüntü seçiniz (JPG, JPEG, PNG)  
    3-) İşlem türünü seçiniz  
    4-) Filtre uygulayabilirsiniz  
    5-) Görüntüyü indirebilirsiniz  
    """)

    st.sidebar.title("Görüntü İşleme Hakkında")
    st.sidebar.markdown("""
    **Gri Formata Dönüştürme:**  
    Renkli bir görüntüyü tek kanallı gri tona çevirir.

    **Filtreler:**  
    - Bulanıklaştırma  
    - Keskinleştirme  
    - Kenar Algılama  
    - Negatif
    """)


def main():
    add_custom_css()
    sidebar_content()

    st.markdown(
        '<h1 class="main-header">Görüntüyü Gri Formata Dönüştürücü</h1>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<p class="info-text">Bu uygulama yüklediğiniz görüntüyü gri formata dönüştürür ve filtre uygular.</p>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader(
            "Bir görüntü yükleyiniz",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_file is not None:
            image = load_image(uploaded_file)
            st.image(image, caption="Orijinal Görüntü", use_column_width=True)

            img_array = np.array(image)
            st.write(f"Boyut: {img_array.shape[1]} x {img_array.shape[0]}")

            process_option = st.radio(
                "İşlem Türü",
                [
                    "Sadece Gri Formata Dönüştür",
                    "Gri Formata Dönüştür ve Filtre Uygula",
                    "Sadece Filtre Uygula"
                ]
            )

            filter_type = None
            intensity = 1.0

            if "Filtre" in process_option:
                filter_type = st.selectbox(
                    "Filtre Türü",
                    ["Bulanıklaştırma", "Keskinleştirme", "Kenar Algılama", "Negatif"]
                )
                intensity = st.slider(
                    "Filtre Yoğunluğu", 0.1, 2.0, 1.0, 0.1
                )

            if st.button("İşlemi Başlat"):
                if process_option == "Sadece Gri Formata Dönüştür":
                    processed_image = convert_to_grayscale(image)
                elif process_option == "Gri Formata Dönüştür ve Filtre Uygula":
                    gray = convert_to_grayscale(image)
                    processed_image = apply_filter(gray, filter_type, intensity)
                else:
                    processed_image = apply_filter(image, filter_type, intensity)

                with col2:
                    st.image(
                        processed_image,
                        caption="İşlenmiş Görüntü",
                        use_column_width=True
                    )

                    buf = io.BytesIO()
                    processed_image.save(buf, format="PNG")

                    st.download_button(
                        "Görüntüyü İndir",
                        buf.getvalue(),
                        file_name="processed_image.png",
                        mime="image/png"
                    )
        else:
            st.info("Lütfen bir görüntü yükleyiniz.")



main()

         
                                                                          