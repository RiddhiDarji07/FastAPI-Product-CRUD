from fastapi import FastAPI, Response

from routes.productRouter import ProductRouter

app = FastAPI()

app.include_router(ProductRouter)

#pip install -r requirements.txt
#uvicorn main:app --reload