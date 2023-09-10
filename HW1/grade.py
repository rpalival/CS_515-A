def calculate(number_grade):
    try:
        if number_grade >= 90 and number_grade <=100:
            return "A"
        elif number_grade >= 80 and number_grade < 90:
            return "B"
        elif number_grade >= 70 and number_grade < 80:
            return "C"
        elif number_grade >= 60 and number_grade < 70:
            return "D"
        elif number_grade >= 0 and number_grade < 60:
            return "F"
        else:
            raise ValueError("N/A")
    except ValueError as ve:
        print(ve)