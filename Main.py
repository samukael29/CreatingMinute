from pathlib import Path
import subprocess
import os
import whisper


def mkv_to_mp3(directory: str, filename: str):
    """
    Extrai o áudio de um arquivo MKV e salva como MP3 usando ffmpeg.
    É necessário ter o ffmpeg instalado no sistema.
    """

    inputfile = os.path.join(directory,  filename + "." + 'mvk')
    outputfile = os.path.join(directory,  filename + "." + 'mp3')

    if os.path.isfile(inputfile):
        print(f"The file '{inputfile}' exists.")
    else:
        print(f"The file '{inputfile}' does not exist or is not a regular file.")

    command = [
        "ffmpeg",
        "-i", inputfile,   # arquivo de entrada
        "-q:a", "0",        # qualidade máxima de áudio
        "-map", "a",        # seleciona apenas a trilha de áudio
        outputfile
    ]

    subprocess.run(command, check=True)
    print(f"Áudio exportado com sucesso para: {outputfile}")



def transcribe_mp3_to_text(directory: str, filename: str):
    """
    Transcribes an MP3 audio file to text using OpenAI's Whisper model.

    Args:
        mp3_file_path (str): The path to the MP3 audio file.

    Returns:
        str: The transcribed text from the audio file.
    """
    inputfile = os.path.join(directory,  filename + "." + 'mp3')
    outputfile = os.path.join(directory,  filename + "." + 'txt')

    
    try:
        # Load the Whisper model (e.g., 'base', 'small', 'medium', 'large')
        # 'base' is a good starting point for general use.
        model = whisper.load_model("base")

        # Transcribe the audio file
        result = model.transcribe(inputfile)

        transcribed_text = result["text"]


        # Save the transcription to a text file
        with open(outputfile, "w", encoding="utf-8") as f:
            f.write(transcribed_text)

        print(f"Transcription saved to {outputfile}")


        # Extract and return the transcribed text
        return result["text"]
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None


placedfiledirectory = "C:\Users\Samuel\Phyton Projects\Arquivos"
file = "2025-09-19-17-06-01"


mkv_to_mp3(placedfiledirectory,file)

transcribe_mp3_to_text(placedfiledirectory,file)
