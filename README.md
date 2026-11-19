# 🎙️ VoxScript AI

### AI-Powered Speech-to-Text Application

VoxScript AI is an AI-powered speech recognition application built using **OpenAI Whisper, Python, PyTorch, and Streamlit**.

It converts audio recordings into text using Automatic Speech Recognition (ASR) and supports multiple languages.

## 📸 Application Screenshots

### Dashboard

![VoxScript AI Dashboard](assets/voxscript-dashboard.png)

### Transcription Result

![Transcription Result](assets/Transcription%20result.png)

## ✨ Features

- 🎙️ Audio-to-text transcription
- 🌍 Multilingual speech recognition
- 🔍 Automatic language detection
- 🎧 Audio file preview
- 📝 Transcription results display
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

## 🧠 AI Model

**OpenAI Whisper – Base Model**

Whisper is a multilingual automatic speech recognition model developed by OpenAI.

This project uses the Base model to recognize speech and generate text transcriptions.

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

## 📂 Project Structure

```text
VoxScript-AI/
│
├── assets/
│   ├── Transcription result.png
│   └── voxscript-dashboard.png
│
├── outputs/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
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

Install FFmpeg and make sure it is added to your system PATH.

### 7. Run the Application

```bash
streamlit run app.py
```

## 📌 Learning Outcomes

Through this project, I learned:

- Fundamentals of Automatic Speech Recognition (ASR).
- How AI models recognize human speech.
- Integrating OpenAI Whisper with Python.
- Audio processing using FFmpeg.
- Using PyTorch-based speech recognition models.
- Building interactive applications using Streamlit.
- Handling audio uploads and transcription results.

## ⚠️ Current Limitations

- Transcription accuracy depends on audio quality and language.
- Tamil transcription accuracy with the Base model needs further improvement.
- Processing speed depends on system hardware.

## 👨‍💻 Developer

**Vignesh U**

- GitHub: [21vicky](https://github.com/21vicky)

## 📅 30 Days 30 AI Projects

**Day 13 – VoxScript AI**

Turning speech into text with Artificial Intelligence. 🚀