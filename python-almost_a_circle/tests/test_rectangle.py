import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Classe de test pour la classe Rectangle.
    """

    def test_constructor(self):
        """
        Teste si le constructeur de Rectangle initialise correctement les attributs.
        """
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_area(self):
        """
        Teste si la méthode area() calcule correctement la surface du rectangle.
        """
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_to_dictionary(self):
        """
        Teste si la méthode to_dictionary() retourne un dictionnaire correctement.
        """
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {
            'id': 1,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
        }
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

    def test_update(self):
        """
        Teste si la méthode update() met à jour les attributs correctement.
        """
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(10, 7, 8, 9, 20)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 20)

    def test_update_kwargs(self):
        """
        Teste si la méthode update() avec des kwargs met à jour les attributs correctement.
        """
        rectangle = Rectangle(5, 10, 2, 3, 1)
        rectangle.update(id=10, width=7, height=8, x=9, y=20)
        self.assertEqual(rectangle.id, 10)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 20)


if __name__ == '__main__':
    unittest.main()
