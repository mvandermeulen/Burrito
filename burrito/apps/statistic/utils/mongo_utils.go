package utils

import (
	"context"
	"fmt"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var mongoConnectStr string = "mongodb://%s:%s@%s:%d/"

func MongoCreateContext() (context.Context, context.CancelFunc) {
	mongoCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	return mongoCtx, cancel
}

func MongoCreateClient(mongoCtx *context.Context) *mongo.Client {
	client, err := mongo.Connect(
		*mongoCtx,
		options.Client().ApplyURI(
			fmt.Sprintf(
				mongoConnectStr,
				GetConfig().MONGO_USER,
				GetConfig().MONGO_PASSWORD,
				GetConfig().MONGO_HOST,
				GetConfig().MONGO_PORT,
			),
		),
	)
	if err != nil {
		GetLogger().Critical(err)
	}
	MongoPing(mongoCtx, client)
	return client
}

func MongoPing(mongoCtx *context.Context, client *mongo.Client) {
	err := client.Ping(*mongoCtx, nil)
	if err != nil {
		GetLogger().Critical(err)
	}
}

func MapToMongoFilters(mapFilters map[string]any) bson.D {
	_filters := bson.D{}
	for key, value := range mapFilters {
		_filters = append(_filters, primitive.E{Key: key, Value: value})
	}

	return _filters
}
