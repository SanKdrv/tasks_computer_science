# Необходимо решить уравнение, которое может содержать переменную x, знаки + и -,
# коэффициент перед x в виде числа, а также числа в качестве слагаемых.
# Ответ необходимо выдать в форме "x=...", если есть решение уравнения,
# "нет решений" - если нет решений и "бесконечное множество решений" -
# если решений бесконечно много.
# Уравнение задается в виде строки.
# Пример: "x+5-3+x=6+x-2", вывод: "x=2"
# Пример: "x=x", вывод: "бесконечное множество решений"
# Пример: "2x=x", вывод: "x=0"


# def solve_equation(equation):
#     # Удаляем пробелы из уравнения
#     equation = equation.replace(" ", "")
#
#     # Разделяем уравнение на левую и правую части
#     left, right = equation.split("=")
#
#     # Считаем сумму чисел и коэффициентов перед x на левой и правой частях
#     left_sum = 0
#     right_sum = 0
#
#     for term in left.split("+"):
#         if "x" in term:
#             if term == "x":
#                 left_sum += 1
#             elif term == "-x":
#                 left_sum -= 1
#             else:
#                 left_sum += int(term[:-1])
#         else:
#             left_sum += int(term)
#
#     for term in right.split("+"):
#         if "x" in term:
#             if term == "x":
#                 right_sum += 1
#             elif term == "-x":
#                 right_sum -= 1
#             else:
#                 right_sum += int(term[:-1])
#         else:
#             right_sum += int(term)
#
#     # Считаем коэффициент при x и свободный член
#     coef = left_sum - right_sum
#     free_term = right_sum - left_sum
#
#     # Проверяем, есть ли решение и возвращаем ответ в нужном формате
#     if coef == 0 and free_term == 0:
#         return "бесконечное множество решений"
#     elif coef == 0 and free_term != 0:
#         return "нет решений"
#     else:
#         return "x=" + str(free_term / coef)
# # Примеры
# # использования:
# # python
# # >> > solve_equation("2x + 3 = 7x - 5")
# # 'x=1.6'
# #
# # >> > solve_equation("x + 2 = x - 3")
# # 'нет решений'
# #
# # >> > solve_equation("2x + 4 = 2(x + 2)")
# # 'бесконечное множество решений'
# eq = str(input())
# solve_equation(eq)

def solve_equation(equation):
    equation = equation.replace(" ", "")  # Удаляем пробелы из уравнения
    equation = equation.replace("=", "-")  # Заменяем знак "=" на "-", чтобы привести уравнение к форме "0 = ..."

    terms = equation.split("-")  # Разделяем уравнение на слагаемые

    left_sum = 0
    right_sum = 0

    for term in terms:
        if "x" in term:
            if term == "x":
                left_sum += 1
            elif term == "-x":
                left_sum -= 1
            else:
                coefficient = int(term[:-1])
                left_sum += coefficient
        else:
            right_sum += int(term)

    if left_sum == right_sum:
        return "бесконечное множество решений"
    elif left_sum == 0:
        return "x=0"
    else:
        value = (right_sum - left_sum) / left_sum
        return "x=" + str(value)


# Примеры использования:
equation = "x+5-3+x=6+x-2"
print(solve_equation(equation))  # x=2

equation = "x=x"
print(solve_equation(equation))  # бесконечное множество решений

equation = "2x=x"
print(solve_equation(equation))  # x=0