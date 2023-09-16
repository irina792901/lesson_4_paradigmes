# Исходные даты в разных форматах
import dateutil.parser

dates = ["2022-05-15", "15/05/22", "2022/05/15", "05-15-2022"]


# Функция для стандартизации дат
def standardize_date(date_str):
    # Попробуем разные форматы дат и вернем в нужном формате
    try:
        date_obj = dateutil.parser.parse(date_str)
        return date_obj.strftime("%Y-%m-%d")
    except:
        return "Недопустимый формат"


# Применение стандартизации к каждой дате
standardized_dates = [standardize_date(date) for date in dates]

# Теперь у нас есть список дат в стандартизированном формате
print(standardized_dates)
