import qrcode
import streamlit as st
from PIL import Image

# Function to create a QR Code
def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(
        fill_color="black", back_color="#fcbf30").convert('RGB')
    
    return qr_image

# Streamlit app
def main():
    st.set_page_config(page_title='QR Code Generator', page_icon='📱')

    st.title('QR Code Generator')

    data = st.text_input('Enter your Text/Link to convert into a QR Code:')
    
    if st.button('Convert'):
        if data:
            qr_image = create_qr_code(data)
            resized_image = qr_image.resize((450, 450))
            st.image(resized_image, caption='Generated QR Code',
                     use_column_width=True)
        else:
            st.error('Please enter text/link before converting.')

    if st.button('Reset'):
        reset()

# Function to reset session state
def reset():
    st.session_state.data = ""
    st.session_state.qr_image = None

if __name__ == '__main__':
    main()
