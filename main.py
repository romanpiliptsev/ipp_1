import requests

b, a = input("Введите первые координаты: "), input("Введите вторые коордианты: ")

while True:
    try:
        image = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={a},{b}&spn=0.006,0.006&l=map")
        with open("image.png", "wb") as f:
            f.write(image.content)
        print("Изображение сохранено в файле image.png")
        print()
    except Exception:
        print("Вы ввели неверные координаты! Введите координаты заново!")
    finally:
        b, a = input("Введите первые координаты: "), input("Введите вторые коордианты: ")

# 55.752004, 37.617734
