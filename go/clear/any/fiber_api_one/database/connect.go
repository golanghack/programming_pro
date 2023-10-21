package database

import (
	"fmt"
	"log"
	"strconv"

	"github.com/golanghack/programming_pro/tree/go/go/clear/any/fiber_api_one/config"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// Declare variable
var DB *gorm.DB 

// Connect to DB
func ConnectDB() {
	var err error 
	p := config.Config("DB_PORT")
	port, err := strconv.ParseUint(p, 10, 32)

	if err != nil {
		log.Println("NOTNOTNOT")
	}

	dsn := fmt.Sprintf("host=%s port=%d user=%s password%s dbname=%s sslmode=disable",
						config.Config("DB_HOST"),
						port,
						config.Config("DB_USER"),
						config.Config("DB_PASSWORD"),
						config.Config("DB_NAME"))
	// connect to DB the variable DB
	DB, err = gorm.Open(postgres.Open(dsn))

	if err != nil {
		panic("FAIL!")
	}
	fmt.Println("Connection to DB")
} 