# Não esqueça de abrir o terminal para instalar os módulos. Ex: pip install mock, pip install coverage

import unittest
import coverage
import webbrowser
import os
from calculo_media import calcular_media

class TestCalcularMedia(unittest.TestCase):
    def test_media_lista_inteiros(self):
        # Teste para lista de inteiros
        lista = [1, 2, 3, 4, 5]
        resultado = calcular_media(lista)
        self.assertEqual(resultado, 3.0)

    def test_media_lista_floats(self):
        # Teste para lista de floats
        lista = [1.5, 2.5, 3.5]
        resultado = calcular_media(lista)
        self.assertAlmostEqual(resultado, 2.5)

    def test_media_lista_vazia(self):
        # Teste para lista vazia
        lista = []
        with self.assertRaises(ValueError):
            calcular_media(lista)

    def test_media_lista_negativos(self):
        # Teste para lista com números negativos
        lista = [-1, -2, -3, -4, -5]
        resultado = calcular_media(lista)
        self.assertEqual(resultado, -3.0)

    def test_media_lista_strings(self):
        # Teste para lista contendo strings
        lista = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            calcular_media(lista)
    
if __name__ == '__main__':
    # Criar uma instância do Coverage com o arquivo .coveragerc
    cov = coverage.Coverage(config_file='.coveragerc')

    # Iniciar a medição da cobertura
    cov.start()

    # Executar os testes
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalcularMedia)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Encerrar a medição da cobertura após os testes
    cov.stop()

    # Salvar os dados de cobertura em um arquivo
    cov.save()
    cov.html_report(directory='htmlcov')

    # Abra o relatório no navegador
    index_file = os.path.join('htmlcov', 'index.html')
    webbrowser.open('file://' + os.path.abspath(index_file))

    # Adicionar uma pausa antes de finalizar
    input("Pressione Enter para sair...")