# This is a sample Python script.

# Исходные оценки студентов в виде строк
grades_str = ["5.0", "4.5", "4.0", "yt", "3.5", "4.0"]

# Создаем пустой список для хранения числовых оценок
grades_float = []

# Проходим по каждой строке в списке оценок
for grade_str in grades_str:
    try:
        # Пробуем преобразовать строку в число с плавающей точкой
        grade_float = float(grade_str)
        # Если успешно, добавляем в список
        grades_float.append(grade_float)
    except ValueError:
        # Если возникла ошибка (например, строка не является числом), пропускаем эту строку
        print(f"Пропущена оценка: {grade_str}")

# Теперь у нас есть список числовых оценок
print("Числовые оценки:", grades_float)

# Вычисляем среднюю оценку
average_grade = sum(grades_float) / len(grades_float)
print(f"Средняя оценка: {average_grade}")