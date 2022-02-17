from .models import (
    TurlaUserToken,
)
import os
import uuid
from django.utils import timezone
from django.conf import settings
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_KEY = settings.SECRET_KEY
_VECTOR_SIZE = 16

def get_user_from_token(token):
    try:
        user_token = TurlaUserToken.objects.get(
            token = token,
        )
        return user_token.appuser
    except TurlaUserToken.DoesNotExist:
        return None


def create_token_for_user(turla_user, user_agent):
    token = uuid.uuid4().hex
    client_token = TurlaUserToken.objects.create(
        turla_user = turla_user,
        token = token,
        user_agent = user_agent,
    )
    return token


#function for turning data into 256 bytes
def _get_hash(data):
    digest = hashes.Hash(hashes.SHA256())
    bytes = data.encode('utf-8')
    digest.update(bytes)
    return digest.finalize()


#function for encrypting data using AES
def encrypt(text):
    #First we want to turn key into 256 byte representation!
    key = _get_hash(_KEY)
    #Then turn text into bytes
    text = text.encode('utf-8')

    #Adding padding to the bytes
    padder = padding.ANSIX923(256).padder()
    padded_data = padder.update(text) + padder.finalize()

    initialization_vector = os.urandom(_VECTOR_SIZE)

    cipher = Cipher(algorithms.AES(key), modes.CBC(initialization_vector))
    encryptor = cipher.encryptor()
    encrypted_text = initialization_vector + encryptor.update(padded_data) + encryptor.finalize()
    return encrypted_text.hex()


#function for decrypting AES
def decrypt(text):
    encrypted = bytes.fromhex(text)
    initialization_vector, b = encrypted[:_VECTOR_SIZE], encrypted[_VECTOR_SIZE:]
    unpadder = padding.ANSIX923(256).unpadder()
    key = _get_hash(_KEY)
    cipher = Cipher(algorithms.AES(key), modes.CBC(initialization_vector))
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(b) + decryptor.finalize()
    unpadded_text = unpadder.update(decrypted_text) + unpadder.finalize()
    text = unpadded_text.decode('utf-8')
    return text


def create_time_stamp(phone_number):
    return [str(phone_number), timezone.now().strftime("%Y-%m-%d %H:%M:%S")]
