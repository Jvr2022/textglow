import unittest
from textglow.glow import apply_glow, gradient_glow, ascii_glow_border

class TestTextGlow(unittest.TestCase):
    def test_apply_glow(self):
        result = apply_glow("Hello", "red")
        self.assertIn("\033[91m", result)

    def test_gradient_glow(self):
        result = gradient_glow("Hello")
        self.assertIn("\033[91mH\033[93me\033[92ml", result)

    def test_ascii_glow_border(self):
        result = ascii_glow_border("Hello")
        self.assertIn("*****", result)
        
if __name__ == "__main__":
    unittest.main()
