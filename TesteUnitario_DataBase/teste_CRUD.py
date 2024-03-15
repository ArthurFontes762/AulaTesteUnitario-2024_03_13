# Não esqueça de abrir o terminal para instalar os módulos. Ex: pip install mock, pip install coverage

import unittest
import coverage
import webbrowser
import os
#import mock
from CRUD import UsersCRUD

class TestUsersInCRUD(unittest.TestCase):
    def setUp(self):
        self.crud = UsersCRUD()
        self.crud.create_user("Alberto", 29)
        self.crud.create_user("Calci", 42)
        self.crud.create_user("Falcon", 36)

    def test_create_user(self):
        new_user = self.crud.create_user("Ari", 48)
        self.assertIn(new_user, self.crud.users)

    def test_read_users(self):
        users = self.crud.read_users()
        self.assertEqual(len(users), 3)
    
    def test_update_user(self):
        updated_user = self.crud.update_user(1, "Updated Calci", 21)
        self.assertEqual(updated_user["name"], "Updated Calci")
        self.assertEqual(updated_user["age"], 21)

    def test_delete_user(self):
        deleted_user = self.crud.delete_user(0)
        self.assertEqual(deleted_user["name"], "Alberto")
        self.assertEqual(len(self.crud.users), 2)

if __name__ == "__main__":
    # Criar uma instância do Coverage com o arquivo .coveragerc
    cov = coverage.Coverage(config_file='.coveragerc.txt')

    # Iniciar a medição da cobertura
    cov.start()

    # Executar os testes
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUsersInCRUD)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Encerrar a medição da cobertura após os testes
    cov.stop()

    # Salvar os dados de cobertura em um arquivo
    cov.save()
    cov.html_report(directory='htmlcov')

    # Abra o relatório no navegador
    index_file = os.path.join('htmlcov', 'index.html')
    webbrowser.open('file://' + os.path.abspath(index_file))