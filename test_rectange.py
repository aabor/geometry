from unittest import TestCase


class TestRectange(TestCase):
    def test_area_succeeds(self):
        from geometry import Rectangle
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_fails(self):
        from geometry import Rectangle
        r = Rectangle(2, 3)
        self.assertNotEqual(r.area(), 8)
