from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.user_view import UserView  # CBV view
import uvicorn

app = FastAPI(
    title="User CRUD API",
    description="FastAPI + CBV + Async + Repository + Service architecture",
    version="1.0.0"
)

# CORS agar kerak bo‘lsa (frontend uchun)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # yoki ["http://localhost:3000"] frontend domeni
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# UserView ni ulash
user_view = UserView()
app.include_router(user_view.router, prefix="/users", tags=["Users"])

# Run server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
