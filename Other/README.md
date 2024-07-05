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

## Event Sample for test coder

```
{"Values": [1.5961, 1, -1, 0, 1,0,0,18,0,1500,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,999,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
```