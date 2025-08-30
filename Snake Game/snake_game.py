import pygame

pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((250, 250, 30, 30))
speed = 5  # 🔥 control character speed

clock = pygame.time.Clock()
run = True

while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    # Key inputs
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-speed, 0)
    if key[pygame.K_d]:
        player.move_ip(speed, 0)
    if key[pygame.K_w]:
        player.move_ip(0, -speed)
    if key[pygame.K_s]:
        player.move_ip(0, speed)

    # Prevent player from leaving screen
    if player.left < 0:
        player.left = 0
    if player.right > screen_width:
        player.right = screen_width
    if player.top < 0:
        player.top = 0
    if player.bottom > screen_height:
        player.bottom = screen_height

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(120) #limits fps, so slower speed
pygame.quit()
