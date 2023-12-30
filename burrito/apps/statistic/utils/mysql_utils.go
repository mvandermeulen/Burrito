package utils

import (
	"fmt"
	"sync"

	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

var dsn string = "%s:%s@tcp(%s:%d)/%s?charset=utf8mb4&parseTime=True&loc=Local"
var db *gorm.DB = nil

func GetDatabase() *gorm.DB {
	var once sync.Once
	once.Do(func() {
		db, _ = gorm.Open(
			mysql.Open(
				fmt.Sprintf(
					dsn,
					GetConfig().MYSQL_USER,
					GetConfig().MYSQL_PASSWORD,
					GetConfig().DB_HOST,
					GetConfig().DB_PORT,
					GetConfig().MYSQL_DATABASE,
				),
			),
			&gorm.Config{},
		)
	})
	return db
}

var adminRoles = []any{9, 10}

type userAdminData struct {
	RoleID int `json:"role_id"`
}

func CheckForAdmin(user_id int) bool {
	var userMetaData userAdminData
	userMetaData.RoleID = -1
	GetDatabase().Table("users").Select("role_id").Where("user_id = ?", user_id).Find(&userMetaData)

	return Contains(adminRoles, userMetaData.RoleID)
}