import streamlit as st
import ffmpeg
import subprocess
import whisper
import tempfile
import os
from io import BytesIO
from docx import Document
from reportlab.pdfgen import canvas

st.title("🎙️Transcripto")
st.subheader("Upload a video and get the transcription")

# Helper: Convert video to audio
def video_to_audio(video_path, audio_path="output.wav"):
    stream = ffmpeg.input(video_path)
    stream = ffmpeg.output(stream, audio_path)
    ffmpeg.run(stream, overwrite_output=True)
    return audio_path

# Cache Whisper model
@st.cache_resource
def get_audio_model():
    model = whisper.load_model("base")  # tiny/base/small/medium/large
    return model

# Transcribe audio
def transcribe_audio(audio_path):
    model = get_audio_model()
    result = model.transcribe(audio_path)
    return result

# File generator for download
def download_file(transcription, base_filename, format_choice):
    if format_choice == "TXT":
        return transcription, f"{base_filename}_transcription.txt", "text/plain"

    elif format_choice == "DOCX":
        buffer = BytesIO()
        doc = Document()
        doc.add_heading("Transcription", 0)
        doc.add_paragraph(transcription)
        doc.save(buffer)
        buffer.seek(0)
        return buffer, f"{base_filename}_transcription.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"

    elif format_choice == "PDF":
        buffer = BytesIO()
        c = canvas.Canvas(buffer)
        textobject = c.beginText(40, 800)
        for line in transcription.split("\n"):
            textobject.textLine(line)
        c.drawText(textobject)
        c.save()
        buffer.seek(0)
        return buffer, f"{base_filename}_transcription.pdf", "application/pdf"


# File uploader
uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"])

if uploaded_video:
    # Save uploaded video to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_video.read())
        video_path = tmp_file.name

    # Convert video to audio
    audio_path = "audio.wav"
    video_to_audio(video_path, audio_path)

    # Run transcription
    with st.spinner("Transcribing..."):
        result = transcribe_audio(audio_path)

    # Display transcription
    transcription = "\n".join([seg["text"] for seg in result["segments"]])
    for seg in result["segments"]:
        start = round(seg["start"], 2)
        end = round(seg["end"], 2)
        text = seg["text"]
        st.markdown(f"**[{start} → {end}]** {text}")

    # Format choice + download button
    format_choice = st.radio("Choose download format:", ["TXT", "DOCX", "PDF"])
    base_filename = os.path.splitext(os.path.basename(video_path))[0]

    file_data, file_name, mime = download_file(transcription, base_filename, format_choice)
    st.download_button(
        label=f"📥 Download {format_choice}",
        data=file_data,
        file_name=file_name,
        mime=mime
    )

    # Cleanup temp files
    os.remove(video_path)
    if os.path.exists(audio_path):
        os.remove(audio_path)