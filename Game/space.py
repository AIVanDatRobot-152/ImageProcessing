import pygame
import math
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Star color
BLUE = (0, 0, 255)      # Planet color
RED = (255, 0, 0)       # Secondary planet color

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Universe Simulation")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Star class
class Star:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

# Planet class
class Planet:
    def __init__(self, orbit_center, orbit_radius, orbit_speed, size, color):
        self.orbit_center = orbit_center
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.size = size
        self.color = color
        self.angle = random.uniform(0, 2 * math.pi)  # Random starting angle

    def update(self):
        self.angle += self.orbit_speed

    def draw(self):
        x = self.orbit_center[0] + int(self.orbit_radius * math.cos(self.angle))
        y = self.orbit_center[1] + int(self.orbit_radius * math.sin(self.angle))
        pygame.draw.circle(screen, self.color, (x, y), self.size)

# Create stars and planets
star = Star(WIDTH // 2, HEIGHT // 2, 20)
planets = [
    Planet((WIDTH // 2, HEIGHT // 2), 100, 0.02, 10, BLUE),
    Planet((WIDTH // 2, HEIGHT // 2), 150, 0.01, 8, RED),
    Planet((WIDTH // 2, HEIGHT // 2), 200, 0.005, 6, BLUE)
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update planets
    for planet in planets:
        planet.update()

    # Draw everything
    screen.fill(BLACK)
    star.draw()
    for planet in planets:
        planet.draw()

    # Refresh display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
