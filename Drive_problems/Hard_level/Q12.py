rainfall, wind_speed, visibility = map(int, input().split())

if rainfall >= 200 or wind_speed >= 120 or visibility < 100:
    print("Red Alert")

elif (rainfall >= 100 and wind_speed >= 80) or visibility < 300:
    print("Orange Alert")

elif rainfall >= 50 or wind_speed >= 50 or visibility < 700:
    print("Yellow Alert")

else:
    print("No Alert")