import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Menentukan ukuran layar
screen_size = 300
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption('Tic Tac Toe')

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Garis grid
line_color = BLACK
line_width = 15

# Ukuran sel grid
cell_size = screen_size // 3

# Permukaan untuk menggambar X dan O
x_surface = pygame.Surface((cell_size, cell_size))
o_surface = pygame.Surface((cell_size, cell_size))

# Font
font = pygame.font.Font(None, 150)

# Pemain saat ini
current_player = 'X'

# Papan permainan (3x3)
board = [['' for _ in range(3)] for _ in range(3)]

# Menentukan posisi yang menang
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Menggambar garis grid
def draw_grid():
    for x in range(1, 3):
        pygame.draw.line(screen, line_color, (x * cell_size, 0), (x * cell_size, screen_size), line_width)
        pygame.draw.line(screen, line_color, (0, x * cell_size), (screen_size, x * cell_size), line_width)

# Menggambar X atau O
def draw_markers():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                x_surface.fill(WHITE)
                pygame.draw.line(x_surface, RED, (0, 0), (cell_size, cell_size), line_width)
                pygame.draw.line(x_surface, RED, (0, cell_size), (cell_size, 0), line_width)
                screen.blit(x_surface, (col * cell_size, row * cell_size))
            elif board[row][col] == 'O':
                o_surface.fill(WHITE)
                pygame.draw.circle(o_surface, BLUE, (cell_size // 2, cell_size // 2), cell_size // 2, line_width)
                screen.blit(o_surface, (col * cell_size, row * cell_size))

# Loop utama permainan
running = True
winner = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            x, y = event.pos
            row = y // cell_size
            col = x // cell_size
            if board[row][col] == '':
                board[row][col] = current_player
                winner = check_winner()
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'

    # Mengisi layar dengan warna putih
    screen.fill(WHITE)

    # Menggambar garis grid
    draw_grid()

    # Menggambar X dan O
    draw_markers()

    if winner:
        text = font.render(winner + ' wins!', True, BLACK)
        screen.blit(text, (screen_size // 10, screen_size // 2 - font.get_height() // 2))

    # Memperbarui tampilan layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
sys.exit()
