# from urllib import 
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: str
# products = []
# id = 0