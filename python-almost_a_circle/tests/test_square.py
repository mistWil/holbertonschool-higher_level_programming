import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Classe de test pour la classe Square.
    """

    def test_constructor(self):
        """
        Teste si le constructeur de Square initialise correctement les attributs.
        """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_area(self):
        """
        Teste si la méthode area() calcule correctement la surface du carré.
        """
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_to_dictionary(self):
        """
        Teste si la méthode to_dictionary() retourne un dictionnaire correctement.
        """
        square = Square(5, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'size': 5,
            'x': 2,
            'y': 3
        }
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_update(self):
        """
        Teste si la méthode update() met à jour les attributs correctement.
        """
        square = Square(5, 2, 3, 1)
        square.update(10, 7, 8, 9)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_update_kwargs(self):
        """
        Teste si la méthode update() avec des kwargs met à jour les attributs correctement.
        """
        square = Square(5, 2, 3, 1)
        square.update(id=10, size=7, x=8, y=9)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)


if __name__ == '__main__':
    unittest.main()
