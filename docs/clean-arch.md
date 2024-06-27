## App directories

```
.
├── docs/ - extra docs, like api endpoints, postman collection, etc
└── services/
    └── distance-api/ - flask api to calculate distance between two addresses and get historical data
```

### Service directories

```
.
├── src/
│   ├── api/ - application
│   ├── controllers/ - redirect calls to use cases and send response
│   ├── external/ - external services, like database connection, distance calculator service and coordinates service
│   ├── gateways/ - data resources abstraction for use cases
│   ├── interfaces/ - application interfaces
│   └── use_cases/ - use cases
└── test/
    └── unit/ - unit tests
```

## Clean Architecture

Clean architecture image used as inspiration:

![Clean Architecture](img/CleanArchitecture.jpg)
