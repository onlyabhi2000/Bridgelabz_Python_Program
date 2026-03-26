Working of FastAPI

| Layer                       | Description                                                              |
| --------------------------- | ------------------------------------------------------------------------ |
| **Client**                  | Sends HTTP requests to your API (e.g. `GET /users/1`)                    |
| **ASGI Server (Uvicorn)**   | Handles the HTTP connection and passes the request to FastAPI            |
| **FastAPI App**             | Routes the request to the correct function using dependency injection    |
| **Path Operation Function** | Your defined function that returns a response (e.g., `def get_user(id)`) |
| **Pydantic Models**         | Validate and serialize/deserialize request and response data             |
| **Middleware (Optional)**   | Code that runs before/after the main logic (e.g., CORS, logging)         |
| **Response Generator**      | Converts your return value (e.g., dict) to a valid HTTP response         |


----------------------------------------------------------------------------------------------------------------------

```Here both the endpoints will work , because it doesnot matter the function name , only matter the decorator ```

@app.get('/greet')
def index():
    return "heyy"

@app.get('/no-greet')
def index():
    return "heyy"

----------------------------------------------------------------------------------------------------------------------

Tip
Always place static paths first, then dynamic ones: because In FastAPI (and Starlette,
which it's built on), routes are matched in the order they’re defined

✅ Good:
/blog/unpublished
/blog/{id}

❌ Bad:
/blog/{id}
# /blog/unpublished will never be reached!
/blog/unpublished

----------------------------------------------------------------------------------------------------------------------
