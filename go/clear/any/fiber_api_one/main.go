package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/database"
)

func main() {
	app := fiber.New()

	// connect to DB
	database.ConnectDB()

	// endpoint 
	app.Get("/", func(c *fiber.Ctx) error {
		err := c.SendString("API Support")
		return err
	})
	app.Listen(":8000")
}

