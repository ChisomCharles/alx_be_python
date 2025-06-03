weather = input("What is the weather like today? (sunny/rainy/cold): ")
weather = weather.lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Do not forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I do not have recommendations for this weather.")
