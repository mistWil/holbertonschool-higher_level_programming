import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Classe de test pour la classe Base.
    """

    def test_id_assigned_correctly(self):
        """
        Teste si l'ID est attribué correctement lors de la création d'instances de Base.
        """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(100)
        
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 100)
        
    def test_to_json_string(self):
        """
        Teste la méthode to_json_string de la classe Base.
        """
        obj = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'a': 1, 'b': 2}]), '[{"a": 1, "b": 2}]')  # Test avec un dictionnaire
        
if __name__ == '__main__':
    unittest.main()
