import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from app.admin.views import UserAdmin
from app.database import async_engine

app = FastAPI()
admin = Admin(app, async_engine, title="Admin Panel")
admin.add_view(UserAdmin)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)