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

    ## Prueba que haga login correctamente
    #def test_correct_login(self):
    #    response = self.app.post('/login', data = dict(login="kepa", login_form=""), follow_redirects=True)
    #    self.assertEqual(response.status_code, 200)
#
    ## Prueba que se pueda fallar el login
    #def test_incorrect_login(self):
    #    response = self.app.post('/login', data = dict(login="maria", login_form=""), follow_redirects=True)
    #    self.assertEqual(response.status_code, 400)
#
    ## Prueba que se hagan transacciones correctas
    #def test_correct_transaction(self):
    #    response = self.app.post('/transaction', data = dict(origen="gbgbgbgbgbgbgbgbgbgbgbgbgbgbgb1234", destino="asdasdasdaasdasdasdaasdasdasda1234", cantidad="123"), follow_redirects=True)
    #    self.assertEqual(response.status_code, 200)
    #    
    ## Prueba que se hagan transacciones incorrectas
    #def test_incorrect_transaction(self):
    #    response = self.app.post('/transaction', data = dict(origen="asdasdasdaasdasdasdaasdasdasda1234", destino="abl", cantidad="800"), follow_redirects=True)
    #    self.assertEqual(response.status_code, 400)
#
    ## Prueba que si se mete la cantidad correcta de dinero se haga la transaccion correctamente
    #def test_correct_money(self):
    #    response = self.app.post('/transaction', data = dict(origen="asdasdasdaasdasdasdaasdasdasda1234", destino="asdasdasdaasdasdasdaasdasdasda1234", cantidad="800"), follow_redirects=True)
    #    self.assertEqual(response.status_code, 200)
#
    ## Prueba que si se mete la cantidad incorrecta de dinero no se haga la transaccion correctamente
    #def test_incorrect_money(self):
    #    response = self.app.post('/transaction', data = dict(origen="asdasdasdaasdasdasdaasdasdasda1234", destino="asdasdasdaasdasdasdaasdasdasda1234", cantidad="80000"), follow_redirects=True)
    #    self.assertEqual(response.status_code, 400)
if __name__ == '__main__':
    unittest.main()