from pathlib import Path

ROOT = Path(__file__).parent.parent
print("root", ROOT)
STATIC_FILES_PATH = f'{ROOT}/ui'
WELCOME_HTML_URL = "/ui/statics/welcome.html"
LOGIN_HTML_URL = "/ui/statics/login.html"
SIGNUP_HTML_URL = "/ui/statics/signup.html"
