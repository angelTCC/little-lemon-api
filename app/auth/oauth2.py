from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta, timezone
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authentication/token")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
)
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  # add expiration: data= {"sub": "johndoe"}
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  # sign JWT
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt