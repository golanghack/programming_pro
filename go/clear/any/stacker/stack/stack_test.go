package stack_test

import (
	"stacker/stack"
	"testing"
)

func TestStack(t *testing.T) {
	count := 1
	var aStack stack.Stack 
	assertTrue(t, aStack.Len() == 0, "пустой стек Stack", count)
	count++ 
	assertTrue(t, aStack.Cap() == 0, "expected empty Stack", count) // 2
    count++
    assertTrue(t, aStack.IsEmpty(), "expected empty Stack", count) // 3
    count++
    value, err := aStack.Pop()
    assertTrue(t, value == nil, "expected nil value", count) // 4
    count++
    assertTrue(t, err != nil, "expected error", count) // 5
    count++
    value1, err := aStack.Top()
    assertTrue(t, value1 == nil, "expected nil value", count) // 6
    count++
    assertTrue(t, err != nil, "expected error", count) // 7
    count++
    aStack.Push(1)
    aStack.Push(2)
	aStack.Push("три")
	assertTrue(t, aStack.Len() == 3, "не пустой стек", count) // 8
	count++ 
	assertTrue(t, aStack.IsEmpty() == false, "не пустой стек", count) // 9
	count++ 
	value2, err := aStack.Pop()
	assertEqualString(t, value2.(string), "три", "неизвестный текст")
}

func assertTrue(t *testing.T, condition bool, message string, id int) {
    if !condition {
        t.Errorf("#%d: %s", id, message)
    }
}

func assertEqualString(t *testing.T, a, b string, message string, id int) {
    if a != b {
        t.Errorf("#%d: %s \"%s\" !=\n\"%s\"", id, message, a, b)
    }
}