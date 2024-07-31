from app.repositories.usuario import read_usuario

def authenticate_user(email: str, password: str):
    user = read_usuario(email)
    if user is None or user["password"] != password:
        return False
    return user
