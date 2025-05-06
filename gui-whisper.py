import os
import logging
import tkinter as tk
from tkinter import filedialog
from faster_whisper import WhisperModel

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def format_timestamp(seconds):
    seconds = int(seconds)
    h, remainder = divmod(seconds, 3600)
    m, s = divmod(remainder, 60)
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"

def main():
    # Initialize hidden Tk root
    root = tk.Tk()
    root.withdraw()

    # Ask user to pick an audio file
    audio_file = filedialog.askopenfilename(
        title="Select an audio file to transcribe",
        filetypes=[("Audio files", "*.mp3 *.wav *.flac *.m4a"), ("All files", "*.*")]
    )
    if not audio_file:
        logging.info("No file selected. Exiting.")
        return

    base, _ = os.path.splitext(audio_file)
    output_file = f"{base}.txt"

    logging.info("Loading Whisper model (large-v2, int8)...")
    model = WhisperModel("large-v2", compute_type="int8")

    logging.info("Transcribing…")
    segments, info = model.transcribe(audio_file, beam_size=5, best_of=5)
    logging.info("Transcription done. Writing output…")

    with open(output_file, "w", encoding="utf-8") as f:
        for seg in segments:
            ts = f"{format_timestamp(seg.start)} → {format_timestamp(seg.end)}"
            f.write(f"{ts}: {seg.text}\n")

    logging.info("Saved transcript to %s", output_file)

if __name__ == "__main__":
    main()
