import random
import string

class Robot:
	USED_NAMES = set()
	ALPHABET = string.ascii_uppercase
	DIGITS = string.digits
	def __init__(self):
		self.name = self._generate_random_name()

	def reset(self):
		self.name = self._generate_random_name()

	@classmethod
    def _generate_random_name(letters: int, numbers: int):
    	letters_alphabet = string.ascii_uppercase
    	digits_alphabet = string.digits
    	result_letters = random.choice(letters_alphabet) for i in range(letters)
    	result_numbers = random.choice(digits_alphabet) for i in range(numbers)
    	return ''.join(result_letters + result_numbers)
