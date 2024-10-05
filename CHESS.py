import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (106, 90, 205)
GREEN = (34, 139, 34)

# Create the display window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')

# Draw the chess board
def draw_board(win):
    win.fill(WHITE)
    colors = [WHITE, BLUE]
    for row in range(ROWS):
        for col in range(COLS):
            color = colors[(row + col) % 2]
            pygame.draw.rect(win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Place pieces on the board using text
def draw_pieces(win, board):
    font = pygame.font.SysFont('Arial', 40)  # Use a font for the piece text
    for row in range(ROWS):
        for col in range(COLS):
            piece = board[row][col]
            if piece != "--":
                piece_label = font.render(piece, True, GREEN if piece[0] == 'w' else BLACK)
                win.blit(piece_label, (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + 10))

# Create initial board setup
def create_board():
    return [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    ]

# Main game loop
def main():
    board = create_board()  # Chess board with pieces
    running = True

    while running:
        draw_board(window)  # Draw the chessboard
        draw_pieces(window, board)  # Draw chess pieces on the board

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
