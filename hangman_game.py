#hangman game

import random
words =  ("apple","banana" ,"orange","pineapple" ,"coconut")
hangman= {0:("   ","   ","   "),1:(" 0 ","   ","   "), 2:(" 0  ","/   ","   "), 3:(" 0 ","/ \\","   "), 4:(" 0 ","/ \\"," | ","   "), 5:(" 0 ","/ \\"," | ","/  "), 6:(" 0 ","/ \\"," | ","/ \\   ")}
for x in hangman[6]:
	print(x)