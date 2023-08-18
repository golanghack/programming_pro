#! /usr/bin/env python3 

"""First neural network."""


weight: float = 0.1

def neural_net(input_data: int, weight: float) -> float:
    """Return prdiction."""
    
    prediction = input_data * weight
    return prediction

 
numbers: list = [8.5, 9.5, 10, 9]
input_data = numbers[0]

predict = neural_net(input_data, weight)

print(predict)