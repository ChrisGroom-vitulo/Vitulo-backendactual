
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth import router as auth_router
from app.routes import router as cattle_router
from app.upload import router as upload_router
from app.kill_data import router as kill_router
from app.payments import router as payments_router
from app.reports import router as reports_router
from app.mapping import router as mapping_router
from app.cts_integration import router as cts_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(cattle_router, prefix="/cattle")
app.include_router(upload_router, prefix="/upload")
app.include_router(kill_router, prefix="/kill")
app.include_router(payments_router, prefix="/payments")
app.include_router(reports_router, prefix="/reports")
app.include_router(mapping_router, prefix="/map")
app.include_router(cts_router, prefix="/cts")
