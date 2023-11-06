"""
Foodie

Description:
"""
# Import libraries
import random
# import tsk
import pygame

pygame.init()

# Create the window
w = pygame.display.set_mode([500, 500])

# Create the components


food = pygame.Rect(random.randint(90, 480), random.randint(0, 480), 20, 20)

# Game Intrduction
print("Welcome to my game! I didn't create this game just so you can have fun but also to test your eyesight :)")
print()
print()
print("How to play: ")
print("Player 1 controls: wasd")
print("Player 2 controls: Arrow Keys")
print(
    "All you have to do is kill your opponent and in order to kill your opponent, you have to be 3 times bigger than him")

# variables
num = 5
run = True
p1x = 20
p1y = 250
p2x = 85
p2y = 250
p1_size = 10
p2_size = 10

# Game loop
while run:
    w.fill((255, 255, 255))

    # Close the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        p2y -= 0.5
    if keys[pygame.K_DOWN]:
        p2y += 0.5
    if keys[pygame.K_LEFT]:
        p2x -= 0.5
    if keys[pygame.K_RIGHT]:
        p2x += 0.5

    if keys[pygame.K_w]:
        p1y -= 0.5
    if keys[pygame.K_s]:
        p1y += 0.5
    if keys[pygame.K_a]:
        p1x -= 0.5
    if keys[pygame.K_d]:
        p1x += 0.5

    # Draw the components
    pygame.draw.ellipse(w, (240, 240, 240), food)
    pygame.draw.circle(w, (255, 0, 0), (p1x, p1y), p1_size)
    pygame.draw.circle(w, (0, 255, 0), (p2x, p2y), p2_size)

    # detect food collision
    if p1x + 25 > food.x and p1x - 25 < food.x:
        if p1y + 25 > food.y and p1y - 25 < food.y:
            p1_size += 5
            food.x = random.randint(0, 480)
            food.y = random.randint(0, 480)

    if p2x + 25 > food.x and p2x - 25 < food.x:
        if p2y + 25 > food.y and p2y - 25 < food.y:
            p2_size += 5
            food.x = random.randint(0, 480)
            food.y = random.randint(0, 480)

    # Kill each other
    if p1_size > p2_size + 3:
        if p1x + 25 > p2x and p1x - 25 < p2x:
            if p1y + 25 > p2y and p1y - 25 < p2y:
                w.fill((0, 0, 0))
                print()
                print()
                print("Player 1 won")
                print("GAMEOVER")
                run = False

    if p2_size > p1_size + 3:
        if p2x + 25 > p1x and p2x - 25 < p1x:
            if p2y + 25 > p1y and p2y - 25 < p1y:
                w.fill((0, 0, 0))
                print()
                print()
                print("Player 2 won")
                print("GAMEOVER")
                run = False

    pygame.display.flip()
