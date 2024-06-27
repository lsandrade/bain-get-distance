## API

## 1. GET `/distance`

Returns the distance between two addresses.

Body (example)
```json
{
    "source_address": "1600 Amphitheatre Parkway, Mountain View, CA",
    "destination_address": "Rua da Consolação, 930, São Paulo, SP"
}
```

Response (example)
```json
{
    "distance": 10388.021264393856
}
```

## 2. GET `/distance/historical`

Returns the historical data of the queries.

Response (example):
```json
[
    {
        "destination_address": "Rua da Consolação, 930, São Paulo, SP",
        "distance": 10388.021264393856,
        "source_address": "1600 Amphitheatre Parkway, Mountain View, CA"
    }
]
```