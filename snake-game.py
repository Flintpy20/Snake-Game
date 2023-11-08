import pygame
from random import randrange
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

try:
	pygame.init()
except:
	print("O módulo pygame não foi iniciado corretamente")

width=320
height=280
length=10
score =40

clock = pygame.time.Clock()
background = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

def text (msg, color, tam, x, y):
	font = pygame.font.SysFont(None, tam)
	text1 = font.render(msg, True, color)
	background.blit(text1, [x, y])

def snake(SnakeXY):
	for XY in SnakeXY:
		pygame.draw.rect(background, green, [XY[0], XY[1], length, length])
	
def apple(pos_x, pos_y):
	pygame.draw.rect(background, red, [pos_x, pos_y, length, length])
	
def game():
	sair = True
	gameover = False
	pos_x=randrange(0, width-length,10)
	pos_y=randrange(0, height-length-score,10)
	apple_x=randrange(0, width-length,10)
	apple_y=randrange(0, height-length-score,10)
	velocity_x=0
	velocity_y=0
	SnakeXY = []
	SnakeComp = 1
	scores = 0
	while sair:
		while gameover:		
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sair = False
					gameover = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_c:
						sair = True
						gameover = False
						pos_x=randrange(0, width-length,10)
						pos_y=randrange(0, height-length-score,10)
						apple_x=randrange(0, width-length,10)
						apple_y=randrange(0, height-length-score,10)
						velocity_x=0
						velocity_y=0
						SnakeXY = []
						SnakeComp = 1
						scores = 0
					if event.key == pygame.K_s:
						sair = False
						gameover = False
			background.fill(white)
			text("Game Over. To continue to press C or S to quit playing", red, 15, width/10, height/2)
			pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT and velocity_x != length:
					velocity_y=0
					velocity_x=-length
				if event.key == pygame.K_RIGHT and velocity_x != -length:
					velocity_y=0
					velocity_x=length
				if event.key == pygame.K_UP and velocity_y != length:
					velocity_x=0
					velocity_y=-length
				if event.key == pygame.K_DOWN and velocity_y != -length:
					velocity_x=0
					velocity_y=length
		if sair:
			background.fill(white)
			pos_x+=velocity_x
			pos_y+=velocity_y
			
			if pos_x == apple_x and pos_y == apple_y:
				apple_x=randrange(0, width-length,10)
				apple_y=randrange(0, height-length-score,10)
				SnakeComp += 1
				scores += 1
			
			if pos_x + length > width:
				pos_x = 0
			if pos_x < 0:
				pos_x=width-length
			if pos_y + length > height-score:
				pos_y = 0
			if pos_y < 0:
				pos_y=height-length-score
			
			
			SnakeHead = []
			SnakeHead.append(pos_x)
			SnakeHead.append(pos_y)
			SnakeXY.append(SnakeHead)
			if len(SnakeXY) > SnakeComp:
				del SnakeXY[0]
			if any(Block == SnakeHead for Block in SnakeXY[:-1]):
				gameover = True
			
			pygame.draw.rect(background, black, [0, height-score, width, score])
			text("Pontuação:" + str(scores), white, 20, 10, height-30)
			snake(SnakeXY)
			apple(apple_x, apple_y)
			pygame.display.update()
			clock.tick(10)
				
game()
pygame.quit()
