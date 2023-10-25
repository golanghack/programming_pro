package router

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/logger"
	noteRoutes "github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/internal/routers/note"
)


func SetupRouters(app *fiber.App) {
	api := app.Group("/api", logger.New())
	// Setup
	noteRoutes.SetupNoteRoutes(api)
}