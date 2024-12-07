import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

pygame.mixer.init()

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")])
    if arquivo:
        pygame.mixer.music.load(arquivo)
        nome_arquivo.set(arquivo.split('/')[-1])

def tocar_audio():
    try:
        if pygame.mixer.music.get_pos() == -1:  # Se o áudio nunca foi iniciado
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.unpause()  # Retomar a música se pausada
    except pygame.error:
        messagebox.showerror("Erro", "Nenhum arquivo foi carregado!")

def alternar_pausar_continuar():
    if pygame.mixer.music.get_pos() > 0:  # Se o áudio está pausado ou tocando
        if pygame.mixer.music.get_busy():  # Está tocando
            pygame.mixer.music.pause()
        else:  # Está pausado
            pygame.mixer.music.unpause()
    else:
        messagebox.showerror("Erro", "Nenhuma música está tocando no momento!")

def parar_audio():
    pygame.mixer.music.stop()

def ajustar_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

janela = tk.Tk()
janela.title("PyPlayer")
janela.geometry("800x800")
janela.config(bg="#121212")

nome_arquivo = tk.StringVar()
nome_arquivo.set("Nenhum arquivo carregado")

cor_botao = "#5C1DFF"
cor_primaria = "#7C4DFF"
cor_secundaria = "#BB86FC"
cor_texto = "#FFFFFF"
cor_neutra = "#2A2A2A"

header = tk.Frame(janela, bg="#121212", height=100)
header.pack(fill="x")

frame_capa = tk.Frame(janela, bg="#121212")
frame_capa.pack(pady=30)

capa_placeholder = tk.Label(frame_capa, text="Capa do Álbum", bg="#2A2A2A", fg=cor_texto, width=30, height=15)
capa_placeholder.pack()

frame_nome = tk.Frame(janela, bg="#121212")
frame_nome.pack(pady=10)

nome_musica = tk.Label(frame_nome, textvariable=nome_arquivo, bg="#121212", fg=cor_secundaria, font=("Arial", 14, "bold"))
nome_musica.pack()

frame_controles = tk.Frame(janela, bg="#121212")
frame_controles.pack(pady=20)

btn_voltar = tk.Button(frame_controles, text="⏮", command=lambda: None, bg=cor_botao, fg=cor_texto, font=("Arial", 12), width=5, relief="flat")
btn_voltar.grid(row=0, column=0, padx=5)

btn_tocar = tk.Button(frame_controles, text="tocar", command=tocar_audio, bg=cor_primaria, fg=cor_texto, font=("Arial", 12), width=5, relief="flat")
btn_tocar.grid(row=0, column=1, padx=5)

btn_pausar = tk.Button(frame_controles, text="⏸", command=alternar_pausar_continuar, bg=cor_secundaria, fg=cor_texto, font=("Arial", 12), width=5, relief="flat")
btn_pausar.grid(row=0, column=2, padx=5)

btn_parar = tk.Button(frame_controles, text="parar", command=parar_audio, bg=cor_primaria, fg=cor_texto, font=("Arial", 12), width=5, relief="flat")
btn_parar.grid(row=0, column=3, padx=5)

btn_avancar = tk.Button(frame_controles, text="⏯", command=lambda: None, bg=cor_botao, fg=cor_texto, font=("Arial", 12), width=5, relief="flat")
btn_avancar.grid(row=0, column=4, padx=5)

frame_volume = tk.Frame(janela, bg="#121212")
frame_volume.pack(pady=20)

volume_slider = tk.Scale(frame_volume, from_=0, to=100, orient="horizontal", label="Volume", command=ajustar_volume, bg="#121212", fg=cor_texto, highlightbackground="#121212", troughcolor="#2A2A2A", sliderlength=20, length=300)
volume_slider.set(100)
volume_slider.pack()

frame_abertura = tk.Frame(janela, bg="#121212")
frame_abertura.pack(pady=20)

btn_abrir = tk.Button(frame_abertura, text="Abrir Música", command=abrir_arquivo, bg=cor_primaria, fg=cor_texto, font=("Arial", 12), width=20, relief="flat")
btn_abrir.pack()

janela.mainloop()