from fastapi import  HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials):
    correct_username = secrets.compare_digest(credentials.username, os.environ["LOGIN"])
    correct_password = secrets.compare_digest(credentials.password, os.environ["PASS"])
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )