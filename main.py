import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

player_x = 100
player_y = 100
player_size = 50
player_speed = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed * dt
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= player_speed * dt
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += player_speed * dt
        
        
    if player_x < 0:
        player_x = 0
    if player_x > 800 - player_size:
        player_x = 800 - player_size
    if player_y < 0:
        player_y = 0
    if player_y > 600 - player_size:
        player_y = 600 - player_size
        
    

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))
    pygame.display.flip()

pygame.quit()
    
        
    
    

