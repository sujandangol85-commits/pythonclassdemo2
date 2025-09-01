import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Player
player_size = 50
player = pygame.Rect(WIDTH // 2, HEIGHT - player_size - 10, player_size, player_size)
player_speed = 7

# Bullets
bullets = []
bullet_speed = -10

# Obstacles
obstacles = []
obstacle_speed = 4
spawn_obstacle_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_obstacle_event, 1000)

# Coins
coins = []
coin_speed = 4
spawn_coin_event = pygame.USEREVENT + 2
pygame.time.set_timer(spawn_coin_event, 3000)

# Score and difficulty
score = 0
level = 1

font = pygame.font.SysFont("Arial", 24)

def draw_window():
    screen.fill(BLACK)
    
    # Draw player
    pygame.draw.rect(screen, GREEN, player)
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    
    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, RED, obs)
    
    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, YELLOW, (coin.centerx, coin.centery), coin.width // 2)
    
    # Draw score
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()

def game_over():
    over_text = font.render("GAME OVER! Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(over_text, (WIDTH // 2 - 200, HEIGHT // 2))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    global bullets, obstacles, coins, score, level, obstacle_speed
    
    bullets = []
    obstacles = []
    coins = []
    score = 0
    level = 1
    obstacle_speed = 4
    player.x = WIDTH // 2
    
    running = True
    while running:
        clock.tick(60)  # 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == spawn_obstacle_event:
                obs = pygame.Rect(random.randint(0, WIDTH-40), -40, 40, 40)
                obstacles.append(obs)
            if event.type == spawn_coin_event:
                coin = pygame.Rect(random.randint(0, WIDTH-20), -20, 20, 20)
                coins.append(coin)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(player.centerx-5, player.top-10, 10, 20)
                    bullets.append(bullet)
        
        # Keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed
        
        # Move bullets
        for bullet in bullets[:]:
            bullet.y += bullet_speed
            if bullet.bottom < 0:
                bullets.remove(bullet)
        
        # Move obstacles
        for obs in obstacles[:]:
            obs.y += obstacle_speed
            if obs.top > HEIGHT:
                obstacles.remove(obs)
            if player.colliderect(obs):
                game_over()
            for bullet in bullets[:]:
                if bullet.colliderect(obs):
                    obstacles.remove(obs)
                    bullets.remove(bullet)
                    score += 10
        
        # Move coins
        for coin in coins[:]:
            coin.y += coin_speed
            if coin.top > HEIGHT:
                coins.remove(coin)
            if player.colliderect(coin):
                coins.remove(coin)
                score += 5
        
        # Increase difficulty
        if score // 50 >= level:
            level += 1
            obstacle_speed += 1
        
        draw_window()

if __name__ == "__main__":
    main()
