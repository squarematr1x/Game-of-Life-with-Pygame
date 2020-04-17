import pygame
from GOL import GameOfLife
from Colors import Colors

def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()

def main():
    grid_w = 36
    grid_h = 26

    gol = GameOfLife(grid_w, grid_h)
    colors = Colors()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    COLORS = colors.get_colors()

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
                if event.key == pygame.K_c:
                    colors.change_colors()
                    COLORS = colors.get_colors()

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

        for i in range(len(gol.grid)):
            for j in range(len(gol.grid[0])):
                color = WHITE

                if cells_selected:
                    if gol.grid[i][j] == 1:
                        if gol.neighbours(i, j) >= 4:
                            color = COLORS[1]
                        if gol.neighbours(i, j) == 3:
                            color = COLORS[2]
                        if gol.neighbours(i, j) == 2:
                            color = COLORS[3]
                        if gol.neighbours(i, j) == 1:
                            color = COLORS[4]
                else:
                    if gol.grid[i][j] == 1:
                        color = COLORS[0]

                pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * j + MARGIN,
                                 (MARGIN + HEIGHT) * i + MARGIN, WIDTH, HEIGHT])

        if cells_selected:
            pygame.time.delay(80)
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

            text_surf, text_rect = text_objects("Press <SPACE> to start the game,pause by pressing <ESC> and change colors with <C>",
                                                info_text)
            text_rect.center = (((grid_w * (WIDTH + MARGIN)) // 2), ((HEIGHT + MARGIN) * grid_h) + grid_h)
            
        screen.blit(text_surf, text_rect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()
