import pygame
from checkers.constant import WHITE, YELLOW, CELL, GREY
from checkers.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_move)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = YELLOW
        self.valid_move = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select_piece(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select_piece(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_move = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_move:
            self.board.move(self.selected, row, col)
            skipped = self.valid_move[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        
        return True
    
    def change_turn(self):
        self.valid_move = {}
        if self.turn == YELLOW:
            self.turn = WHITE
        else:
            self.turn = YELLOW

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREY, (col*CELL + CELL//2, row*CELL + CELL//2), 15)