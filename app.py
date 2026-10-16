"""Aplicación de prueba para el pipeline de CI."""


def sumar(a: int, b: int) -> int:
    """Devuelve la suma de dos números."""
    return a + b


def saludar(nombre: str) -> str:
    """Devuelve un saludo personalizado."""
    return f"Hola, {nombre}!"


def main() -> None:
    print(saludar("DevOps Apocalipsis"))
    print(f"2 + 3 = {sumar(2, 3)}")


if __name__ == "__main__":
    main()
