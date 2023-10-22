package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/database"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/router"
)

func main() {
	app := fiber.New()

	// connect to DB
	database.ConnectDB()

	router.SetupRouters(app)
	app.Listen(":8000")
}

