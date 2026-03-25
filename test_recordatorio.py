import unittest
from recordatorios import generar_recordatorio

class TestRecordatorio(unittest.TestCase):

    def test_generar_recordatorio_valido(self):
        resultado = generar_recordatorio("Estudiar TDD")
        self.assertEqual(resultado, "Recordatorio: Estudiar TDD")

if __name__ == "__main__":
    unittest.main()
