package database

import (
	"fmt"
	"log"
	"strconv"

	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/config"
	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/internal/model"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// Declare the variable for the database
var DB *gorm.DB

// ConnectDB connect to db
func ConnectDB() {
    var err error
    p := config.Config("DB_PORT")
    port, err := strconv.ParseUint(p, 10, 32)

    if err != nil {
        log.Println("Not")
    }

    // Connection URL to connect to Postgres Database
    dsn := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable", config.Config("DB_HOST"), port, config.Config("DB_USER"), config.Config("DB_PASSWORD"), config.Config("DB_NAME"))
    // Connect to the DB and initialize the DB variable
    DB, err = gorm.Open(postgres.Open(dsn))

    if err != nil {
        panic("failed to connect database")
    }

    fmt.Println("Connection Opened to Database")

    // migrations
    DB.AutoMigrate(&model.Note{})
    fmt.Println("Migrated")
}