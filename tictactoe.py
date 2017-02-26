#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:24:00 2017

@author: zyb
"""

import numpy as np
import sys

class tic_tac_toe(object):
	# initialize with 3x3 0s
	def __init__(self):
		self._board = np.zeros(9).reshape(3,3)
		self._winner = 0

	def player(self):
		_row = 3
		_col = 3
		while _row not in [0,1,2]:
			_row = input("row(0,1,2): ")
		while _col not in [0,1,2]:
			_col = input("col(0,1,2): ")
		if self._board[_row,_col] == 0:
			self._board[_row,_col] = 1
		else: 
			print 'Occupied! Cannot put it here. Try another blank.'
			self.player()
		self.printBoard()
		self._winner = self.checkWinner()
		self.printWinner()

	def computer(self):
		# find blanks in board, output index of blanks
		_idx = np.where(self._board == 0)
		# random position out of blanks
		_len = _idx[0].shape[0]
		if _len > 0:
			_pos = np.random.choice(np.arange(_len))
			_x = _idx[0][int(_pos)]
			_y = _idx[1][int(_pos)]
			print 'x,y',_x,_y
			self._board[_x,_y] = -1
		self.printBoard()
		self._winner = self.checkWinner()
		self.printWinner()

	def checkWinner(self):
		for i in range(3):
			if(self._board[i,0] == self._board[i,1] == self._board[i,2] and self._board[i,0] != 0):
				return self._board[i,0]
		for i in range(3):
			if(self._board[0,i] == self._board[1,i] == self._board[2,i] and self._board[0,i] != 0):
				return self._board[0,i]
		if(self._board[0,0] == self._board[1,1] == self._board[2,2] and self._board[0,0] != 0):
			return self._board[0,0]
		if(self._board[0,2] == self._board[1,1] == self._board[2,0] and self._board[0,2] != 0):
			return self._board[0,2]
		# no winner yet
		if 0 in self._board:
			return 0
		else:
		# draw
			return ''

	def printWinner(self):
		if self._winner == '':
			print 'Draw!'
			exit()
		elif self._winner == 1:
			print 'Palyer win!'
			exit()
		elif self._winner == -1:
			print 'Computer win!'
			exit()
		else:
			return 0

	def printBoard(self):
		print '----------'
		for i in range(3):
			for j in range(3): 
				if self._board[i,j] == 1:
					print 'X ',
				elif self._board[i,j] == -1:
					print 'O ', 
				else:
					print '_ ', 
			print  
		print '----------'


def main():
	new_game = tic_tac_toe()
	firstplay = raw_input("First hand? y(es) or n(0): ") or 'y'
	while new_game.printWinner() == 0:
		if firstplay == 'y':
			new_game.player()
			new_game.computer()
		else:
			new_game.computer()
			new_game.player()

if __name__ == '__main__':
	main()



