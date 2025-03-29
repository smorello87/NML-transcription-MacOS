# Audio Transcription Tool

A simple desktop application that transcribes audio files into text using the [faster-whisper](https://github.com/guillaumekln/faster-whisper) library. The tool features a graphical user interface (GUI) built with Tkinter, allowing users to easily select audio files and generate transcriptions with timestamps.

---

## Features

- **GUI-Based Interface:** User-friendly interface built with Tkinter for selecting audio files.
- **Audio Transcription:** Transcribes audio files using the Whisper model (large-v2) from the faster-whisper library.
- **Timestamped Output:** Transcription output includes formatted timestamps (HH:MM:SS or MM:SS) for each segment.
- **Multi-threaded Processing:** Transcription is executed in a separate thread to prevent the UI from freezing.
- **Supported Audio Formats:** Works with popular audio file formats like MP3, WAV, M4A, FLAC, OGG, AAC, and OPUS.

---

## Requirements

- Python 3.7+
- [faster-whisper](https://github.com/guillaumekln/faster-whisper)
- Tkinter (usually comes pre-installed with Python)
- Other standard libraries: `os`, `logging`, `threading`

> **Note:** The Whisper model used is configured to run on CPU with int8 computation. Adjust the model settings if you have a GPU or different performance needs.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/audio-transcription-tool.git
   cd audio-transcription-tool
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the Required Dependencies:**

   ```bash
   pip install faster-whisper
   ```

   If you encounter any issues with `tkinter`, refer to your operating system's installation guides.

---

## Usage

1. **Run the Application:**

   ```bash
   python transcription_tool.py
   ```

2. **Select an Audio File:**
   
   - Click the "Select Audio File" button.
   - Choose an audio file from the dialog (supported formats: MP3, WAV, M4A, FLAC, OGG, AAC, OPUS).

3. **Transcription Process:**

   - The application initializes the Whisper model.
   - The audio file is transcribed, and timestamps are added.
   - Once complete, the transcription is saved in a text file with the same name as the audio file.

4. **Output:**

   - The transcription file is saved in the same directory as the audio file.
   - A success message is displayed upon completion.

---

## How to Compile the App

### What You Need to Compile It

- A Mac computer with Python 3.9 (or later) installed.
- An internet connection (to install PyInstaller).

### How to Compile the App

Follow these steps:

1. **Download the Files:**

   - Save the `transcription_tool.py` file to a folder on your computer.

2. **Open Terminal:**

   - Open the Terminal application (you can find it in Applications > Utilities).

3. **Navigate to Your Folder:**

   - In Terminal, type `cd ` (with a space after) and then drag and drop the folder containing `transcription_tool.py` into the Terminal window. Press **Enter**.

4. **Install PyInstaller:**

   - In the Terminal, type:
     ```bash
     pip install pyinstaller
     ```
     This will install PyInstaller, which is used to create a standalone app.

5. **Create the Standalone App:**

   - In the Terminal, type:
     ```bash
     pyinstaller --windowed transcription_tool.py
     ```
     This command tells PyInstaller to package the tool as an application without showing a command-line window.

6. **Find Your App:**

   - After the build process finishes, open the folder named `dist` inside your current folder.
   - Inside `dist`, you will see an application called **transcription_tool**.

7. **Run the App:**

   - Double-click on **transcription_tool** to launch the application.
   - A window will appear allowing you to select an audio file. Follow the on-screen instructions to transcribe your audio file.

---

## Code Overview

- **`format_timestamp(seconds)`**: Converts seconds to HH:MM:SS or MM:SS format.
- **`transcribe_audio(audio_file, status_label)`**: Handles the transcription process, including model initialization, transcription, and saving the output.
- **`choose_file()`**: Opens a file dialog for selecting an audio file and starts the transcription in a separate thread.
- **GUI Setup:** Creates the main window, buttons, and status label.

---

## Troubleshooting

- **No File Selected Error:** Ensure you choose a valid audio file.
- **Model Initialization Errors:** Check that the faster-whisper library is installed correctly and that your system supports CPU-based inference.
- **Tkinter Issues:** Verify that your Python installation includes Tkinter. On some systems, it may need to be installed separately.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [faster-whisper](https://github.com/guillaumekln/faster-whisper) for providing an efficient implementation of the Whisper transcription model.
- Python and the Tkinter community for making GUI development accessible.

---

Feel free to contribute, raise issues, or fork the repository to improve the tool!
