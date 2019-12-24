import pygame
from GOL import GameOfLife

def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()

def main():
    grid_w = 36
    grid_h = 26

    gol = GameOfLife(grid_w, grid_h)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN1 = (90, 150, 30)
    GREEN2 = (0, 61, 0)
    GREEN3 = (0, 102, 0)
    GREEN4 = (0, 153, 0)
    GREEN5 = (76, 153, 0)

    WIDTH = 20
    HEIGHT = 20
    MARGIN = 2

    pygame.init()
    WINDOW_SIZE = [grid_w * WIDTH + (grid_w + 1) * MARGIN, grid_h * HEIGHT + (grid_h + 1) * MARGIN + grid_h + 6]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Game of Life")
    info_text = pygame.font.SysFont("freesansbold.ttf", 20)

    done = False
    cells_selected = False
    clock = pygame.time.Clock()

    while not done:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cells_selected = False
                if event.key == pygame.K_SPACE:
                    cells_selected = True
                if event.key == pygame.K_r and not cells_selected:
                    gol.initialize_grid()
                if event.key == pygame.K_e and not cells_selected:
                    gol.empty_grid()

            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    try:
                        x = pos[1] // (HEIGHT + MARGIN)
                        y = pos[0] // (WIDTH + MARGIN)

                        if gol.grid[x][y] == 0:
                            gol.grid[x][y] = 1

                    except IndexError:
                        pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                try:
                    x = pos[1] // (HEIGHT + MARGIN)
                    y = pos[0] // (WIDTH + MARGIN)

                    if gol.grid[x][y] == 0:
                        gol.grid[x][y] = 1
                    else:
                        gol.grid[x][y] = 0

                except IndexError:
                    pass

        pygame.time.delay(100)

        for i in range(len(gol.grid)):
            for j in range(len(gol.grid[0])):
                color = WHITE

                if cells_selected:
                    if gol.grid[i][j] == 1:
                        if gol.neighbours(i, j) >= 4:
                            color = GREEN2
                        if gol.neighbours(i, j) == 3:
                            color = GREEN3
                        if gol.neighbours(i, j) == 2:
                            color = GREEN4
                        if gol.neighbours(i, j) == 1:
                            color = GREEN5
                else:
                    if gol.grid[i][j] == 1:
                        color = GREEN1

                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * j + MARGIN,
                                 (MARGIN + HEIGHT) * i + MARGIN, WIDTH, HEIGHT])

        if cells_selected:
            grid = gol.update_grid()
            percentage = round(gol.pct_of_living * 100)
            cells = gol.count

            text_surf, text_rect = text_objects(f"Number of cells: {cells}  ( {percentage} %)", info_text)
            text_rect.center = (((grid_w * (WIDTH + MARGIN)) // 2), ((HEIGHT + MARGIN) * grid_h) + (grid_h + 6) // 2)

        else:
            text_surf, text_rect = text_objects("Select cells that are alive <left mouse button> "
                                                ", random cells <R> or empty grid <E>", info_text)
            text_rect.center = (((grid_w * (WIDTH + MARGIN)) // 2), ((HEIGHT + MARGIN) * grid_h) + grid_h // 3)
            screen.blit(text_surf, text_rect)

            text_surf, text_rect = text_objects("Press <SPACE> to start the game and pause by pressing <ESC>",
                                                info_text)
            text_rect.center = (((grid_w * (WIDTH + MARGIN)) // 2), ((HEIGHT + MARGIN) * grid_h) + grid_h)
            
        screen.blit(text_surf, text_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
