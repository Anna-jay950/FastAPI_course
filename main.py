from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

items: list[dict] = [
    {"id": 1,
      "name": "Item 1", 
      "description": "This is the first item."
      },
    {
        "id": 2, 
        "name": "Item 2", 
        "description": "This is the second item."
     },
    {
        "id": 3, 
        "name": "Item 3", 
        "description": "This is the third item."
    },
]


@app.get("/api/posts", response_class=HTMLResponse, include_in_schema=False)

@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{items[0]['id']}</h1>"


@app.get("/api")
def home_api():
    return {"message": "Hello World"}


@app.get("/")
def get_posts():
    return items


# To run this FastAPI application, you can use the following command in your terminal:
# uvicorn main:app --reload
