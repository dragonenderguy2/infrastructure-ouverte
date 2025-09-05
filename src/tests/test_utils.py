import unittest
from utils import check_open_standard, format_documentation

class TestUtils(unittest.TestCase):
    def test_check_open_standard(self):
        self.assertEqual(check_open_standard('HTTP'), 'HTTP est une norme ouverte.')

    def test_format_documentation(self):
        formatted = format_documentation('Titre', 'Ceci est un contenu de documentation.')
        self.assertIn('Titre', formatted)
        self.assertIn('Ceci est un contenu de documentation.', formatted)

if __name__ == '__main__':
    unittest.main()
