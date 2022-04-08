import sys, random , os, time

print('ROCK , PAPER & SCISSORS')
time.sleep(3)

win = losses = ties = 0

rndm_options = ['r', 'p', 's']
rndm_no = 0

chance = 'null'

def clrscr():
	if os.name == 'posix':
		_  = os.system('clear')
	else:
		_ = os.system('cls')

def instruct():
	print('Enter your choice among rock, paper and scissors')
	print('Enter r for rock, p for paper , s for scissors and q for quit')

def curr_score():
	print('WINS =',win , 'LOSSES =', losses, 'TIES =', ties)


def show(chance):
	if chance == 'r':
		print('You have choosen rock')
	elif chance == 'p':
		print('You have choosen paper')
	elif chance == 's':
		print('You have choosen scissors')

def versus(rndm):
	if rndm == 'r':
		print('versus  rock')
	elif rndm == 'p':
		print('versus paper')
	elif rndm == 's':
		print('versus scissors')
def won():
	print('You won this')

def lost():
	print('You lost')

def draw():
	print('Its a draw')
clrscr()

while(chance != 'q'):
	clrscr()
	curr_score()
	print()
	instruct()
	
	
	chance = input()
	
	if(chance != 'r' and chance != 'p' and chance != 's' and chance != 'q'):
		clrscr()
		continue
	rndm_no = random.randint(0,2)
	show(chance)
	versus(rndm_options[rndm_no])
	if(chance == rndm_options[rndm_no]):
		ties+=1
		draw()
		time.sleep(2)
	elif(chance == 'p' and rndm_options[rndm_no] == 'r'):
		win+=1
		won()
		time.sleep(2)
	elif(chance == 'r' and rndm_options[rndm_no] == 's'):
		win+=1
		won()
		time.sleep(2)
	elif(chance == 's' and rndm_options[rndm_no] == 'p'):
		win+=1
		won()
		time.sleep(2)
	elif(chance == 'p' and rndm_options[rndm_no] == 's'):
		losses+=1
		lost()
		time.sleep(2)
	elif(chance == 's' and rndm_options[rndm_no] == 'r'):
		losses+=1
		lost()
		time.sleep(2)
	elif(chance == 'r' and rndm_options[rndm_no] == 'p'):
		losses+=1
		lost()
		time.sleep(2)

clrscr()
print('The final scores are:')
curr_score()


