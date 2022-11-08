import pygame, random
WIDTH = 1080
HEIGHT = 720
BLACK = (0,0,0)
WHITE = (255,255,255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()


def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
pygame.init()

screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
done = False
score = 0
coin_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

for i in range(50):
    coin = Coin()
    coin.rect.x = random.randrange(1080)
    coin.rect.y = random.randrange(720)

    coin_list.add(coin)
    all_sprite_list.add(coin)

fondo = pygame.image.load("galaxia.png").convert()
x = 0

player = Player()
all_sprite_list.add(player)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(fondo, (x, 0))
    x = 1
    mouse_pos = pygame.mouse.get_pos()
    player.rect.x = mouse_pos[0]
    player.rect.y = mouse_pos[1]

    coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)

    for coin in coin_hit_list:
        score += 10
        print(score)


    all_sprite_list.draw(screen)

    draw_text(screen, str(score), 25, WIDTH // 2, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
