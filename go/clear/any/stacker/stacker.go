
package main

import (
	"fmt"
	"stacker/stack"
	"strings"
)

func main() {
	var haystack stack.Stack
	haystack.Push("one")
	haystack.Push(-20)
	haystack.Push([]string{"two", "three", "foo"})
	haystack.Push(50.00)
	for {
		item, err := haystack.Pop()
		if err != nil {
			break
		} 
		fmt.Println(item)
	}
	var aStack stack.Stack
	aStack.Push("abracadabra")
	aStack.Push(4)
	aStack.Push(99)
	x, err := aStack.Top()
	fmt.Println(x)
	aStack.Push(-6e-4)
	aStack.Push("Wow")
	x, err = aStack.Top()
	fmt.Println(x)
	aStack.Push(33.5)
	fmt.Println("стек пуст", aStack.IsEmpty())
	fmt.Printf("Len() == %d Cap == %d\n", aStack.Len(), aStack.Cap())
	difference := aStack.Cap() - aStack.Len()
	for i := 0; i < difference; i++ {
		aStack.Push(strings.Repeat("*", difference - i))
	}
	fmt.Printf("Len() == %d Cap == %d\n", aStack.Len(), aStack.Cap())
	for aStack.Len() > 0 {
		x, _ = aStack.Pop()
		fmt.Printf("%T %v\n", x, x)
	}
	fmt.Println("стек пуст", aStack.IsEmpty())
	x, err = aStack.Pop()
	fmt.Println(x, err)
	x, err = aStack.Top()
	fmt.Println(x, err)
}