import pygame
import random

# Inisialisasi pygame
pygame.init()

# Lebar dan tinggi jendela permainan`
WIDTH = 800
HEIGHT = 600

# Warna yang digunakan dalam permainan
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Membuat jendela permainan
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce Game")

# Membuat pemain
player_width = 170
player_height = 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 2

# Membuat bola dan kecepatan bola
ball_radius = 10
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT // 2)
ball_speed_x = 0.6
ball_speed_y = 0.6


# Fungsi untuk menggambar pemain
def draw_player():
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_width, player_height))


# Fungsi untuk menggambar bola
def draw_ball():
    pygame.draw.circle(window, RED, (ball_x, ball_y), ball_radius)


# Fungsi untuk menggambar tombol
def draw_button(x, y, width, height, color, text):
    pygame.draw.rect(window, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    window.blit(text_surface, text_rect)


# Fungsi untuk memulai permainan
def start_game():
    global running
    running = True


# Fungsi untuk menampilkan menu awal
def show_menu():
    window.fill(WHITE)
    draw_button(300, 200, 200, 100, BLUE, "Start")
    pygame.display.update()


# Menampilkan menu awal
show_menu()

# Loop utama permainan
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 300 <= mouse_pos[0] <= 500 and 200 <= mouse_pos[1] <= 300:
                start_game()
                menu_running = False

# Loop permainan
while running:
    # Membersihkan jendela permainan
    window.fill(WHITE)

    # Memeriksa input pemain dan menggerakkan pemain
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Menggerakkan bola
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Memantulkan bola ketika mencapai batas jendela
    if ball_x < ball_radius or ball_x > WIDTH - ball_radius:
        ball_speed_x *= -1
    if ball_y < ball_radius:
        ball_speed_y *= -1

    # Memeriksa tabrakan antara bola dan pemain
    if ball_y + ball_radius > player_y and ball_x + ball_radius > player_x and ball_x - ball_radius < player_x + player_width:
        ball_speed_y *= -1

    # Memeriksa apakah bola jatuh ke bawah
    if ball_y > HEIGHT:
        running = False

    # Menggambar pemain dan bola
    draw_player()
    draw_ball()

    # Memperbarui tampilan
    pygame.display.update()

# Menutup jendela pygame
pygame.quit()