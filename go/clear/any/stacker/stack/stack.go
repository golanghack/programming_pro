package stack

import "errors"

type Stack []interface{}

func (stack *Stack) Pop() (interface{}, error) {
	theStack := *stack
	if len(theStack) == 0 {
		return nil, errors.New("не могу использовать Pop() с пустым стеком")
	}
	x := theStack[len(theStack) - 1]
	*stack = theStack[:len(theStack) - 1]
	return x, nil
}

func (stack *Stack) Push(x interface{}) {
	*stack = append(*stack, x)
}

func (stack Stack) Top() (interface{}, error) {
	if len(stack) == 0 {
		return nil, errors.New("не могу использовать Top() с пустым стеком")
	}
	return stack[len(stack) - 1], nil
}

func (stack Stack) Cap() int {
	return cap(stack)
}

func (stack Stack) Len() int {
	return len(stack)
}

func (stack Stack) IsEmpty() bool {
	return len(stack) == 0
}