# 🎙️ Transcripto

A simple Streamlit app that transcribes videos into text using OpenAI’s **Whisper** model.

🌐 **[Live Demo on Streamlit Cloud](https://transcripto12.streamlit.app/)**

---

## ✨ Features

* 🎥 Upload video files (`.mp4`, `.avi`, `.mov`, `.mkv`)
* 🔊 Automatic audio extraction with **ffmpeg**
* 🧠 Transcribe speech into text using **Whisper**
* ⏱️ Accurate timestamps in `hh:mm:ss.ms` format
* 📥 Download transcription as:

  * `.txt` (plain text)
  * `.docx` (Word document)
  * `.pdf` (Portable Document Format)
  
* Deployed free on Streamlit Cloud

---

## 🚀 How to Use

### 🔗 Online (Recommended)

1. Open the app 👉 [Live Demo](https://transcripto12.streamlit.app/)
2. Upload your video file
3. Select a Whisper model size (`tiny` → `large`)
4. Wait for transcription to finish
5. Download your transcript in the desired format

---

### 💻 Run Locally

#### 1. Clone repo

```bash
git clone https://github.com/fns12/Transcripto.git
cd transcripto
```

#### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Make sure ffmpeg is installed

* **Linux/macOS**:

  ```bash
  sudo apt-get install ffmpeg
  ```
* **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

#### 5. Run the app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
transcripto/
│── app.py              # Main Streamlit app
│── requirements.txt    # Python dependencies
│── packages.txt        # System packages (for Streamlit Cloud, includes ffmpeg)
│── runtime.txt         # Python runtime version (for Streamlit Cloud)
│── README.md           # Documentation
```

---



---

## 📝 Example Output

```
[00:00:01.200 → 00:00:03.450] Hello everyone, welcome to this session.
[00:00:04.000 → 00:00:06.150] Today we will be testing transcription.
```

---

## 📜 License

MIT License. Free to use and modify.

