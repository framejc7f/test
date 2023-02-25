import pyperclip
from nickname_generator import generate

def getBuffer()-> str:
    return pyperclip.paste()


def getNickname()-> str:
    return generate()