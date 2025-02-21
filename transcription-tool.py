import os
import logging
import tkinter as tk
from tkinter import filedialog, messagebox
from faster_whisper import WhisperModel
from threading import Thread

# Fix for OpenMP conflict (prevents crashing)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more verbosity
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def format_timestamp(seconds):
    """Convert seconds to HH:MM:SS format (or MM:SS if under an hour)."""
    seconds = int(seconds)
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    else:
        return f"{m:02d}:{s:02d}"

def transcribe_audio(audio_file, status_label):
    """Handles the transcription process in a separate thread."""
    if not audio_file:
        messagebox.showerror("Error", "No file selected!")
        return

    base, _ = os.path.splitext(audio_file)
    output_file = f"{base}.txt"

    try:
        status_label.config(text="Initializing Whisper model...")
        root.update_idletasks()

        model = WhisperModel("large-v2", device="cpu", compute_type="int8")

        status_label.config(text="Transcribing...")
        root.update_idletasks()

        segments, _ = model.transcribe(audio_file, beam_size=5, best_of=5)

        status_label.config(text="Saving transcription...")
        root.update_idletasks()

        with open(output_file, "w") as f:
            for seg in segments:
                start_formatted = format_timestamp(seg.start)
                end_formatted = format_timestamp(seg.end)
                line = f"{start_formatted} - {end_formatted}: {seg.text}"
                f.write(line + "\n")

        messagebox.showinfo("Success", f"Transcription saved as:\n{output_file}")
        status_label.config(text="Transcription complete!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        status_label.config(text="Error in transcription.")

def choose_file():
    """Opens file dialog to choose an audio file."""
    file_path = filedialog.askopenfilename(
        title="Select an Audio File",
        filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg *.aac *.opus")]
    )

    if file_path:
        status_label.config(text=f"Selected file: {os.path.basename(file_path)}")
        root.update_idletasks()

        # Run transcription in a separate thread (prevents UI freezing)
        transcription_thread = Thread(target=transcribe_audio, args=(file_path, status_label), daemon=True)
        transcription_thread.start()

# Create GUI
root = tk.Tk()
root.title("Audio Transcription Tool")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

btn_choose_file = tk.Button(frame, text="Select Audio File", command=choose_file, font=("Arial", 12))
btn_choose_file.pack()

status_label = tk.Label(root, text="No file selected.", font=("Arial", 10))
status_label.pack(pady=10)

root.mainloop()
