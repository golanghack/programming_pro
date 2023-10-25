package noteRoutes

import (

	"github.com/gofiber/fiber/v2"
	noteHandler "github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/internal/handler/note"
)

func SetupNoteRoutes (router fiber.Router) {
	note := router.Group("/note")

	//add 
	note.Post("/", noteHandler.CreateNotes)
	// read 
	note.Get("/", noteHandler.GetNotes)
	// read one
	note.Get("/:noteId", noteHandler.GetNote)
	// put 
	note.Put("/noteId", noteHandler.UpdateNote)
	// delete one
	note.Delete("/noteId", noteHandler.DeleteNote)
}