import pygame 


# Initialiaze pygame modules
pygame.init()

# Set dimensions and initialize window
WIDTH, HEIGHT = 1100, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Color variables
WHITE = (250, 250, 250)
GREY = (100, 100, 100)
RED = (255, 50, 50)
BLUE = (50, 50, 255)

# Frames per second
FPS = 30

# List of bar heights
BAR_HEIGHTS = [num for num in range(1, 501)]

# Bar dimension and location constants
BAR_WIDTH = 2
BAR_FROM_TOP = 550 
BAR_FROM_LEFT = 50 


# Draw bars at random before being sorted
def draw_bars():
    for i in range(len(BAR_HEIGHTS)):
        pygame.draw.rect(WIN, GREY, pygame.Rect(BAR_FROM_LEFT + BAR_WIDTH * i, BAR_FROM_TOP - BAR_HEIGHTS[i], BAR_WIDTH, BAR_HEIGHTS[i]))

    pygame.display.update()


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
        draw_bars()
    
    pygame.quit()


if __name__ == "__main__":
    main()