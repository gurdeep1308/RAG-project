# 🎓 AI Course Teaching Assistant (RAG)

An AI-powered teaching assistant built using **Retrieval Augmented Generation (RAG)** that helps users search and understand course videos.

The system converts video lectures into searchable knowledge by extracting transcripts, generating embeddings, retrieving relevant context, and answering questions using an LLM.

---

## 🚀 Features

- 🎥 Convert course videos into searchable content
- 🎙️ Automatic speech-to-text using Whisper
- 🧩 Transcript chunking with timestamps
- 🧠 Semantic embeddings using BGE-M3
- 🔍 Similarity-based retrieval using cosine similarity
- 🤖 LLM-powered answers using Llama 3.2 / GPT models
- ⏱️ Provides video number and timestamps for relevant topics
- 📚 Works on your own course data

---

## 🏗️ Architecture
Video Lectures
|
↓
Convert Video → MP3
|
↓
Whisper Transcription
|
↓
JSON Transcript Chunks
|
↓
BGE-M3 Embeddings
|
↓
Vector Similarity Search
|
↓
Relevant Context Retrieval
|
↓
LLM Response

---

## 📂 Project Structure
## 📂 Project Structure

RAG-project/

│── videos/
│   └── Course video files

│── audios/
│   └── Converted MP3 files

│── jsons/
│   └── Generated transcript chunks

│── video_to_mp3.py
│   └── Converts videos into MP3 audio files

│── mp3_to_json.py
│   └── Converts MP3 audio into timestamped JSON transcripts using Whisper

│── preprocessing_json.py
│   └── Generates BGE-M3 embeddings and saves vector data

│── process_incoming.py
│   └── Performs similarity search and generates LLM responses

│── stt.py
│   └── Experimental speech-to-text script

│── embeddings.joblib
│   └── Stored embeddings database

│── README.md
│   └── Documentation

## ⚙️ How it works

### 1. Add videos

Place course videos inside:

videos/

---

### 2. Convert videos to audio

Run:

python video_to_mp3.py

---

### 3. Generate transcript chunks

Run:

python mp3_to_json.py

This creates JSON files containing:

- video number
- title
- timestamp
- transcript text

---

### 4. Create embeddings

Run:

python preprocessing_json.py

This generates:

embeddings.joblib

containing:

- chunk id
- transcript text
- BGE-M3 vector embeddings

---

### 5. Ask questions

Run:

python process_incoming.py

Example:

Ask a Question:
Where is HTML audio tag explained?

The assistant retrieves relevant video chunks and answers with:

- video number
- timestamp
- explanation