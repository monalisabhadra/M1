import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Rolling Simulator 🎲")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (70, 130, 180)
BUTTON_HOVER_COLOR = (100, 160, 210)

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)

button_rect = pygame.Rect(WIDTH//2 - 75, HEIGHT//2 - 25, 150, 50)

def roll_dice():
    return random.randint(1, 6)

def draw_button(surface, rect, text, mouse_pos):
    color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(surface, color, rect, border_radius=8)
    txt_surf = font.render(text, True, WHITE)
    txt_rect = txt_surf.get_rect(center=rect.center)
    surface.blit(txt_surf, txt_rect)

def main():
    clock = pygame.time.Clock()
    result = None
    message = "Click 'Roll Dice' to start!"
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(WHITE)

        header = font.render("🎲 Dice Rolling Simulator 🎲", True, BLACK)
        screen.blit(header, (WIDTH//2 - header.get_width()//2, 20))

        if result is not None:
            res_text = font.render(f"You rolled a {result}!", True, BLACK)
        else:
            res_text = font.render(message, True, BLACK)
        screen.blit(res_text, (WIDTH//2 - res_text.get_width()//2, HEIGHT//2 - 80))

        draw_button(screen, button_rect, "Roll Dice", mouse_pos)

        instr = small_font.render("Press ESC or close window to quit", True, (100, 100, 100))
        screen.blit(instr, (WIDTH//2 - instr.get_width()//2, HEIGHT - 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    result = roll_dice()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()