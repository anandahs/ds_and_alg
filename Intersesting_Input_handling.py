def celcius_to_fahrenheit(c):
    f = c * (9 / 5) + 32
    return f


if __name__ == "__main__":

    while True:
        try:
            c = int(input("enter temperature in celcius:"))
            print(f"temperature in fahrenheit:{celcius_to_fahrenheit(c)}")
            break
        except ValueError:
            print(f"Temperature should be in whole number!")
