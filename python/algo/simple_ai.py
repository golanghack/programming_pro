#! /usr/bin/env python3 

"""<--SIMPLE AI-->"""

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib import collections as mc 


def draw_lattice(n, name):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j,'o', c = 'black')
            
    plt.savefig(name)

def draw_game(n, name, game):
    colors2 = []
    for k in range(0, len(game)):
        if k % 2 == 0:
            colors2.append('red')
        else:
            colors2.append('blue')
    lc = mc.LineCollection(game, colors=colors2, linewidths=2)
    fig, ax = plt.subplots()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            plt.plot(i, j, 'o', c = 'black')
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.savefig(name)

def count_squares(game):
    count_of_squares = 0
    for line in game:
        parallel = False
        left = False
        rigth = False
        if line[0][1] == line[1][1]:
            if [(line[0][0], line[0][1] - 1), (line[1][0], line[1][1] - 1)] in game:
                parallel = True
            if [(line[0][0], line[0][1]), (line[1][0] - 1, line[1][1] - 1)] in game:
                left = True
            if [(line[0][0] + 1, line[0][1]), (line[1][0], line[1][1] - 1)] in game:
                rigth = True
            if parallel and left and rigth:
                count_of_squares += 1
    return count_of_squares


def score(game):
    score = [0, 0]
    progress = []
    squares = 0
    for line in game:
        progress.append(line)
        new_squares  = count_squares(progress)
        if new_squares > squares:
            if (len(progress) % 2) == 0:
                score[1] = score[1] + 1
            else:
                score[0] = score[0] + 1
        squares = new_squares
    return score

def generate_tree(possible_moves, depth, max_depth, game_so_far):
    tree = []
    for move in possible_moves:
        move_profile = [move]
        game2 = game_so_far.copy()
        game2.append(move)
        move_profile.append(score(game2))
        if depth < max_depth:
            possible_moves2 = possible_moves.copy()
            possible_moves2.remove(move)
            move_profile.append(generate_tree(possible_moves2, depth + 1, max_depth, game2))
        else:
            move_profile.append([])
        tree.append(move_profile)
    return  tree

def minimax(max_or_min, tree):
    allscores = []
    for move_profile in tree:
        if move_profile[2] == []:
            allscores.append(move_profile[1][0] - move_profile[1][1])
        else:
            move, score = minimax((-1) * max_or_min, move_profile[2])
            allscores.append(score)
    new_list = [score * max_or_min for score in allscores]
    best_score = max(new_list)
    best_move = np.argmax(new_list)
    return best_move, max_or_min * best_score

game = [[(1,2),(1,1)],[(3,3),(4,3)],[(1,5),(2,5)],[(1,2),(2,2)],[(2,2),(2,1)],\
[(1,1),(2,1)],[(3,4),(3,3)],[(3,4),(4,4)]]
allpossible = []
game_size = 5

for i in range(1, game_size + 1):
    for j in range(2, game_size + 1):
        allpossible.append([(i, j), (i, j - 1)])
for i in range(1, game_size):
    for j in range(1, game_size + 1):
        allpossible.append([(i, j), (i + 1, j)])
for move in allpossible:
    if move in game:
        allpossible.remove(move)
        
        
the_tree = generate_tree(allpossible, 0, 3, game)

move, score = minimax(1, the_tree)

print(the_tree[move][0])


draw_lattice(5, 'lat.png')  
draw_game(5, 'game.png', game)
  
