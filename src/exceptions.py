class NumeroDebeSerPositivo(Exception):
    def __init__(self):
        super().__init__('El número debe ser positivo')
