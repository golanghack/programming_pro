package main

import (
	"bytes"
	"io"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"testing"
)


func TestBigDigits(t *testing.T) {
	log.SetFlags(0)
	log.Println("Тестирование программы bigdigits.go")
	path, _ := os.Getwd()
	expected, err := io.ReadFile(filepath.Join(path, "0123456789.txt"))
	if err != nil {
		t.Fatal(err)
	}
	executable := filepath.Join(path, "bigdigits")
	reader, writer, err := os.Pipe()
	if err != nil {
		t.Fatal(err)
	}
	command := exec.Command(executable, "0123456789")
	command.Stdout = writer
	err = command.Run()
	if err != nil {
		t.Fatal(err)
	}
	writer.Close()
	actual, err := io.ReadAll(reader)
	if err != nil {
		t.Fatal(err)
	}
	reader.Close()
	if bytes.Compare(actual, expected) != 0 {
		t.Fatal("actual != expected")
	}
}