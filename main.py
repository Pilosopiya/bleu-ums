from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

# routers
from routers import users
from routers import auth

app = FastAPI(title="Retail Auth Service")

# include routers
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(users.router, prefix='/users', tags=['users'])


# CORS setup to allow frontend and backend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # SUSUNTUKIN Q GOMALAW
        "https://bleu-ums.vercel.app", # ums frontend
        "https://bleu-pos-eight.vercel.app", # pos frontend
        "https://bleu-ims.vercel.app", # ims frontend
        "https://bleu-oos.vercel.app", # oos frontend

        "https://product-services-1.onrender.com",#product services
        "https://ingredient-services.onrender.com", #ingredient services
        "https://material-service.onrender.com", #material services
        "https://merchandise-service.onrender.com", #merchandise services
        "https://recipe-service-npf6.onrender.com", #recipe services
        "https://waste-service.onrender.com", #waste services
        "https://discount-services.onrender.com", #discount services
        "https://sales-service-bm35.onrender.com", #sales services
        "https://ordering-service.onrender.com", #ordering services
        "https://payment-service-oo77.onrender.com", #payment services
        
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# run app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=4000, host="127.0.0.1", reload=True)
    