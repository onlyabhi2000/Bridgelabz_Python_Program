from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

@app.get('/')
def index():
    return {"data" : "blog list"}

##Query paramater
##i want 10 blogs only
@app.get('/blog')
def index(limit):
    return {"data" : f'{limit} only blogs'}

@app.get('/blog/unpublished')
def show(id : int):
    return {"data" : "unpublished ocmments"}

# Note by default id will be treated a string so , we need to declare explicitly as int
# @app.get('/blog/{id}')
# def show(id):
#     return {"data" : id}

@app.get('/blog/{id}')
def show(id : int):
    return {"data" : id}


##Query paramater
##i want 10 blogs only
@app.get('/blog')
def index(limit , published : bool):
    if published:
        return {"data" : f'{limit} only Tr blogs'}
    else:
        return {"data" : f'{limit} only FL blogs'}



## impiortant : to use the post method we have to use the pydanyic model
# where we havto create tye actual model 

class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool]


@app.post('/blog')
def create_post(blog:Blog):
    return { "data" : f"post created anf created the schema, here is {blog.title} "}