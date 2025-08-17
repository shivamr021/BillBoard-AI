from fastapi import FastAPI
from routes import analyze, reports

app = FastAPI()

app.include_router(analyze.router)
app.include_router(reports.router)
