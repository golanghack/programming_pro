# syntax=docker/dockerfile:1
FROM golang:1.17-alpine 
RUN apk add curl 
WORKDIR /app
COPY go.mod ./
COPY go.sum ./
RUN go mod download 
COPY *.go ./

# Now it should build
RUN go build -o /app
EXPOSE 8083
CMD ['/app']