import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card


def configure_interface():
    st.title('Upload de Arquivo DIO - Desafio 1 - Azure - Fake Docs')
    uploaded_file = st.file_uploader(
        'Escolha um arquivo', type=['png', 'jpg', 'jpeg']
    )

    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f'Arquivo {fileName} enviado com sucesso!')
            credit_card_info = analyze_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write('Erro ao enviar arquivo!')


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem enviada', use_column_width=True)
    st.write('Resultado da validação:')
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(
            '<h1 style="color: green;">Cartão Válido</h1>',
            unsafe_allow_html=True
        )
        st.write(f'Nome: {credit_card_info["card_name"]}')
        st.write(f'Data de validade: {credit_card_info["expiry_date"]}')
    else:
        st.markdown(
            '<h1 style="color: red;">Cartão Inválido</h1>',
            unsafe_allow_html=True
        )
        st.write('Não foi possível identificar as informações do cartão')


if __name__ == '__main__':
    configure_interface()
