import os,time, sys
from pynput import keyboard
import random

os.system("mode 70,40")
class screen:
	def __init__(self,x=70,y=40):
		self.screen=[]
		self.x=x
		self.y=y
	def draw(self, objs):
		screen=[[" " for z in range(self.x//2)] for i in range(self.y)]
		while len(objs)>0:
			i=objs.pop()
			while len(i)>0:
				screen[i.pop()][i.pop()]="*"
		os.system("cls")
		print(*list(map(lambda x: " ".join(x),screen)), end="\n")

	

class rectangle:
	def __init__(self, width,height,x=0,y=0):
		self.width=width
		self.height=height
		self.x=x
		self.y=y
		self.obj=[]
	def draw(self):
		global screen
		if self.x<1:
			self.x=1
		if self.x>screen.x//2-self.width-1:
			self.x=screen.x//2-self.width-1
		if self.y<1:
			self.y=1
		if self.y>screen.y-self.height-1:
			self.y=screen.y-self.height-1
		ris=[]
		for i in range(self.width):
			ris.append(self.x+i)
			ris.append(self.y)
			ris.append(self.x+i)
			ris.append(self.y+self.height)
		for i in range(1,self.height):
			ris.append(self.x)
			ris.append(self.y+i)
			ris.append(self.x+self.width-1)
			ris.append(self.y+i)
		return ris
rec=rectangle(5,5,20,10)
rec1=rectangle(3,3,4,y=3)
screen=screen()
screen.draw([rec.draw(), rec1.draw()])

def on_press(key):
	global rec1
	if key == keyboard.Key.right:
		rec.x+=1

	if key == keyboard.Key.left:

		rec.x=rec.x-1
	if key == keyboard.Key.up:
		rec.y=rec.y-1

	if key == keyboard.Key.down:
		rec.y=rec.y+1
		
	if key == keyboard.Key.esc:
		listener.stop()
	if rec.x==rec1.x+rec1.width//2 and rec.y+rec.height//2 in range(rec1.y,rec1.y+rec1.height):
		rec1=rectangle(3,3, random.randint(10,30),random.randint(10,60))
	screen.draw([rec.draw(), rec1.draw()])

listener = keyboard.Listener(on_press=on_press,)
listener.start()
listener.join()




