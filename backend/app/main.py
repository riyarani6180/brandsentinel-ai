
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import Base, engine
from app import models

# Import API routers
from app.api.auth import router as auth_router
from app.api.guidelines import router as guidelines_router
from app.api.approved_facts import router as approved_facts_router
from app.api.review_submissions import router as review_submissions_router
from app.api.review_findings import router as review_findings_router
from app.api.review_comments import router as review_comments_router
from app.api.user_management import router as user_management_router
from app.api.audit_logs import router as audit_logs_router
from app.api.compliance import router as compliance_router
from app.api.brand_assets import router as brand_assets_router
from app.api.document_upload import router as document_upload_router


# Create database tables
Base.metadata.create_all(bind=engine)


# Initialize FastAPI application
app = FastAPI(
    title="BrandSentinel API",
    description="An Intelligent Brand-Governance Platform",
    version="1.0.0"
)


# Configure CORS for React frontend


app.add_middleware(
    CORSMiddleware,

allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://brandsentinel-teal.vercel.app",
    "https://brandsentinel-fgqfolntl-riyarani6180.vercel.app",
    "https://brandsentinel-c34akzov0-riyarani6180.vercel.app",
    "https://brandsentinel-xu17-4xu0s4pmg-riyarani6180.vercel.app",
    "https://brandsentinel-21lm-git-round-3-submission-riyarani6180.vercel.app",
    "https://brandsentinel-ai-six.vercel.app",
],


    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




# Register API routers
app.include_router(auth_router)
app.include_router(guidelines_router)
app.include_router(approved_facts_router)
app.include_router(review_submissions_router)
app.include_router(review_findings_router)
app.include_router(review_comments_router)
app.include_router(user_management_router)
app.include_router(audit_logs_router)
app.include_router(compliance_router)
app.include_router(brand_assets_router)
app.include_router(document_upload_router)


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to BrandSentinel API",
        "status": "running"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "BrandSentinel"
    }
