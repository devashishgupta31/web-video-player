from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse
from server import env

router = APIRouter(prefix="/app", tags=["main"])

@router.get("/", name="home")
def home() -> RedirectResponse:
    return RedirectResponse(env.WELCOME_HTML_URL, status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/login")
def login() -> RedirectResponse:
    return RedirectResponse(env.LOGIN_HTML_URL, status.HTTP_307_TEMPORARY_REDIRECT)


@router.get("/signup")
def login() -> RedirectResponse:
    return RedirectResponse(env.SIGNUP_HTML_URL, status.HTTP_307_TEMPORARY_REDIRECT)
