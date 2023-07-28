# syntax=docker
FROM golang:1.17-alpine 
RUN apk add curl 
WORKDIR /
COPY go.mod 
COPY go.sum 
RUN go mod download 
COPY *.go 
RUN go build -o /app
EXPOSE 8083
CMD ['/app']