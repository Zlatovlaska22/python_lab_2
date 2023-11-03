while True:
    print("1 - задача 1\n2 - задача 2\n3 - задача 3\n4 - задача 4\n5 - выход")
    try:
       choice = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка, введите число.")
    if choice == 1:
        def CheckAnagramm(first, second):
            wordPoint = True
            listFirst = list(first)
            countFirst = len(listFirst)
            listSecond = list(second)
            countSecond = len(listSecond)
            if (countFirst == countSecond):
                sortedFirst = sorted(listFirst)
                sortedSecond = sorted(listSecond)
                for i in range(len(sortedFirst)):
                    if sortedFirst[i] == sortedSecond[i]:
                        wordPoint = True
                    else:
                        wordPoint = False
                        break
                if wordPoint:
                    print("Слова являются анаграммами")
                else:
                    print("Слова не являются анаграммами")
            else:
                print("Слова не являются анаграммами")
        wordFirst = input("Введите первое слово: ")
        wordSecond = input("Введите второе слово: ")
        CheckAnagramm(wordFirst, wordSecond)
    elif choice == 2:
        def TakeArgument(num):
            if num == 1:
                while True:
                    try:
                        n = int(input("Введите количество элементов списка: "))
                        break
                    except ValueError:
                        print("Ошибка, повторите попытку.")
                userList = []
                for el in range(1, n + 1):
                    while True:
                        try:
                            el = int(input("Введите элемент списка: "))
                            break
                        except ValueError:
                            print("Ошибка, повторите попытку.")
                    userList.append(el)
                print("Список: ", userList)
                lastPositive = -1
                for i in range(len(userList)):
                    if userList[i] > 0:
                        lastPositive = i
                sumAfterLast = 0
                if lastPositive != -1:
                    for i in range(lastPositive + 1, len(userList)):
                        sumAfterLast += userList[i]
                print("Сумма элементов после положительного равна ", sumAfterLast)
                while 0 in userList:
                    userList.remove(0)
                print("Измененный список: ", userList)
            elif num == 2:
                while True:
                    try:
                        value = int(input("Введите число: "))
                        break
                    except ValueError:
                        print("Ошибка, повторите попытку.")
                reverseValue = 0
                if value > 0:
                    while value > 0:
                        lastNumber = value % 10
                        reverseValue = reverseValue * 10 + lastNumber
                        value = value // 10
                    print("Число в обратном порядке: ", reverseValue)
                elif value < 0:
                    valuePositive = value * (-1)
                    while valuePositive > 0:
                        lastNumber = valuePositive % 10
                        reverseValue = reverseValue * 10 + lastNumber
                        valuePositive = valuePositive // 10
                    print("Число в обратном порядке: ", reverseValue * (-1))
            elif num == 3:
                count = 0
                text = input("Введите строку: ")
                words = text.split()
                countWords = len(words)
                print("Количество слов: ", countWords)
            elif num == 4:
                dict = {}
                while True:
                    try:
                        dictSize = int(input("Введите количество жлементов словаря: "))
                        break
                    except ValueError:
                        print("Ошибка, повторите попытку.")
                for i in range(dictSize):
                    key = input("Введите ключ: ")
                    value = input("Введите значение: ")
                    dict[key] = value
                print("Словарь: ", dict)
                minKey = min(dict, key=dict.get)
                minValue = dict[minKey]
                print("Элемент с минимальным значением: ключ ", minKey, ", значение ", minValue)


        while True:
            print("1 - передача списка\n2 - передача числа\n3 - передача строки\n4 - передача словаря\n5 - выход")
            while True:
                try:
                    num = int(input("Ваш выбор: "))
                    break
                except ValueError:
                    print("Ошибка, повторите попытку.")
            if num == 5:
                break
            elif num == 1 or num == 2 or num == 3 or num == 4:
                TakeArgument(num)
            else:
                num = int(input("Неверное значение, повторите попытку: "))
                TakeArgument(num)
    elif choice == 3:
        def MinusMatrix(row, col):
            hasMinus = False
            matrix = []
            for i in range(row):
                elements = []
                for j in range(col):
                    value = int(input(f"Введите значение для [{i}][{j}]: "))
                    elements.append(value)
                matrix.append(elements)
            print("Первоначальная матрица:")
            for elements in matrix:
                print(elements)
            for i in range(row):
                for j in range(col):
                    if matrix[i][j] < 0:
                        hasMinus = True
                        break
            if hasMinus:
                for i in range(row):
                    for j in range(col):
                        matrix[i][j] = -matrix[i][j]
            print("Измененная матрица:")
            for elements in matrix:
                print(elements)


        MyRow = int(input("Введите количество строк: "))
        MyCol = int(input("Введите количество столбцов: "))
        MinusMatrix(MyRow, MyCol)
    elif choice == 4:
        try:
            number = int(input("Введите число: "))
            result = 10 / number
            print("Результат:", result)
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль")
        except ValueError:
            print("Ошибка: Введите корректное число")
        finally:
            print("Завершение программы")
    elif choice == 5:
        break


