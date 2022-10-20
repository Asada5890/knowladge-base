
# age = None

# if age:  # будет выполнено if bool(age):
#     print(f"Возраст: {age}")
# else:
#     print("Данные о возрасте отсутствуют")

#####

# name = input("Как тебя зовут: ")

# if name:
#     print(f"Привет {name}!")
# else:
#     print("Напиши хоть что-нибудь")

#####

# cart = list()
# # cart = ["хлеб", "масло", "молоко"]

# # if not cart - если корзина пустая
# if cart:
#     print("Оформляем заказ...")
# else:
#     print("Корзина пуста!")

#####

dest = input("Введите пункт назначения: ").strip()

while not dest:
    print("Необходимо ввести пункт назначения!")
    dest = input("Попробуйте еще раз: ")



