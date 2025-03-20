import unittest
from app import is_valid_email, calculate_square_area, filter_even_numbers, convert_date_format, is_palindrome

class TestAppFunctions(unittest.TestCase):
    
    def setUp(self):
        self.valid_emails = [ #poprawne adresy mailowe
            "test@example.com",
            "name@domain.co.uk" #podwójna domena
        ]
        self.invalid_emails = [ #niepoprawne adresy mailowe
            "invalid-email", #brak @
            "user@com", #brak pełnej domeny
            "user@domain..com" #podwójna kropka
        ]
        
        self.square_cases = [
            (5, 25), #typowy
            (10, 100), #typowy
            (1, 1), #brzegowy, najmniejszy możliwy bok
            (-3, None), #błędny, wartość ujemna
            (0, None) #brzegowy, wartość 0
        ]
        
        self.numbers_cases = [
            ([1, 2, 3, 4, 5], [2, 4]), #typowy, liczby parzyste i nieparzyste
            ([7, 9, 11], []), #brak liczb parzystych
            ([0, -2, -4, 3], [0, -2, -4]), #liczby ujemne i 0
            ([], []), #pusta lista
            ([2, 4, 6, 8], [2, 4, 6, 8]) #same parzyste liczby
        ]
    
        self.date_cases = [ #poprawne daty
            ("02-07-2003", "2003/07/02"), #typowy
            ("11-02-2005", "2005/02/11"), #typowy
            ("29-02-2024", "2024/02/29"), #rok przestępny
        ]
        self.invalid_dates = ["32-01-2020", "invalid-date"] #niepoprawne daty
        
        self.palindrome_cases = [
            ("Kajak", True), #typowy
            ("Kamil Ślimak", True), #palindrom z polskimi znakami i spacjami
            ("Hello world", False), #nie palindrom
            ("", True), #pusty string
            ("A man, a plan, a canal, Panama!", True) #zdanie palindromiczne
        ]
        
    def test_is_valid_email(self): #Test poprawności email
        for email in self.valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))
        for email in self.invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))
        
    def test_calculate_square_area(self): #Test obliczania pola kwadratu
        for side, expected in self.square_cases:
            with self.subTest(side=side):
                if expected is None:
                    with self.assertRaises(ValueError):
                        calculate_square_area(side)
                else:
                    self.assertEqual(calculate_square_area(side), expected)
            
    def test_filter_even_numbers(self): #Test filtrowania liczb parzystych
        for numbers, expected in self.numbers_cases:
            with self.subTest(numbers=numbers):
                self.assertEqual(filter_even_numbers(numbers), expected)
        
    def test_convert_date_format(self): #Test konwersji formatu daty
        for date_str, expected in self.date_cases:
            with self.subTest(date_str=date_str):
                self.assertEqual(convert_date_format(date_str), expected)
        for date_str in self.invalid_dates:
            with self.subTest(date_str=date_str):
                with self.assertRaises(ValueError):
                    convert_date_format(date_str)
                    
    def test_is_palindrome(self): #Test sprawdzający czy tekst jest palindromem
        for text, expected in self.palindrome_cases:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected)

if __name__ == "__main__":
    unittest.main()
                         