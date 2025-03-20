import re
from datetime import datetime

def is_valid_email(email): #Sprawdza czy podany adres e-mail jest poprawny
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
    
    if ".." in email.split("@")[-1]:  
        return False
    
    return re.match(pattern,email) is not None

def calculate_square_area(side): #Oblicza pole kwadrat
    if side <= 0:
        raise ValueError("Długość boku kwadratu musi być większa niż 0.")
    return side * side

def filter_even_numbers(numbers): #Zwraca liczby parzyste z listy
    return [num for num in numbers if num % 2 == 0]

def convert_date_format(date_str): #Konwertuje datę z formatu DD-MM-YYYY na YYYY/MM/DD
    try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
        return date_obj.strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano 'DD-MM-YYYY'.")
    
def is_palindrome(text): #Sprawdxa czy tekst jest palindromem
    cleaned_text = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    return cleaned_text == cleaned_text[::-1]