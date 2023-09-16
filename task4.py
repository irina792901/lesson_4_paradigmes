# Предположим, у нас есть список измерений температуры в разных масштабах (Фаренгейт, Кельвин, и Цельсий), и нам нужно сконвертировать
# и стандартизировать все измерения в градусы Цельсия.

# Исходные данные
temperature_data = [("Фаренгейт", 98.6), ("Кельвин", 310.15), ("Цельсий", 37.0)]
def standartizid(temperature, scale):
    if scale == "Фаренгейт":
        return (temperature - 32) * 5/9
    elif scale == "Кельвин":
        return temperature - 273.15
    elif scale == "Цельсий":
        return temperature
    else:
        raise ValueError(f"Неизвестная шкала: {scale}")

# Конвертировать все данные в градусы Цельсия
result = [(standartizid(temp, scale), "Цельсий") for scale, temp in temperature_data]

# Вывести конвертированные данные
for temp, scale in result:
    print(f"{temp:.2f} градусов {scale}")
