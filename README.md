# 🎙️ VoxScript AI

### AI-Powered Speech-to-Text Application

VoxScript AI is a speech recognition application built using OpenAI Whisper and Streamlit. It converts audio recordings into text using AI-powered speech recognition and supports multiple languages.

## ✨ Features

- 🎙️ Audio-to-text transcription
- 🌍 Multilingual speech recognition
- 🔍 Automatic language detection
- 🎧 Audio file preview
- 📝 Transcription results
- 📊 Word and character count
- 📥 Download transcripts as TXT files
- 🌙 Modern dark-themed interface

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenAI Whisper | Speech recognition |
| PyTorch | Deep learning framework |
| Streamlit | Web application interface |
| FFmpeg | Audio processing |

## 🌍 Supported Languages

- English
- Tamil
- Hindi
- Telugu
- Malayalam
- Kannada
- French
- Spanish
- German
- Japanese
- Korean
- Arabic

## ⚙️ How It Works

1. User uploads an audio file.
2. The application processes the audio using FFmpeg.
3. OpenAI Whisper analyzes the audio.
4. Speech is converted into text.
5. The application displays the transcription.
6. Users can download the generated transcript.

## 🔄 Project Workflow

```text
        START
          |
          v
    Upload Audio File
          |
          v
     Audio Preview
          |
          v
    Select Language
          |
          v
    Load Whisper Model
          |
          v
     Audio Processing
       (FFmpeg)
          |
          v
   Whisper Recognition
          |
          v
   Speech-to-Text
          |
          v
 Display Transcription
          |
          v
  Word & Character Count
          |
          v
   Download TXT File
          |
          v
         END
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/21vicky/VoxScript-AI.git
```

### 2. Navigate to the Project

```bash
cd VoxScript-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install FFmpeg

Install FFmpeg and ensure it is available in your system PATH.

### 7. Run the Application

```bash
streamlit run app.py
```

## 📂 Project Structure

```text
VoxScript-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│
└── outputs/
```

## 🧠 AI Model

**OpenAI Whisper – Base Model**

Whisper is a multilingual automatic speech recognition model developed by OpenAI.

This project uses the Base model for audio transcription.

## 📌 Learning Outcomes

Through this project, I learned:

- Fundamentals of speech recognition.
- How automatic speech recognition (ASR) works.
- How to integrate OpenAI Whisper with Python.
- Audio processing using FFmpeg.
- Building interactive applications using Streamlit.
- Handling audio uploads and transcription results.

## ⚠️ Current Limitations

- Transcription accuracy depends on audio quality and language.
- Tamil transcription with the Base model needs further improvement.
- Processing speed depends on the system's hardware.

## 👨‍💻 Developer

**Vignesh U**

GitHub: [21vicky](https://github.com/21vicky)

## 📅 30 Days 30 AI Projects

**Day 13 – VoxScript AI**

Turning speech into text with Artificial Intelligence.