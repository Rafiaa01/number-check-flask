# Number API — Task A

A small Flask API that checks a number and returns basic facts about it.

## Endpoint

POST `/check`

### Input

```json
{
  "number": 7
}
```

### Validation

The API accepts the request only when:

The body is valid JSON.
`number` is present.
`number` is a whole integer.
Strings, decimals, and booleans are rejected.
The number is between 1 and 1000.

Invalid requests return 400 Bad Request with a JSON error message.

### Valid Response

```json
{
  "number": 7,
  "is_even": false,
  "is_prime": true,
  "square": 49
}
```

### Example Error

```json
{
  "error": "number must be between 1 and 1000"
}
```

## Technologies

Python
Flask

## Run the Application

```bash
python flask_app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
 ```
