# my solution
def avg_temperature():
    days = int(input("How many day's temperature? "))

    all_temperatures = []
    for day in range(1, days + 1):
        day_temp = int(input(f"Day {day}'s high temp"))
        all_temperatures.append(day_temp)

    avg_temp = sum(all_temperatures) / len(all_temperatures)

    print(f"Average = {avg_temp}")
    day_temperature_2 = [day_temp for day_temp in all_temperatures if day_temp > avg_temp]
    print(f"{len(day_temperature_2)} day(s) above average")


def avg_temperature_instructor():
    days = int(input("How many day's temperature? "))

    all_temperatures = []
    total_temp = 0

    for day in range(1, days + 1):
        day_temp = int(input(f"Day {day}'s high temp "))
        all_temperatures.append(day_temp)
        total_temp += day_temp

    avg_temp = total_temp / days

    print(f"Average = {avg_temp}")
    day_temperature_2 = [day_temp for day_temp in all_temperatures if day_temp > avg_temp]
    print(f"{len(day_temperature_2)} day(s) above average")


if __name__ == "__main__":
    #avg_temperature()
    avg_temperature_instructor()
