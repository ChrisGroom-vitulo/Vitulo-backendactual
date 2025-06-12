from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import auth, upload, kill_data, payments, reports, mapping, cts_integration

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(kill_data.router)
app.include_router(payments.router)
app.include_router(reports.router)
app.include_router(mapping.router)
app.include_router(cts_integration.router)

@app.get("/")
def read_root():
    return {"message": "Vitulo Backend is running"}
