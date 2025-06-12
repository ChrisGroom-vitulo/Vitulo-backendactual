from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import auth
from app.database import SessionLocal, engine
from app.models import User
from app.database import Base
from passlib.hash import bcrypt

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"message": "Vitulo Backend is running"}

# Create default admin user if not present
def create_default_admin():
    db = SessionLocal()
    user = db.query(User).filter(User.username == "admin").first()
    if not user:
        admin = User(username="admin", hashed_password=bcrypt.hash("admin123"), role="admin")
        db.add(admin)
        db.commit()
        print("✅ Default admin created: admin / admin123")
    db.close()

create_default_admin()