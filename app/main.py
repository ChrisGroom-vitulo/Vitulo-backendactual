from fastapi import FastAPI
from app import auth, payments, reports, kill_data, upload, cts_integration, mapping

app = FastAPI()

app.include_router(auth.router)
app.include_router(payments.router)
app.include_router(reports.router)
app.include_router(kill_data.router)
app.include_router(upload.router)
app.include_router(cts_integration.router)
app.include_router(mapping.router)
