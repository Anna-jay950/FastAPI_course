from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

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


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"items": items, "title": "Home"})


@app.get("/api")
def home_api():
    return {"message": "Hello World"}


@app.get("/api/posts")
def get_posts(): 
    return items   


# To run this FastAPI application, you can use the following command in your terminal:
# uvicorn main:app --reload
