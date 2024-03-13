# Não esqueça de abrir o terminal para instalar os módulos. Ex: pip install mock

import unittest
import coverage
import webbrowser
import os
import mock
from calculadora import adicao, subtracao, multiplicacao, divisao, calculadora, potenciacao

class TestCalculadora(unittest.TestCase):
    def test_adicao(self):
        resultado = adicao(2,2)
        self.assertAlmostEqual(resultado, 4.0)
    
    def test_subtracao(self):
        resultado = subtracao(7,3)
        self.assertAlmostEqual(resultado, 4.0)
    
    def test_multiplicacao(self):
        resultado = multiplicacao(9,9)
        self.assertAlmostEqual(resultado, 81.0)

    def test_divisao(self):
        resultado = divisao(30,10)
        self.assertAlmostEqual(resultado, 3.0)

    def test_potenciacao(self):
        resultado = potenciacao(10,2)
        self.assertAlmostEqual(resultado, 100.0)

    def test_erro_divisao(self):
        with self.assertRaises(ValueError):
            divisao(30,0)

    def test_menu1(self):
        with mock.patch('builtins.input', return_value='1'):
            assert calculadora() == 1

    def test_menu2(self):
        with mock.patch('builtins.input', return_value='2'):
            assert calculadora() == 2

    def test_menu3(self):
        with mock.patch('builtins.input', return_value='3'):
            assert calculadora() == 3

    def test_menu4(self):
        with mock.patch('builtins.input', return_value='4'):
            assert calculadora() == 4

    def test_menu5(self):
        with mock.patch('builtins.input', return_value='5'):
            assert calculadora() == 5
    
    def test_menu_error(self):
        with mock.patch('builtins.input', return_value='0'):
            assert calculadora() == 0
    
if __name__ == "__main__":
    # Criar uma instância do Coverage com o arquivo .coveragerc
    cov = coverage.Coverage(config_file='.coveragerc.txt')

    # Iniciar a medição da cobertura
    cov.start()

    # Executar os testes
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculadora)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Encerrar a medição da cobertura após os testes
    cov.stop()

    # Salvar os dados de cobertura em um arquivo
    cov.save()
    cov.html_report(directory='htmlcov')

    # Abra o relatório no navegador
    index_file = os.path.join('htmlcov', 'index.html')
    webbrowser.open('file://' + os.path.abspath(index_file))