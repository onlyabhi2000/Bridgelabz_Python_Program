from pydantic import BaseModel
### Pydantic Schema
class Blog(BaseModel):
    title : str
    body : str
