"""
Two players (numbered 1 and 2) are playing a game with n stones. Player 1 
always plays first, and the two players move in alternating turns. The game's 
rules are as follows:

In a single move, a player can remove 2, 3, or 5 stones from the game board.
If a player is unable to make a move, that player loses the game.

Given the number of stones, find and print the name of the winner on a new line. 
Each player plays optimally, meaning they will not make a move that causes them 
to lose the game if some better, winning move exists.

Input Format

The first line contains an integer, T, denoting the number of test cases. 
Each of the  subsequent lines contains a single integer n denoting the number 
of stones in a test case.

Output Format

On a new line for each test case, print 'First' if the first player wins; 
otherwise, print 'Second'.

# doctests
>>> play(1)
'Second'
>>> play(2)
'First'
>>> play(3)
'First'
>>> play(4)
'First'
>>> play(5)
'First'
>>> play(6)
'First'
>>> play(7)
'Second'
>>> play(8)
'Second'
>>> play(10)
'First'

Explanation

In the sample, we have 8 testcases.

We'll refer to our two players as  and .

If ,  can't make any moves and loses the game (i.e., the  wins and we print  on 
a new line).

If ,  removes  stones in their first move and wins the game, so we print  on a 
new line.

If ,  removes  stones in their first move, leaving  stone on the board. Because  
is left with no available moves,  wins and we print  on a new line.

If ,  removes  stones in their first move, leaving  stone on the board. Because
has no available moves, 

"""



def play(stones):
    # "moves" is a map from number of stones to whether player1 will win; 
    # player1 always goes first;
    moves = {0:False, 1:False, 2:True, 3:True, 4:True, 5:True, 6:True, 7:False}
    x = max(moves.keys())
    while x < stones:
        x += 1 
        if moves[x-2] == moves[x-3] == moves[x-5]:
            moves[x] = not moves[x-2] 
        elif not moves[x-5] or not moves[x-3] or not moves[x-2]:
            moves[x] = True
    return "First" if moves[stones] else "Second"

if __name__ == "__main__":
    import doctest
    doctest.testmod()


T = int(input())
while T:
    num_stones = int(input())
    print(play(num_stones))
    T -= 1


