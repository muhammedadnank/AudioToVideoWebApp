# Audio to Video WebApp 🎧🎥

A premium Django web application that converts audio files (MP3, WAV, etc.) into MP4 videos with a sleek black background. It also supports extracting audio from existing videos to create a clean, black-screen version.

## Features ✨

- **MP3 to MP4 Conversion**: Transform any audio file into a video instantly.
- **Video to Black-Screen**: Extract audio and replace the visual track with a minimalist black background.
- **Premium UI**: Modern dark-mode "glassmorphism" design built with Tailwind CSS.
- **Persistent Storage**: Integrated with Render's persistent disks to save your processed files.
- **Supabase Powered**: Uses Supabase PostgreSQL for robust, remote data management.
- **Production Ready**: Fully configured with Gunicorn and WhiteNoise for high performance.

## Tech Stack 🛠️

- **Backend**: Django (Python)
- **Media Processing**: MoviePy
- **Database**: Supabase (PostgreSQL)
- **Frontend**: Tailwind CSS
- **Deployment**: Render

## Local Setup 💻

1. **Clone the repository**:
   ```bash
   git clone https://github.com/muhammedadnank/AudioToVideoWebApp
   cd AudioToVideoWebApp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the server**:
   ```bash
   python manage.py runserver
   ```

## Deployment Guide 🚀

### 1. Supabase Setup
- Create a project on [Supabase.com](https://supabase.com/).
- Copy your **Connection String (URI)** from Project Settings > Database.

### 2. Render Deployment
- Go to [Render](https://render.com/) and create a new **Blueprint**.
- Connect this repository.
- Provide the following environment variables when prompted:
  - `DATABASE_URL`: Your Supabase connection string.
  - `SECRET_KEY`: A unique random string.
  - `DEBUG`: `False`.
- Render will automatically set up the web service and a persistent disk for your media.

## License 📄
Developed as an open-source tool for easy audio-visual processing.
