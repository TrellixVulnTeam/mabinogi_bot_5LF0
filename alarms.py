from datetime import date


def checkday():
    if date.today().weekday() == 2:
        print("Yay")
        return True
