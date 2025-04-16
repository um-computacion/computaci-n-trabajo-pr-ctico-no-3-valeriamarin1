import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestNumeroValido(unittest.TestCase):
    
    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)
    
    @patch('builtins.input', return_value='25')
    def test_ingreso_feliz_25(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 25)
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo) as contexto:
            ingrese_numero()
        self.assertEqual(str(contexto.exception), 'El número debe ser positivo')

if __name__ == '__main__':
    unittest.main()
