import pygame
import math
import random

pygame.init()
WIDTH,HEIGHT = 800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("WELCOME TO HANGMAN")

WHITE = (0,0,255)
LIGHT_CYAN = (128,207,215)
MIDNIGHT_BLUE = (25,25,112)
MEDIUM_BLUE = (38,0,146)
#MEDIUM_BLUE = (0,0,205)
INDIGO = (75,0,130)
PEACH = (255,255,224)
GOLD = (255,215,0)
KHAKI = (240,230,140)
RED = (255,0,0)
New = (10,10,200)
BLACK = (255,255,255)

def main():
 Radius = 20
 Gap = 15
 letters=[]
 start_x= round((WIDTH - (Radius * 2 + Gap) * 13) / 2)
 start_y= 400
 A = 65

 for i in range(26):
   x = start_x + Gap * 2 + ((Radius * 2 + Gap) * (i % 13))
   y = start_y + ((i//13) * (Gap + Radius * 2))
   letters.append([x,y, chr(A + i), True])
  

 Letter_Font = pygame.font.SysFont('timesnewroman',25)
 Word_Font = pygame.font.SysFont('timesnewroman',40)
 Title_Font = pygame.font.SysFont('timesnewroman',45)
 Trophy = pygame.image.load("Trophy.png")
 Cry = pygame.image.load("Cry.png")
 images=[]
 for i in range (7): 
   image=pygame.image.load("Hangman "+str(i)+".png")
   images.append(image)

 hangman_status = 0
 words = ["DEVELOPER", "HANGMAN", "MALDIVES","STUDENT", "CODING"]
 word = random.choice(words)
 guessed = []
 """ 
 WHITE = (0,0,255)
 LIGHT_CYAN = (128,207,215)
 MIDNIGHT_BLUE = (25,25,112)
 MEDIUM_BLUE = (38,0,146)
 #MEDIUM_BLUE = (0,0,205)
 INDIGO = (75,0,130)
 PEACH = (255,255,224)
 GOLD = (255,215,0)
 KHAKI = (240,230,140)
 RED = (255,0,0)
 New = (10,10,200)
  """
 FPS = 60
 clock = pygame.time.Clock()
 run = True
 
 def draw():
   win.fill(LIGHT_CYAN)
   text = Title_Font.render("HANGMAN GAME",1,MIDNIGHT_BLUE)
   win.blit(text, (WIDTH/2 - text.get_width()/2,20))
   text = Letter_Font.render("Click a letter and try to guess the word!",1,New)
   win.blit(text, (WIDTH/2 - text.get_width()/2,75))
   
   display_word = ""
   for letter in word:
     if letter in guessed:
       display_word += letter + " "
     else:
       display_word += "_ "
   text = Word_Font.render(display_word, 1, MEDIUM_BLUE)
   win.blit(text,(400, 200))
       
   for letter in letters:
     x,y, ltr,visible=letter
     if visible:
      pygame.draw.circle(win, MEDIUM_BLUE,(x,y), Radius, 2)
      text = Letter_Font.render(ltr,1,MEDIUM_BLUE)
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
   win.blit(images[hangman_status],(150,100))
   pygame.display.update()

 def display_message(message):
   pygame.time.delay(900)
   win.fill(PEACH)
   win.blit(Trophy,(300,160))
   text = Word_Font.render(message, 1, GOLD)
   win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 - 100))
   pygame.display.update()
   pygame.time.delay(2500)

 def display_messagelost(message):
   pygame.time.delay(900)
   win.fill(KHAKI)
   win.blit(Cry,(300,200))
   text = Word_Font.render(message, 1, RED)
   win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2 - 100))
   pygame.display.update()
   pygame.time.delay(2500)
 menu = False
   
 
 while run:
   clock.tick(FPS)
   pygame.display.update()
   left_pressed = pygame.mouse.get_pressed(3)[0]
   m_x, m_y = pygame.mouse.get_pos()

   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       run = False
  
   if menu:
     rect = pygame.draw.rect(win, (200,200,255), (195,50,400,50))
     text = Word_Font.render("Press to play again", 1, BLACK)
     win.blit(text, (200, 50))
     if rect.collidepoint((m_x, m_y)) and left_pressed:
       #print("HAZAAH!!!!!!!")
       hangman_status = 0
       won = False
       word = random.choice(words)
       for letter in letters: letter[3] = True
       guessed = []
       menu = False

   else:
       if left_pressed:
         for letter in letters:
           x,y,ltr,visible = letter
           if visible:
            dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
            if dis < Radius:
             letter[3] = False
             guessed.append(ltr)
             if ltr not in word:
               hangman_status += 1
     
       draw()
       
       for event in pygame.event.get():
         if event.type == pygame.QUIT:
           run = False
         if event.type == pygame.MOUSEBUTTONDOWN:
           m_x,m_y = pygame.mouse.get_pos()
           for letter in letters:
             x,y,ltr,visible = letter
             if visible:
              dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
              if dis < Radius:
               letter[3] = False
               guessed.append(ltr)
               if ltr not in word:
                 hangman_status += 1
       draw()
       if set(word).issubset(set(guessed)):
        won = True
       for letter in word:
         if letter not in guessed:
           won = False
           break
    
       if won:
         display_message("Congratulations, you WON!")
         #pygame.display.update()
         menu = True
         #break
       if hangman_status == 6:
         display_messagelost("Sorry, you LOST!")
         display_messagelost("The correct word was " + word)
         #menu = True
         #pygame.display.update()
         menu = True
         #break

main()
"""
Word_Font = pygame.font.SysFont('timesnewroman',40)

def message(message):
  pygame.time.delay(900)
  win.fill(PEACH)
  text = Word_Font.render(message, 1, GOLD)
  win.blit(text, (WIDTH/2 - 
  text.get_width()/2, HEIGHT/2 - 
  text.get_height()/2 - 100))
  pygame.display.update()

message("Do you want to play again? ")
Radius = 80
Gap = 40
letters=[]
start_x= round((WIDTH - (Radius * 2 + Gap) * 13) / 2)
start_y= 400
if message == "yes":
  main()
elif message == "no":
  print("Thank you for playing.")"""
pygame.quit()
