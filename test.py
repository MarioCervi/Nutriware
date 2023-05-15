import app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    # Prueba que se acceda correctamente a la URL
    def test_transactions(self):
        response = self.app.get('/buscador', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Prueba que busca alimentos correctamente
    def test_alimento_correcto(self):
       response = self.app.post('/buscador', data = dict(buscador="nutella", login_form=""), follow_redirects=True)
       self.assertEqual(response.status_code, 200)
       
    #Prueba que busca alimentos escritos con mayusculas
    def test_alimento_mayus(self):
       response = self.app.post('/buscador', data = dict(buscador="NUTELLA", login_form=""), follow_redirects=True)
       self.assertEqual(response.status_code, 200)
    
    #Prueba que busca alimentos escritos con mayusculas y minusculas
    def test_alimento_mix(self):
       response = self.app.post('/buscador', data = dict(buscador="NuTeLlA", login_form=""), follow_redirects=True)
       self.assertEqual(response.status_code, 200)
       
    #Prueba de que si introduces un numero se maneja el error.
    def test_alimento_num(self):
       response = self.app.post('/buscador', data = dict(buscador="1234", login_form=""), follow_redirects=True)
       self.assertEqual(response.status_code, 200)
    
    #Prueba de que si introduces un simbolo se maneja el error.
    def test_alimento_simbol(self):
       response = self.app.post('/buscador', data = dict(buscador="prueba/*/", login_form=""), follow_redirects=True)
       self.assertEqual(response.status_code, 200)
       
if __name__ == '__main__':
    unittest.main()