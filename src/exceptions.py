# src/exceptions.py

class NumeroDebeSerPositivo(Exception):
    def __init__(self, mensaje="El número debe ser positivo"):
        super().__init__(mensaje)


