# === IDEA ===
# Import and Configuration
import pygame
import random
from pygame.locals import *

pygame.init()

# Display configuration
size = (640, 480)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
pygame.display.set_caption('Poke-A-Mole')


# Entities
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/Mole-2.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound('media/hop.wav')  # soundbible.com
        self.rect.left = random.randint(0, 620)
        self.rect.top = random.randint(0, 460)

    def flee(self):
        self.rect.left = random.randint(0, 620)
        self.rect.top = random.randint(0, 460)

    def cry(self):
        self.sound.play()

    def hit(self, pos):
        return self.rect.collidepoint(pos)


class Stick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('media/stick.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


mole = Mole()
stick = Stick()

sprite_group = pygame.sprite.Group()
sprite_group.add(mole)
sprite_group.add(stick)

background = pygame.image.load('media/grass.png')  # Rasen
background = pygame.transform.scale(background, size)

background_hit = pygame.Surface(size)
background_hit = background_hit.convert()
background_hit.fill((255, 0, 0))

font = pygame.font.Font(None, 25)

# Action ---> === ALTER ===
# Assign Variables
keepGoing = True
count = 0
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT, 200)
# Loop


while keepGoing:
    ## Timer
    clock.tick(30)

    ## Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif event.type == MOUSEBUTTONDOWN:
            if mole.hit(pygame.mouse.get_pos()):
                mole.cry()
                mole.flee()
                count += 1
                screen.blit(background_hit, (0, 0))
                break
        elif event.type == USEREVENT:
            mole.flee()
            pygame.time.set_timer(USEREVENT, 1000)  # TODO: Zeit zufällig machen
            screen.blit(background, (0, 0))
            sprite_group.update()
            sprite_group.draw(screen)
            text = font.render(u'Maulwürfe ' + str(count), True, Color('white'))  # TODO: on top of the screen
            screen.blit(text, (10, 230))

    ## ReDisplay

    # x, y = pygame.mouse.get_pos()

    pygame.display.flip()
