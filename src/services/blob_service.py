from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config


def upload_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION_STRING
        )
        blob_client = blob_service_client.get_blob_client(
            Config.CONTAINER_NAME, file_name
        )
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.write(f'Erro ao enviar arquivo: {e}')
        return None
