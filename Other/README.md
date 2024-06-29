## Event Sample

```
{"Values": [1.1, 2.2]}
```

## Test function locally

start function

```
docker run --platform linux/amd64 -p 9000:8080 lambda-c-function:test
```

call function (Unix style)

```
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"Values":[1.1, 2.2]}'
```

call function (Windows style)

```
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{\"Values\":[1.1, 2.2]}"
```