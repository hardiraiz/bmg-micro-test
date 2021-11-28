- POST http://localhost:7020/login
```json
request:
{
    "email":"test@gmail.com",
    "password":"password"
}

response:
{
    "id":"string"
}
```

- POST http://localhost:7020/register
```json
request:
{
    "email":"test@gmail.com",
    "password":"password"
}
response:
{
    "message":"registration success"
}
error:
{
    "message":"registration failed"
}
```
- GET http://localhost:7020/list
```json
response:
{
    "message":"success",
    "data":[
        {
            "message":"success",
            "email":"test2@gmail.com"
        },
        {
            "message":"success",
            "email":"test3@gmail.com"
        },
        {
            "message":"success",
            "email":"test4@gmail.com"
        }
    ]
}
error:
{
    "message":"success",
    "data":[]
}

```
- http://localhost:7020/edit-data
- http://localhost:7020/find-user
- http://localhost:7020/ref-input
- http://localhost:7020/hero-search