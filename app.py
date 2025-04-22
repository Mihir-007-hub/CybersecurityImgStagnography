import streamlit as st
from PIL import Image
from stego_utils import encode_text_to_image, decode_text_from_image
import io

st.set_page_config(page_title="🕵️‍♂️ Steganography Tool", layout="centered")

st.title("🖼️ Text Steganography - Hide & Reveal Messages in Images")

tab1, tab2 = st.tabs(["🔐 Encode", "🔎 Decode"])

with tab1:
    st.header("🔐 Hide a message inside an image")
    uploaded_image = st.file_uploader("Upload a PNG image", type=["png"])
    secret_text = st.text_area("Enter the secret message you want to hide")

    if uploaded_image and secret_text:
        img = Image.open(uploaded_image)
        encoded_img = encode_text_to_image(img, secret_text)

        st.image(encoded_img, caption="Preview of encoded image", use_column_width=True)

        buf = io.BytesIO()
        encoded_img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        st.download_button("📥 Download Encoded Image", data=byte_im, file_name="encoded_image.png", mime="image/png")

with tab2:
    st.header("🔎 Reveal a hidden message from an image")
    encoded_img_file = st.file_uploader("Upload an encoded PNG image", type=["png"], key="decode")

    if encoded_img_file:
        img = Image.open(encoded_img_file)
        message = decode_text_from_image(img)
        st.success("✅ Hidden message found:")
        st.code(message)
