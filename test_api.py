import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from grandprix import create_app
from model import Booking, Developer, Resource

class GrandPrixTestCase(unittest.TestCase):

    def setUp(self):        
        self.app = create_app()
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_healthy(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['healthy'], True)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()