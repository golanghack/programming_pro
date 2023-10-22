package router

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
)


func SetupRouters(app *fiber.App) {
	app := fiber.App()
	api := app.Group("api", logger.New())
	user := app.Group("user", logger.New())

	user.Get("/", func(c *fiber.Ctx) {})
	user.Get("/:userId", func(c *fiber.Ctx) {})
	user.Put("/:userId", func(c *fiber.Ctx) {})
}