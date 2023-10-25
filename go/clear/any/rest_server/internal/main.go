package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/go-openapi/loads"
    "github.com/go-openapi/runtime/middleware"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/rest_server/pkg/swagger/server/restapi"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/rest_server/pkg/swagger/server/restapi/operations"

)

func main() {
	// Swagger
	swaggerSpec, err := loads.Analyzed(restapi.SwaggerJSON, "")
	if err != nil {
		log.Fatalln(err)
	}

	api := operations.NewHelloAPIAPI(swaggerSpec)
	server := restapi.NewServer(api)

	defer func() {
		if err := server.Shutdown(); err != nil {
			// err handle 
			log.Fatalln(err)
		}
	}()

	server.Port = 8000
	api.CheckHealthHandler = operations.CheckHealthHandlerFunc(Health)
	api.GetHelloUserHandler = operations.GetHelloUserHandlerFunc(GetHelloUser)
	api.GetGoNameHandler = operations.GetGoNameHandlerFunc(GetGoByName)

	// start server 
	if err := server.Serve(); err != nil {
		log.Fatalln(err)
	}
}

// Health router return OK 
func Health(operations.CheckHealthParams) middleware.Responder {
	return operations.NewCheckHealthOK().WithPayload("OK")
}

// GetHelloUser return Hello + name(you)
func GetHelloUser(user operations.GetHelloUserParams) middleware.Responder {
	return operations.NewGetHelloUserOK().WithPayload("Hi " + user.User + "!")
}

// GetGoByName return go in png 
func GetGoByName(gother operations.GetGoNameParams) middleware.Responder {
	var URL string 
	if gother.Name != "" {
		URL = "https://github.com/scraly/gophers/raw/main/" + gother.Name + ".png"
	} else {
		// by default 
		URL = "https://github.com/scraly/gophers/raw/main/dr-who.png"
	}

	response, err := http.Get(URL)
	if err != nil {
		fmt.Println("error")
	}
	return operations.NewGetGoNameOK().WithPayload(response.Body)
}