import streamlit as st
from pytube import YouTube
import os

st.set_page_config(page_title="Conversor YouTube → MP4")

st.title("🎬 Conversor YouTube → MP4 (educacional)")
st.markdown("Cole o link de um vídeo educacional livre de direitos autorais.")

url = st.text_input("🔗 URL do vídeo")

download_path = "videos_baixados"
os.makedirs(download_path, exist_ok=True)

if st.button("⬇️ Baixar"):
    if not url:
        st.warning("Por favor, insira uma URL válida.")
    else:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            st.info(f"🎥 Baixando: {yt.title}")
            stream.download(output_path=download_path)
            st.success(f"✅ Download concluído: {yt.title}")
        except Exception as e:
            st.error(f"Erro: {e}")
