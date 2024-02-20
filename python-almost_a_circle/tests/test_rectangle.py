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
        rectangle = Rectangle(5, 10) # Ajoutez les coordonnées x et y
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)  # Défaut
        self.assertEqual(rectangle.y, 0)  # Défaut

    def test_constructor_with_coordinates(self):
        """
        Teste si le constructeur de Rectangle initialise correctement les attributs avec des coordonnées.
        """
        rectangle = Rectangle(5, 10, 2, 3)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_invalid_width(self):
        """
        Teste si une ValueError est levée lorsque la largeur est négative.
        """
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_invalid_height(self):
        """
        Teste si une ValueError est levée lorsque la hauteur est négative.
        """
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        """
        Teste si une ValueError est levée lorsque la largeur est nulle.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """
        Teste si une ValueError est levée lorsque la hauteur est nulle.
        """
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_invalid_x_coordinate(self):
        """
        Teste si une ValueError est levée lorsque la coordonnée x est négative.
        """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_invalid_y_coordinate(self):
        """
        Teste si une ValueError est levée lorsque la coordonnée y est négative.
        """
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_constructor_with_all_arguments(self):
        """
        Teste si le constructeur de Rectangle initialise correctement les attributs avec tous les arguments.
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

    def test_invalid_arguments(self):
        """
        Tests avec des argument invalides
        """
        with self.assertRaises(TypeError):
            Rectangle("1", 2) # La chaîne "1" doit être remplacée par un entier
        with self.assertRaises(TypeError):
            Rectangle(1, "2") # La chaîne "2" doit être remplacée par un entier
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3") # La chaîne "3" doit être remplacée par un entier
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4") # La chaîne "4" doit être remplacée par un entier

if __name__ == '__main__':
    unittest.main()
