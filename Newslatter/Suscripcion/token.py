import jwt


def encode_user(correo):
    """
    encode user payload as a jwt
    :param user:
    :return:
    """
    encoded_data = jwt.encode(payload={"correo": correo},
                              key='secret',
                              algorithm="HS256",)
    





    return encoded_data

def decode_user(token_encriptado):
   clave_secreta ='secret'
   datos_desencriptados = jwt.decode(token_encriptado, clave_secreta, algorithms=["HS256"])
   correo_desencriptado = datos_desencriptados["correo"]
   return correo_desencriptado
