# ===========================
# AgriAI Main Controller
# ===========================

from weather import get_weather
from vision import detect_crop
from irrigation import irrigation_advice
from fertilizer import fertilizer_advice
from yield_prediction import predict_yield


def main():

    print("\n🌾 Welcome to AgriAI 🌾\n")

    city = input("Enter your city: ")

    image = input("Enter crop image path: ")

    area = float(input("Enter farm area (acre): "))

    seed = input("Enter seed variety: ")

    stage = input("Enter crop stage (Seedling/Vegetative/Flowering/etc): ")


    print("\nFetching weather data...")
    weather = get_weather(city)


    print("Analyzing crop image...")
    crop_info = detect_crop(image)


    crop_name = crop_info["crop"]


    irrigation = irrigation_advice(
        weather,
        crop_name
    )


    fertilizer = fertilizer_advice(
        crop_name,
        stage,
        weather
    )


    predicted_yield = predict_yield(
        area,
        seed,
        crop_name
    )


    print("\n==============================")
    print("      AGRIAI REPORT")
    print("==============================")

    print(f"\nCrop : {crop_name}")

    print(f"Disease : {crop_info['disease']}")

    print(f"\nTemperature : {weather['temperature']} °C")

    print(f"Humidity : {weather['humidity']} %")

    print(f"Rainfall : {weather['rainfall']} mm")

    print(f"\nIrrigation Advice : {irrigation}")

    print(f"Fertilizer Advice : {fertilizer}")

    print(f"Estimated Yield : {predicted_yield} Quintals")

    print("\n==============================")



if __name__ == "__main__":
    main()
