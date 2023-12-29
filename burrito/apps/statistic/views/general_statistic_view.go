package views

import (
	"BurritoStatistic/models"
	"BurritoStatistic/utils"
	"encoding/json"
	"time"

	"github.com/gofiber/fiber/v2"
)

func GetGeneralStatistic(ctx *fiber.Ctx) error {
	tokenPayload := utils.ValidateJWTAndCheckPermission(ctx)
	if tokenPayload == nil {
		return nil
	}

	requestBody := models.GeneralStatisticRequest{}
	ctx.BodyParser(&requestBody)

	if !utils.IsValidGeneralStatisticRequest(&requestBody) {
		requestBody.From = time.Now().Format("2006-01-02")
		requestBody.To = time.Now().AddDate(0, 0, -7).Format("2006-01-02")
	}

	db := utils.GetDatabase()

	var generalStatisticInstance = models.GeneralStatisticModel{}

	db.Table("tickets").Select("COUNT(*)").Count(&generalStatisticInstance.Global.TicketsCount)
	db.Table("tickets").Select("status_id, COUNT(*) AS count").Group("status_id").Find(&generalStatisticInstance.Global.Statuses)

	db.Table("tickets").Select("DATE(created) date, status_id, COUNT(*) tickets_count").Group("status_id, date").Find(&generalStatisticInstance.Period)

	statisticResponse, _ := json.Marshal(generalStatisticInstance)
	return ctx.JSON(string(statisticResponse))
}
