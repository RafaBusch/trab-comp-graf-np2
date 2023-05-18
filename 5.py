import pygame
import librosa

# Inicialização do Pygame
pygame.init()

# Configurações da janela
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dançando com a Música")

# Carregando a música
music_file = "musica.mp3"
pygame.mixer.music.load(music_file)

# Carregando a imagem do boneco
boneco_image = pygame.image.load("boneco.png")
boneco_rect = boneco_image.get_rect()
boneco_rect.center = (window_width // 2, window_height // 2)

# Definindo a velocidade do boneco
velocidade = 5

# Análise do áudio
audio, sr = librosa.load(music_file)
onset_frames = librosa.onset.onset_detect(y=audio, sr=sr)
onset_times = librosa.frames_to_time(onset_frames, sr=sr)
onset_index = 0

# Iniciando a reprodução da música
pygame.mixer.music.play()

# Loop principal do jogo
running = True
clock = pygame.time.Clock()

while running:
    # Verificação de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar se há um novo onset (início de um trecho rítmico)
    if onset_index < len(onset_times) and pygame.mixer.music.get_pos() / 1000 >= onset_times[onset_index]:
        # Atualizar o movimento do boneco
        boneco_rect.x += velocidade
        if boneco_rect.left < 0 or boneco_rect.right > window_width:
            velocidade *= -1  # Inverter a direção do movimento

        onset_index += 1

    # Limpeza da tela
    window.fill((0, 0, 0))

    # Desenhar o boneco na tela
    window.blit(boneco_image, boneco_rect)

    # Atualização da tela
    pygame.display.flip()

    # Definir a velocidade de atualização da tela
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
