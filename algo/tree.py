#! /usr/bin/env python3 
"""<--TREE-->"""

import pandas as pd 
import numpy as np 

ess = pd.read_csv('ess.csv')

ess = ess.loc[ess['sclmeet'] <= 10,:].copy()
ess = ess.loc[ess['sclmeet'] <= 10,:].copy()
ess = ess.loc[ess['rlgdgr'] <= 10,:].copy()
ess = ess.loc[ess['hhmmb'] <= 50,:].copy()
ess = ess.loc[ess['netusoft'] <= 5,:].copy()
ess = ess.loc[ess['agea'] <= 200,:].copy()
ess = ess.loc[ess['health'] <= 5,:].copy()
ess = ess.loc[ess['happy'] <= 10,:].copy()
ess = ess.loc[ess['eduyrs'] <= 100,:].copy().reset_index(drop=True)

social = list(ess.loc[:, 'sclmeet'])
happy = list(ess.loc[:, 'happy'])

low_social = [hap for soc, hap in zip(social, happy) if soc <= 5]
hight_social = [hap for soc, hap in zip(social, happy) if soc > 5]

mean_lower = np.mean(low_social)
mean_higher = np.mean(hight_social)

low_errors = [abs(low_happy - mean_lower) for low_happy in low_social]
hight_errors = [abs(high_happy - mean_higher) for high_happy in hight_social]

total_errors = sum(low_errors) + sum(hight_errors)

def get_splitpoint(all_values, predicated_values):
    lowest_error = float('inf')
    best_split = None
    best_lowermean = np.mean(predicated_values)
    best_highermean = np.mean(predicated_values)
    for percentile in range(1, 100):
        split_candidate = np.percentile(all_values, percentile)
        lower_rout_comes = [outcome for value, outcome in zip(all_values, predicated_values) if value <= split_candidate]
        high_rout_comes = [outcome for value, outcome in zip(all_values, predicated_values) if value > split_candidate]
        
        if np.min([len(lower_rout_comes), len(high_rout_comes)]) > 0:
            mean_lower = np.mean(lower_rout_comes)
            mean_higher = np.mean(high_rout_comes)
            
            lower_errors = [abs(outcome - mean_lower) for outcome in lower_rout_comes]
            higher_errors = [abs(outcome - mean_higher) for outcome in high_rout_comes]
            
            total_error = sum(lower_errors) + sum(higher_errors)
            
            if total_error < lowest_error:
                best_split = split_candidate
                lowest_error = total_error
                best_lowermean = mean_lower
                best_highermean = mean_higher
    return best_split, lowest_error, best_lowermean, best_highermean

all_values = list(ess.loc[:, 'hhmmb'])
predicated_values = list(ess.loc[:, 'happy'])

max_deep = 3

def get_split(depth, data, variables, outcome_variable):
    best_var = ''
    lowest_error = float('inf')
    best_split = None 
    predicated_values = list(data.loc[:, outcome_variable])
    best_lowermean = -1
    best_hightmean = -1
    for var in variables:
        all_values = list(data.loc[:, var])
        splitted = get_splitpoint(all_values, predicated_values)
        
        if (splitted[1] < lowest_error):
            best_split = splitted[0]
            lowest_error = splitted[1]
            best_var = var
            best_lowermean = splitted[2]
            best_hightmean = splitted[3]
            
            
    generated_tree = [
        [best_var, float('-inf'), best_split, []],
        [best_var, best_split, float('inf'), []]
    ]
    
    if depth < max_deep:
        split_data1 = data.loc[data[best_var] <= best_split, :]
        split_data2 = data.loc[data[best_var] > best_split, :]
        if len(split_data1.index) > 10 and len(split_data2.index) > 10:
            generated_tree[0][3] = get_split(depth + 1, split_data1, variables, outcome_variable)
            generated_tree[1][3] = get_split(depth + 1, split_data2, variables, outcome_variable)
        else:
            depth = max_deep + 1 
            generated_tree[0][3] = best_lowermean
            generated_tree[1][3] = best_hightmean
            
    return generated_tree

def get_prediction(obsrver, tree):
    j = 0
    keep_going = True
    prediction = -1
    while (keep_going):
        j = j + 1
        variable_tocheck = tree[0][0]
        bound1 = tree[0][1]
        bound2 = tree[0][2]
        bound3 = tree[1][2]
        
        if obsrver.loc[variable_tocheck] < bound2:
            tree = tree[0][3]
        else:
            tree = tree[1][3]
        if isinstance(tree, float):
            keep_going = False
            prediction = tree
    return prediction

variables = ['rlgdgr', 'hhmmb', 'netusoft', 'agea', 'eduyrs']
outcome_variable = 'happy'
predictions = []
the_tree = get_split(0, ess, variables, outcome_variable)
for k in range(0, 30):
    observer = ess.loc[k, :]
    predictions.append(get_prediction(observer, the_tree))
    
ess.loc[:, 'predicted'] = predictions
errors = abs(ess.loc[:, 'predicted'] - ess.loc[:, 'happy'])


np.random.seed(518)
ess_shuffled = ess.reindex(np.random.permutation(ess.index)).reset_index(drop=True)
training_data = ess_shuffled.loc[0: 37000, :]
test_data = ess_shuffled.loc[37001:, :].reset_index(drop=True)

the_tree = get_split(0, training_data, variables, outcome_variable)
predictions = []
for k in range(0, len(test_data.index)):
    observer = test_data.loc[k,:]
    predictions.append(get_prediction(observer, the_tree))
    
test_data.loc[:, 'predicted'] = predictions
errors = abs(test_data.loc[:, 'predicted'] - test_data.loc[:, 'happy'])
print(np.mean(errors))


