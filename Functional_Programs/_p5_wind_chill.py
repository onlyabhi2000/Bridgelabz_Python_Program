import math

def wind_chill(t, v):
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (math.pow(v, 0.16))
    return w 


t = int(input("Enter the value of temperature: "))
v = int(input("Enter the value of velocity: "))


if abs(t) > 50 or v < 3 or v > 120:
    print("Invalid input: t must be <= 50 and 3 <= v <= 120.")
else:
    calculated_wind_chill = wind_chill(t, v)
    print(f"Effective wind chill temperature is: {calculated_wind_chill:.2f}°F")
