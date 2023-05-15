import unittest
from unittest.mock import patch

from flask import session

import app

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True 

    @patch('app.oauth.google.authorize_access_token')
    def test_google_login_logout(self, mock_authorize_access_token):
        # Mock the Google auth response
        mock_authorize_access_token.return_value = {
            'userinfo': {
                'email': 'test@example.com',
                'name': 'Test User',
            }
        }

        # Test login and logout
        with self.app as c:
            # Test login
            response = c.get('/google/auth', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(session['email'], 'test@example.com')
            self.assertEqual(session['name'], 'Test User')

            # Test logout
            response = c.get('/cerrar-sesion/')
            self.assertEqual(response.status_code, 302)
            self.assertNotIn('email', session)
            self.assertNotIn('name', session)

if __name__ == '__main__':
    unittest.main()
