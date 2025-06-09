import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="YouTube para MP4", layout="centered")
st.title("🎬 Conversor de YouTube para MP4 (educacional)")

url = st.text_input("🔗 Cole a URL de um vídeo do YouTube")

output_dir = "videos"
os.makedirs(output_dir, exist_ok=True)

if st.button("⬇️ Baixar"):
    if not url:
        st.warning("Por favor, insira uma URL válida.")
    else:
        try:
            ydl_opts = {
                'format': 'bestvideo+bestaudio/best',
                'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.download([url])

            st.success("✅ Download concluído com sucesso!")
        except Exception as e:
            st.error(f"Erro durante o download: {e}")
