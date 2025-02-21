import uvicorn

from app.config.settings import settings
from app.utils.constants import MODE

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app",
        reload=settings.mode == MODE.DEV,
        port=settings.port,
        host=settings.host,
        workers=4 if settings.mode == MODE.PROD else None,
    )
