import random

class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        """
        Initialize the generator with a list of characters (alphabet).
        """
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        """
        Generate a random string of the given size using the provided alphabet.
        """
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1: int, size2: int) -> tuple:
        """
        Generate a pair of strings with specified lengths.
        """
        return self.generate(size1), self.generate(size2)

    def generate_similar_pair(self, size: int, similarity: float) -> tuple:
        """
        Generate a pair of strings with a certain degree of similarity.
        similarity is a float between 0 and 1, where 1 means identical strings.
        """
        str1 = self.generate(size)
        str2 = ''
        for char in str1:
            if random.random() < similarity:
                str2 += char
            else:
                str2 += random.choice(self.alphabet)
        return str1, str2

    def generate_different_pair(self, size1: int, size2: int) -> tuple:
        """
        Generate a pair of entirely different strings.
        """
        return self.generate(size1), self.generate(size2)