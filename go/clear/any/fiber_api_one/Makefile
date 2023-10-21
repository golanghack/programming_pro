build:
	go build -o server 

run: build
	./server

watch:
	reflex -s -r '\.go$$' make run 