import pygame
import math
import random

pygame.init()

from pygame import mixer
mixer.music.load("cradles.wav")
mixer.music.play()
mixer.music.set_volume(0.2)
mixer.init()




WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")


RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)


images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

winning=["GREAT WORK","WELL DONE","YOU WIN","WON KEEP SHINING"]
losing=["TRY AGAIN","BETTER LUCK NEXT TIME","OOPS! RETRY"]
hangman_status = 0
file=open("words.txt","a")
words='PYTHON VARIABLES ARRAYS LISTS ALGORITHM ARGUMENTS OPERATORS BINARY LOOPS FUNCTIONS JAVA  PROGRAM BOOLEAN OBJECTS CLASS INCREMENT DECREMENT ITERATION KEYWORDS OPERAND POINTER PACKAGE BACKEND FRONTEND SYNTAX BINARY COMPILER BUG CONSTANTS DEBUGGING INPUT OUTPUT TERMINAL'.split()
word = random.choice(words)
file.write("\n")
file.write(word)
file.close()
guessed = []


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)


def draw():
    win.fill((118,238,198))

    
    text = TITLE_FONT.render("LET'S PLAY", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

   
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, WHITE)
    win.blit(text, (50, 200))

  
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (550, 150))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill((238,118,0))
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()
     
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
               
                break
        
        if won:
            a=random.choice(winning)
            display_message(a)
            break

        if hangman_status == 6:
            b=random.choice(losing)
            display_message(b)
            break
 
while True:
    
    main()

pygame.quit()