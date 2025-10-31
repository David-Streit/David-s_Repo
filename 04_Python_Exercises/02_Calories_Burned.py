calories_per_minute = 4.2

for minutes in range(10, 31, 5):  # start=10, stop=31 (not included), step=5
    calories_burned = minutes * calories_per_minute
    print(
        f"After {minutes} minutes, you have burned {calories_burned:.1f} calories.")
