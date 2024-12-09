
# PyPlayer - Player de Áudio com Interface Gráfica

O **PyPlayer** é um player de áudio simples desenvolvido com Python e a biblioteca Tkinter. Ele permite ao usuário carregar arquivos MP3, visualizar a capa do álbum (caso esteja presente), e controlar a reprodução da música com funcionalidades como tocar, pausar, continuar e parar. Além disso, é possível ajustar o volume da música.

## Funcionalidades

- Carregar arquivos de áudio no formato MP3
- Exibir a capa do álbum (se disponível nos metadados do MP3)
- Controlar a reprodução da música:
  - Tocar
  - Pausar/Continuar
  - Parar
- Ajustar o volume da música
- Interface gráfica simples e intuitiva

## Tecnologias Utilizadas

- Python
- Tkinter (para a interface gráfica)
- Pygame (para a reprodução de áudio)
- Mutagen (para ler os metadados do arquivo MP3 e extrair a capa do álbum)
- Pillow (para manipulação de imagens)

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado em seu computador. Para instalar as bibliotecas necessárias, execute:

```bash
pip install pygame mutagen pillow
```

### Executando o Projeto

1. Clone o repositório para seu computador:

```bash
git clone https://github.com/caioreis29974/PyPlayer.git
```

2. Navegue até a pasta do projeto e execute o script `main.py`:

```bash
python player.py
```

A interface gráfica será aberta e você poderá carregar suas músicas e controlá-las diretamente.

## Como Usar

1. **Abrir Música**: Clique no botão "Abrir Música" para selecionar um arquivo MP3 de sua escolha.
2. **Reprodução**: Use os botões de "Tocar", "Pausar", "Parar" e "Continuar" para controlar a reprodução da música.
3. **Ajuste de Volume**: Use o controle deslizante para ajustar o volume da música.

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções no código! Se você encontrar algum problema ou tiver sugestões, por favor, abra uma **issue** ou envie um **pull request**.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
