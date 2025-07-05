from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import upload, analyze, report  # Will create these next

app = FastAPI(title="GPT PayAudit")

# Enable CORS for frontend (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to frontend URL in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registrations
app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(report.router)

@app.get("/ping")
def ping():
    return {"message": "✅ Backend running"}
