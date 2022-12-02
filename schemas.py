from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title : str
    body : str

