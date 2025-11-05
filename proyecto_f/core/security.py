import datetime
from jose import JWTError
from passlib.context import CryptContext
from core.config import settings
import jwt

# Configurar hashing de contraseñas
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Función para generar un hashed_password
def get_hashed_password(password: str):
    return pwd_context.hash(password) 

# Función para verificar una contraseña hashada
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Función para crear un token JWT
def create_access_token(data: dict): 
    to_encode = data.copy()
    expire = datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=settings.jwt_access_token_expire_minutes) # toma la fecha y hora en que se ejecuta y le agrega un tiempo que viene de JWT_ACCESS_TOKEN_EXPIRE_MINUTES en .env 
    to_encode.update({"exp": expire}) # agrgar datos con el .update
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm) #codifica el token
    return encoded_jwt

# Función para verificar si un token JWT es valido
async def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]) # decodifica el token
        user_id = payload.get("sub")
        return int(user_id) if user_id is not None else None
    except jwt.ExpiredSignatureError: # Token ha expirado
        return None
    except JWTError:
        return None
