import subprocess

def mkv_to_mp3(input_file: str, output_file: str):
    """
    Extrai o áudio de um arquivo MKV e salva como MP3 usando ffmpeg.
    É necessário ter o ffmpeg instalado no sistema.
    """
    command = [
        "ffmpeg",
        "-i", input_file,   # arquivo de entrada
        "-q:a", "0",        # qualidade máxima de áudio
        "-map", "a",        # seleciona apenas a trilha de áudio
        output_file
    ]

    subprocess.run(command, check=True)
    print(f"Áudio exportado com sucesso para: {output_file}")

# Exemplo de uso


input_file = "C:\\Users\\slaa\\Videos\\2025-09-19 10-29-49\\2025-09-19-10-29-49.mkv"
output_file = "C:\\Users\\slaa\\Videos\\2025-09-19 10-29-49\\2025-09-19-10-29-49.mp3"


mkv_to_mp3(input_file,output_file)
