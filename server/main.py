from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from server import env
from server.router import home

app = FastAPI(version="1.0.0")
app.mount('/ui' ,StaticFiles(directory=env.STATIC_FILES_PATH, html=True), name='app-ui')
app.include_router(home.router)

@app.get("/")
def get_home() -> RedirectResponse:
    return RedirectResponse(home.router.url_path_for("home"), status.HTTP_307_TEMPORARY_REDIRECT)

