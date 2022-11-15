import pygame

pygame.init()

# Game Settings
monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_characteristcs = {
    "sky": {
        "color": (135, 206, 235)
    },
    "grass": {
        "color": (0,255,0),
        "position": {
            "y": 0.8 * monitor_display[1]
        }
    }
}

# Game Logic
game_running_flag = True

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running_flag = False
            
    if not game_running_flag:
        pygame.quit()
        
        break
    
    game_display.fill(game_characteristcs["sky"]["color"])
    
    #Create grass.
    pygame.draw.rect(game_display, game_characteristcs["grass"]["color"], pygame.Rect(0, game_characteristcs["grass"]["position"]["y"], monitor_display[0], monitor_display[1] - game_characteristcs["grass"]["position"]["y"]))
    #Left @ 15:43 https://utrgv.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c0e56256-e3f0-459b-ae0f-af4901319aba
    #Running Game Mechanics
    pygame.display.update()
    
    system_clock.tick(30)