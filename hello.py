import time
formatted_time = int(time.strftime("%H"))
if (formatted_time < 13):
    print("Hello Good Morning")
elif (13<formatted_time < 17):
    print("Hello Good Afternoon")
else:
    print("Hello Good Evening")