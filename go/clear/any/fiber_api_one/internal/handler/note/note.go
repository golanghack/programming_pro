package noteHandler

import (
	"github.com/gofiber/fiber/v2"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/database"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/internal/model"
	"github.com/google/uuid"
)

func GetNotes(c *fiber.Ctx) error {
	db := database.DB 
	var notes []model.Note 
	db.Find(&notes)

	if len(notes) == 0 {
		return c.Status(404).JSON(fiber.Map{"status": "error",
											"message": "No notes",
											"data": nil})
	}
	return c.JSON(fiber.Map{"status": "succes", 
							"message": "Notes found",
							"data": notes})					
}

func CreateNotes(c *fiber.Ctx) error {
	db := database.DB 
	note := new(model.Note)

	err := c.BodyParser(note)
	if err != nil {
		return c.Status(500).JSON(fiber.Map{"status": "error",
											"message": "Input review",
											"data": err})
	}
	note.ID = uuid.New()
	err = db.Create(&note).Error
	if err != nil {
		return c.Status(500).JSON(fiber.Map{"status": "error", 
											"message": "could not create",
											"data": err})	
	}
	return c.JSON(fiber.Map{"status": "succes",
							"message": "Create note",
							"data": note})
}

func GetNote(c *fiber.Ctx) error {
	db := database.DB 
	var note model.Note

	// read
	id := c.Params("noteId")

	// find
	db.Find(&note, "id = ?", id)

	// no such note
	if note.ID == uuid.Nil {
		return c.Status(404).JSON(fiber.Map{"status": "error", 
											"message": "no note",
											"data": nil})
	} 
	return c.JSON(fiber.Map{"status": "success",
							"message": "Notes found",
							"data": note})
}

func UpdateNote(c *fiber.Ctx) error {
	type updateNote struct {
		Title  string `json: "Title"`
		Subtitle string `json:"sub_title"`
		Text string `json:"Text"`
		AddText string `json:"AddText"`
	}

	db := database.DB
	var note model.Note

	id := c.Params("noteId")
	db.Find(&note, "id = ?", id)
	if note.ID == uuid.Nil {
		return c.Status(404).JSON(fiber.Map{"status": "error",
											"message": "no notes",
											"data": nil})
	}	
	var updateNoteData updateNote
	err := c.BodyParser(&updateNoteData)
	if err != nil {
		return c.Status(500).JSON(fiber.Map{"status":"error",
											"message": "no review notes",
											"data": err})
	}
	// edit
	note.Title = updateNoteData.Title
	note.Subtitle = updateNoteData.Subtitle
	note.Text = updateNoteData.Text
	note.AddText = updateNoteData.AddText

	// save
	db.Save(&note)
	return c.JSON(fiber.Map{"status": "success",
							"message": "Notes found",
							"data": note})
}

func DeleteNote(c *fiber.Ctx) error {
	db := database.DB
	var note model.Note

	// id 
	id := c.Params("noteId")
	// find
	db.Find(&note, "id = ?", id)

	// no such 
	if note.ID == uuid.Nil {
		return c.Status(404).JSON(fiber.Map{"status": "error",
		"message": "Notes no",
		"data": nil})
	}
	err := db.Delete(&note, "id = ?", id).Error
	if err != nil {
		return c.Status(404).JSON(fiber.Map{"status": "error",
		"message": "Notes found",
		"data": nil})
	}
	return c.JSON(fiber.Map{"status": "succes",
						"message": "Delete Succes"})
}