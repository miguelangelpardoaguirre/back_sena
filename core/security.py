
from passlib.context import CryptContext

# Configurar hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")

# Función para generar un hashed_password
def get_hashed_password(password: str):
    return pwd_context.hash(password)