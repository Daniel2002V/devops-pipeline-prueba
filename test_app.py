from app import saludar, sumar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0


def test_saludar():
    assert saludar("DevOps") == "Hola, DevOps!"
