def convert_to_L_per_100KM(efficiency_data):
    converted_data = []
    for item in efficiency_data:
        scale = item["масштаб"]
        value = item["значение"]

        if scale == "MPG":
            # Конвертация из миль на галлон в литры на 100 километров
            converted_value = 235.215 / value
        elif scale == "KPL":
            # Конвертация из километров на литр в литры на 100 километров
            converted_value = 100 / value
        elif scale == "MPL":
            # Преобразование миль на литр в литры на 100 километров
            converted_value = 100 / (value * 0.621371)  # 1 миля = 0.621371 км
        else:
            raise ValueError(f"Неизвестный масштаб: {scale}")

        converted_data.append({"масштаб": "L/100KM", "значение": converted_value})

    return converted_data


# Пример данных
data = [
    {"масштаб": "MPG", "значение": 25.0},
    {"масштаб": "KPL", "значение": 10.0},
    {"масштаб": "MPL", "значение": 40.0},
    {"масштаб": "MPG", "значение": 30.0}
]

# Конвертировать данные в масштаб "литры на 100 километров"
converted_data = convert_to_L_per_100KM(data)

# Вывести конвертированные данные
for item in converted_data:
    print(f"Масштаб: {item['масштаб']}, Значение: {item['значение']:.8f}")
