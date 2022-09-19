import uvicorn
from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI()

app.include_router(api_router, prefix=settings.API_PREFIX)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
