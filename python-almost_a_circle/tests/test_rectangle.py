#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
import sys
import os
from io import StringIO


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

    def test_str_representation(self):
        """
        Teste si la méthode __str__() retourne une représentation correcte du rectangle.
        """
        rectangle = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rectangle), expected_output)

    def test_display_without_x_and_y(self):
        """
        Teste si la méthode display() affiche correctement le rectangle sans x et y.
        """
        rectangle = Rectangle(5, 5)
        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_display_without_y(self):
        """
        Teste si la méthode display() affiche correctement le rectangle sans y.
        """
        rectangle = Rectangle(5, 5, 2)
        expected_output = "  #####\n  #####\n  #####\n  #####\n  #####\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_create_with_id_only(self):
        """
        Teste si la méthode create() crée correctement un Rectangle avec un ID spécifié.
        """
        rectangle = Rectangle.create(**{'id': 89, 'width': 5, 'height': 10})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_create_with_id_and_width(self):
        """
        Teste si la méthode create() crée correctement un Rectangle avec un ID et une largeur spécifiés.
        """
        rectangle = Rectangle.create(**{'id': 89, 'width': 5, 'height': 10})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_create_with_id_width_and_height(self):
        """
        Teste si la méthode create() crée correctement un Rectangle avec un ID, une largeur et une hauteur spécifiés.
        """
        rectangle = Rectangle.create(**{'id': 89, 'width': 5, 'height': 10})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_create_with_id_width_height_and_position(self):
        """
        Teste si la méthode create() crée correctement un Rectangle avec un ID, une largeur, une hauteur et une position spécifiés.
        """
        rectangle = Rectangle.create(**{'id': 89, 'width': 5, 'height': 10, 'x': 2, 'y': 3})
        self.assertEqual(rectangle.id, 89)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_create_with_invalid_arguments(self):
        """
        Teste si la méthode create() lève une exception avec des arguments invalides.
        """
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': '89'}) # L'ID doit être un entier
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89, 'width': '5'}) # La largeur doit être un entier
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89, 'width': 5, 'height': '10'}) # La hauteur doit être un entier

    def test_save_to_file_none(self):
        """
        Teste si la méthode save_to_file() enregistre correctement une liste vide.
        """
        Rectangle.save_to_file(None)
        self.assertFalse(os.path.exists("Rectangle.json"))

    def test_save_to_file_empty_list(self):
        """
        Teste si la méthode save_to_file() enregistre correctement une liste vide.
        """
        Rectangle.save_to_file([])
        self.assertFalse(os.path.exists("Rectangle.json"))

    def test_save_to_file_with_rectangles(self):
        """
        Teste si la méthode save_to_file() enregistre correctement une liste de Rectangles.
        """
        r1 = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
            self.assertEqual(content, '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_load_from_file_non_existing_file(self):
        """
        Teste si la méthode load_from_file() retourne une liste vide lorsque le fichier n'existe pas.
        """
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existing_file(self):
        """
        Teste si la méthode load_from_file() retourne une liste de Rectangles lorsque le fichier existe.
        """
        r1 = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([r1])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 1)
        self.assertEqual(rectangles[0].id, r1.id)
        self.assertEqual(rectangles[0].width, r1.width)
        self.assertEqual(rectangles[0].height, r1.height)
        self.assertEqual(rectangles[0].x, r1.x)
        self.assertEqual(rectangles[0].y, r1.y)

    def test_display(self):
        """
        Teste si la méthode display() affiche correctement le rectangle.
        """
        rectangle = Rectangle(5, 5, 2, 3)
        expected_output = "\n\n\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        rectangle.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

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
