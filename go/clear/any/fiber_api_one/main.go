package main

import (
	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	// endpoint 
	app.Get("/", func(c *fiber.Ctx) error {
		err := c.SendString("API Support")
		return err
	})
	app.Listen(":8000")
}

