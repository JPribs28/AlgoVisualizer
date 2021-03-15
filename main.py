import pygame 


# Initialiaze pygame modules
pygame.init()

# Set dimensions and initialize window
WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Frames per second
FPS = 30

# Color variables
WHITE = (250, 250, 250)

# Draw and update window
def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

# Main game loop
def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
    
    pygame.quit()


if __name__ == "__main__":
    main()