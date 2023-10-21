package config

import (
	"fmt"
	"os"

	"github.com/joho/godotenv"
)

// Env func
func Config(key string) string {
	// load 
	err := godotenv.Load(".env")
	if err != nil {
		fmt.Print("Error loading environment")
	}
	return os.Getenv(key)
}