from numpy import square
import numpy as np
import pygame
from ball import ball
from peg import peg

pygame.init()
screen = pygame.display.set_mode((720, 1280))
clock = pygame.time.Clock()
running = True

dt = 0

peg_group = pygame.sprite.Group()

def mkboard(pos, levels):
    x_off, y_off = 0, 0
    shift = 64

    for i in range(levels):
        peg_group.add(peg(pos=(pos[0] +x_off, 100 + y_off)))
        for j in range(2 * i + 1):
            peg_group.add(peg(pos=(pos[0] + x_off - shift * j, 100 + y_off)))
        x_off += shift
        y_off += shift

    for i in range(5):
        off = 45 if i % 2 == 0 else 10
        for j in range(12):
            peg_group.add(peg(pos=(off + shift * j, 100 + y_off)))
        y_off += 64
    
    x_off = 0

    for i in range(levels * 2):
        peg_group.add(peg(pos=(pos[0] +x_off, 100 + y_off)))
        for j in range(2 * i + 1):
            peg_group.add(peg(pos=(pos[0] + x_off - shift * j, 100 + y_off)))
        x_off += shift
        y_off += shift


if __name__ == "__main__":
    ball_group = pygame.sprite.Group()


    #    ball_group.add(ball(screen.get_rect().center))
    mkboard(screen.get_rect().center , 6)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                ball_group.add(ball(pos))

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        ball_group.draw(screen)
        peg_group.draw(screen)
        
        ball_group.update(dt)

        
        for ent in ball_group:
            for col in pygame.sprite.spritecollide(ent, peg_group, False, collided=pygame.sprite.collide_circle):
                ent.col(col.rect.center)
            for col in pygame.sprite.spritecollide(ent, ball_group, False, collided=pygame.sprite.collide_circle):
                if ent != col:
                    ent.ballcol(col)
            if not screen.get_rect().collidepoint(ent.rect.center):
                ent.kill()

            
        
        # for col in pygame.sprite.groupcollide(ball_group, peg_group, False, False, collided=pygame.sprite.collide_circle):
            
        #     col.col(np.array(pygame.sprite.spritecollide(col, peg_group, False, collided=pygame.sprite.collide_circle).rect.center))

        
        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
    
