from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import auth, upload, reports, mapping, kill_data, payments, cts_integration

app = FastAPI()

# Allow CORS for local frontend dev and deployment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router, prefix="/auth")
app.include_router(upload.router, prefix="/upload")
app.include_router(reports.router, prefix="/reports")
app.include_router(mapping.router, prefix="/mapping")
app.include_router(kill_data.router, prefix="/kill")
app.include_router(payments.router, prefix="/payments")
app.include_router(cts_integration.router, prefix="/cts")

@app.get("/")
def read_root():
    return {"message": "Vitulo Backend is running"}

