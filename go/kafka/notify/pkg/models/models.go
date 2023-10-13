package models

type User struct {
    ID int `json:"id"`
    Name string `json:"name"`
}

type Notification struct {
    From User           `json:"From"`
    To User             `json:"To"`
    Message string      `json:"message"`
}