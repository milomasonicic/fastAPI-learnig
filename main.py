from fastapi import FastAPI
from routes.user import router
from core.database import engine, Base  # Importuj engine i Base
from models.user import User  # Importuj User model


app = FastAPI(debug=True)

app.include_router(router)

# Kreiranje svih tabela koje su definisane u modelima
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}




  
