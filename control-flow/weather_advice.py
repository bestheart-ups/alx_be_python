#use of if, elif and else statements

weather = input("whats the weather like today? (sunny/ rainy/ cold): ")
#provide clothing recommendation

if weather == "sunny":
    print("wear a t-shirt and sun glasses")
elif weather == "rainy":
    print("dont forget your umbrella and a raincoat")
elif weather == "cold":
    print("make sure to wear a warm cold and a scarf")
else:
    print("sorry, i dont have recommendation for this weather")