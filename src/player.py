import tkinter as tk
from tkinter import filedialog
import pygame
import time

pygame.mixer.init()

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Áudio", "*.mp3 *.wav")])
    if arquivo:
        pygame.mixer.music.load(arquivo)
        nome_arquivo.set(arquivo.split('/')[-1])

def tocar_audio():
    pygame.mixer.music.play()
    atualizar_progresso()

def pausar_audio():
    pygame.mixer.music.pause()

def continuar_audio():
    pygame.mixer.music.unpause()

def parar_audio():
    pygame.mixer.music.stop()

def ajustar_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

def atualizar_progresso():
    if pygame.mixer.music.get_busy():
        current_pos = pygame.mixer.music.get_pos() / 1000
        progresso.set(current_pos)
        tempo_atual.config(text=f"{current_pos:.2f}s")
        janela.after(1000, atualizar_progresso)

janela = tk.Tk()
janela.title("PyPlayer")

nome_arquivo = tk.StringVar()
progresso = tk.DoubleVar()

frame = tk.Frame(janela)
frame.pack(pady=10)

label_nome = tk.Label(frame, text="Arquivo de Áudio: ")
label_nome.grid(row=0, column=0, padx=10)

label_nome_arquivo = tk.Label(frame, textvariable=nome_arquivo)
label_nome_arquivo.grid(row=0, column=1, padx=10)

btn_abrir = tk.Button(janela, text="Abrir", command=abrir_arquivo)
btn_abrir.pack(pady=5)

btn_tocar = tk.Button(janela, text="Tocar", command=tocar_audio)
btn_tocar.pack(pady=5)

btn_pausar = tk.Button(janela, text="Pausar", command=pausar_audio)
btn_pausar.pack(pady=5)

btn_continuar = tk.Button(janela, text="Continuar", command=continuar_audio)
btn_continuar.pack(pady=5)

btn_parar = tk.Button(janela, text="Parar", command=parar_audio)
btn_parar.pack(pady=5)

volume_slider = tk.Scale(janela, from_=0, to=100, orient="horizontal", label="Volume", command=ajustar_volume)
volume_slider.set(100)
volume_slider.pack(pady=10)

progress_bar = tk.Scale(janela, from_=0, to=100, orient="horizontal", variable=progresso, state="disabled")
progress_bar.pack(pady=5)

tempo_atual = tk.Label(janela, text="0.00s")
tempo_atual.pack()

janela.mainloop()