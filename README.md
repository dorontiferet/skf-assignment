# skf-assignment
A simple web service for storing and retrieving text messages using Redis as a database.

## Running:
To run the application and the DB in docker:
```
docker-compose up
```

## Testing:
Powered by pytest:
```
pytest
```

## Usage:
### Publish a message:
`POST /messages/publish`
```
curl -H "Content-Type: application/json" -X POST -d "{\"content\":\"this is the content of the message\"}" http://localhost:5000/messages/publish
```

### Retrieve last message:
`GET /messages/getLast`
```
curl http://localhost:5000/messages/getLast
```

### Retrieve all messages between timeframes:
`GET /messages/getByTime?start=START&end=END`

*start, end - optional timestamps
```
curl "http://localhost:5000/messages/getByTime?start=1600000000&end=1700000000"
```

