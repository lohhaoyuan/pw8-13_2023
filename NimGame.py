import random
from math import *
N = 128
def calculateMex(Set):
    Mex = 0
  
    while (Mex in Set):
        Mex += 1 
  
    return (Mex)
def calculateGrundy( n):
    if (n == 0):
        return (0)
  
    Set = set() # A Hash Table
  
    for i in range(n):
        Set.add(calculateGrundy(i));
  
    return (calculateMex(Set))



    
# a solver for Nim game
class NimSolver():
    def __init__(self, board):
        self.board = None
        if len(board)>10:
            print("Too many piles.")
            return
        for i in board:
            if i >= N:
                print("Too many monkey pins in one pile.")
                return
        self.board = board
        self.temp_result = {}
        self.game = True
    def hash_func(self, current_board):
        board = [i for i in current_board if i > 0]
        board.sort()
        result = 0
        for i in board:
            result = result * N + i
        return result
    def calc_nim_sum(self):
        pile_bins = [bin(pile)[2:] for pile in self.board]
        lens = [len(pile) for pile in pile_bins]
        max_len = max(lens)
        pile_bins = ["0"*(max_len - len(pile))+pile for pile in pile_bins]
        result = ""
        for i in range(max_len):
            res = 0
            for pile in pile_bins:
                res += int(pile[i])
                res %= 2
            result += str(res)
        return result
    def choose_move(self):
        nim_sum = self.calc_nim_sum(self.board)
        first_one = nim_sum.find("1")
        first_one_ind = len(nim_sum) - first_one - 1
        mod = 2**(first_one_ind+1)
        mod_piles = [pile % mod for pile in self.board]
        max_mod = -1
        max_mod_ind = -1
        for i, m_pile in enumerate(mod_piles):
            if m_pile > max_mod:
                max_mod = m_pile
                max_mod_ind = i
        max_mod_bin = bin(self.board[max_mod_ind])[2:]
        max_mod_bin = "0"*(len(nim_sum)-len(max_mod_bin))+max_mod_bin
        new_pile_bin = ""
        for i in self.board(len(nim_sum)):
            if nim_sum[i] == "1":
                new_pile_bin += str((int(max_mod_bin[i])+1)%2)
            else:
                new_pile_bin += max_mod_bin[i]
        take = self.board[max_mod_ind] - int(new_pile_bin, base=2)
        return (max_mod_ind, take)
    def am_i_winning(self, current_board):
        # remove 0 values
        board = [i for i in current_board if i > 0]
        if len(board) == 0:
            return True
        elif len(board) == 1:
            return False
        else:
            key = self.hash_func(board)
            if key in self.temp_result:
                return self.temp_result[key]
            for i in range(len(board)):
                for opponent_take_n in range(1, board[i]+1):
                    board[i] -= opponent_take_n # opponent's action

                    if self.am_i_winning(board):
                        self.temp_result[key] = False
                        return False # I will lose as opponent will win
                    board[i] += opponent_take_n # recover the board
            self.temp_result[key] = True
            # print(board)
            return True
    def binary(self,num):
        if num >= 1:    
            self.binary(num // 2)
            print(num % 2) 
    def get_nim_sum(self):
        print(self.board)
        nimsum = 0
        ii = []
        for i in self.board:
            ii.append(self.binary(i))
        for i in ii:
            for j in str(i):
                nimsum += int(j) * (10 ** int(i))

        print(nimsum)
                      
            
    def printresult(self):
        if self.board is None or len(self.board) <= 0:
            print("Invalid board.")
            return
        
        print(self.board)
        if self.am_i_winning(self.board):
            print("Starting player losers")
        else:
            print("Starting player wins") 
    def ff(self):
        if random.randint(1,2) == 1:
            print("I can't win, good game.")
        else:
            print("My loss has been written in the stars.")

    def win(self):
        if random.randint(1,4) == 1:
            print("GGWP")
        else:
            print("Good game, let's have a rematch!")
        self.game = False

def game():
    noofpiles = input("How many piles are there?")
    pileconfig = []
    for i in range(noofpiles):
        pileconfig.append(input("How many items are in pile " + str(i) + "?"))
    nim_solver = NimSolver(pileconfig)
    while nim_solver.game == True:
        nim_solver.choose_move()
        nim_solver.printresult()
    if nim_solver.am_i_winning == True:
        nim_solver.ff()
    else:
        nim_solver.win()



            




