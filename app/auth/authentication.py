from fastapi import APIRouter, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from app.db.session import get_db
from fastapi.param_functions import Depends

from app.models.user import UserModel
from app.db.hash import Hash

from app.auth import oauth2

router = APIRouter()

# Crea un token JWT con la identidad del usuario autenticado.
@router.post('/token')
def get(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  user = db.query(UserModel).filter(UserModel.name == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  
  if not Hash.verify_password( request.password, user.hashed_password ):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
  
  access_token = oauth2.create_access_token(data={'sub': user.name})

  return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user_id': user.id_user,
    'username': user.name
  }