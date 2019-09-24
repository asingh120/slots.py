'''
Program: slot.py
Author: Amit
Date: 9/21/19

Program uses gui with to imitate a slot machine 
which generates three random words from a list.  If all 
three words match, then user wins grand prize. If two 
out of three match, then user wins second prize.
'''

from breezypythongui import EasyFrame
import random


class Slots(EasyFrame):

	def __init__(self):
		''' sets up the window and the widgets'''
		EasyFrame.__init__(self, "Lotsa Slots", width = 470, height = 355, background = 'powderblue')

		# sets up the labels and widgets
		self.title = self.addLabel(text = "Ready to Play?", row = 0, column = 0, columnspan = 3, sticky = "NSEW" ,background = 'powderblue', font = ("Helvetica", 20, 'italic'))
		self.first = self.addTextField(text = "", row = 1, column = 0, rowspan = 2, width = 100)
		self.second = self.addTextField(text = "", row = 1, column = 1, rowspan = 2, width = 100)
		self.third = self.addTextField(text = "", row = 1, column = 2, rowspan = 2, width = 100)

		self.main = self.addLabel(text = "Let's Make Some Magic Baby", row = 3, column = 0, columnspan = 3, sticky = "NSEW", background = 'powderblue', font = ("Arial Black", 20))
		self.button = self.addButton(text = "Spin That Shit", row = 4, column = 0, columnspan = 4, command = self.spin)
		self.addLabel(text = "", row = 5, column =0, columnspan = 4, sticky = "NSEW", background = 'powderblue')

		self.button["background"] = 'red'
		self.button["foreground"] = 'white'
		self.button["font"] = "Times+New+Roman"

	# Event Handler Method
	def spin(self):
		# Creates list of possible words 
		master = ["coin", "tree", "ball", "wand", "banana", "weeb", "cinder"]

		# Assign variables for each random word
		one = random.choice(master)
		two = random.choice(master)
		three = random.choice(master)

		# Sets random word to text field
		self.first.setText(one)
		self.second.setText(two)
		self.third.setText(three)

		# Game mechanics for deciding if there is a winner or not
		if one == two == three:
			self.win = self.addLabel(text = "YOU JUST WON, BIIIG TIME!!", row = 5, column = 0, columnspan = 4, sticky = "NSEW", background = 'yellow', font = ("Arial+Bold", 22, 'italic'))
		elif one == two or one == three or two == three:
			self.runner = self.addLabel(text = "YOU WIN... JUST IN SECOND PLACE!", row = 5, column = 0, columnspan = 4, sticky = "NSEW", background = 'lawngreen', font = ("Verdana", 18))
		else:
			self.nowin = self.addLabel(text = "WOMP WOMP, SPIN AGAIN", row = 5, column =0, columnspan = 4, sticky = "NSEW", background = 'powderblue', font = ("Helvetica", 14, 'bold'))

def main():
	Slots().mainloop()

main()

		