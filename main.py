with open("moon.txt", "r") as fd:
    pathArr = fd.read()
    expected = calculate(pathArr)

#Функция, которая считает количество кратеров.
def calculate(pathArr: list) -> int:
    expected = 0
    for x in pathArr:
        for y in x:
            if y == 1:
                expected += 1
                return main()
    return expected
#Функция, которая обрабатывает лист на кратеры.
def main(pathArr: list) -> int:
    weight = 1
    n = 0
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1
                    # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1
                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1
                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1
                        n += 1
                    return weight / n
    return
print(calculate(pathArr))

