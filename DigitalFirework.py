import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Digital Fireworks")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(colors)
        self.explosion_radius = random.randint(50, 150)
        self.exploded = False
        self.particles = []

    def explode(self):
        for _ in range(100):
            angle = random.uniform(0, 2 * 3.1416)
            speed = random.uniform(2, 8)
            particle = {
                'x': self.x,
                'y': self.y,
                'vx': speed * pygame.math.Vector2(math.cos(angle), math.sin(angle)).x,
                'vy': speed * pygame.math.Vector2(math.cos(angle), math.sin(angle)).y,

                'color': self.color,
                'life': random.randint(10, 50)
            }
            self.particles.append(particle)
        self.exploded = True

# Main loop
clock = pygame.time.Clock()
fireworks = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Create new fireworks
    if random.randint(0, 100) < 5:
        fireworks.append(Firework(random.randint(0, width), height))

    # Update and draw fireworks
    screen.fill(black)
    for firework in fireworks:
        pygame.draw.circle(screen, firework.color, (firework.x, firework.y), 5)
        firework.y -= 5
        if firework.y < firework.explosion_radius and not firework.exploded:
            firework.explode()

    # Update and draw particles
    for firework in fireworks:
        if firework.exploded:
            for particle in firework.particles:
                pygame.draw.circle(screen, particle['color'], (int(particle['x']), int(particle['y'])), 2)
                particle['x'] += particle['vx']
                particle['y'] += particle['vy']
                particle['life'] -= 1
                if particle['life'] <= 0:
                    firework.particles.remove(particle)

    pygame.display.flip()
    clock.tick(30)
