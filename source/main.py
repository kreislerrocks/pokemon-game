import pygame, sys
pygame.init()
class Screen(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
 
size = width, height = 768, 576
screen = pygame.display.set_mode(size)
screen.fill([0, 0, 0])
cursor = 1
startscreen = Screen('pokelogotest.jpg', [64,64])
game = Screen('name2.png', [screen.get_width() / 2 - 148, 300])
newgamebtn = Screen('newgame.png', [20,20])
newgamebtn2 = Screen('newgame2.png', [20,20])
loadgamebtn = Screen('loadgame.png', [20,140])
loadgamebtn2 = Screen('loadgame2.png', [20,140])
optionsbtn = Screen('options.png', [20, 260])
optionsbtn2 = Screen('options2.png', [20, 260])
startfont = pygame.font.Font(None, 30)
startfontsurf = startfont.render("Press Space", 1, (255, 255, 255))
firsttext = startfont.render("Hello there! It's so nice to meet you!", 1, (255, 255, 255))
startfontpos = [325,400]
truefontpos = [20, 500]
start = False
startfonton = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and start == False:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                start = True
        elif event.type == pygame.QUIT:
            running = False
    if not start:
        screen.blit(startscreen.image, startscreen.rect)
        screen.blit(game.image, game.rect)
        if startfonton:
            screen.blit(startfontsurf, startfontpos)
            startfonton = False
        else:
            pygame.draw.rect(screen, [0, 0, 0], [325,400,125,50], 0)
            startfonton = True
        pygame.display.flip()
        pygame.time.delay(500)
    else:
        screen.fill([0, 0, 0])
        if cursor == 1:
            screen.blit(newgamebtn2.image, newgamebtn2.rect)
            screen.blit(loadgamebtn.image, loadgamebtn.rect)
            screen.blit(optionsbtn.image, optionsbtn.rect)
            pygame.display.flip()
        elif cursor == 2:
            screen.blit(newgamebtn.image, newgamebtn.rect)
            screen.blit(loadgamebtn2.image, loadgamebtn2.rect)
            screen.blit(optionsbtn.image, optionsbtn.rect)
            pygame.display.flip()
        else:
            screen.blit(newgamebtn.image, newgamebtn.rect)
            screen.blit(loadgamebtn.image, loadgamebtn.rect)
            screen.blit(optionsbtn2.image, optionsbtn2.rect)
            pygame.display.flip()        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if cursor < 3:
                        cursor = cursor + 1
                elif event.key == pygame.K_UP:
                    if cursor > 1:
                        cursor = cursor - 1
                elif event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    if cursor == 1:
                        screen.fill([0, 0, 0])
                        screen.blit(firsttext, truefontpos)
                        pygame.display.flip()
                        cont = False
                        while not cont:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        cont = True
                                    elif event.key == pygame.K_ESCAPE:
                                        pygame.quit()
                        pygame.draw.rect(screen, [0,0,0], [0,500,1000,100],0)
                        screen.blit(startfont.render("My name is [Name].",1,(255,255,255)),truefontpos)
                        pygame.display.flip()
                        pygame.time.delay(1000)
                    elif cursor == 2:
                        screen.fill([255, 255, 255])
                    else:
                        screen.fill([0, 0, 0])
                         
pygame.quit()
