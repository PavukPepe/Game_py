import random
import Location

n1 = Location.n1
class Character():
    HP = 3
    VN = 3
    inv = {"Баклашка пива": 1, "Чирик": 2}
    location = n1

    def Draka(self, dif):
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 5*dif)
        if n1 > n2:
            self.VN = self.VN - 1
            print(self.location.react_draka[1])
            print(f"Оставеееся ХП: {self.HP}")
        else:
            self.VN = self.VN - 1
            self.HP = self.HP - 1
            print(self.location.react_draka[0])
            print(f"Оставеееся ХП: {self.HP}")

    def Change(self):
        if self.inv["Чирик"] > 1:
            self.inv["Чирик"] = self.inv["Чирик"] - 2
            self.inv["Баклашка пива"] = self.inv["Баклашка пива"] + 1
            print("Вес ваших карманов уменьшился, зато теперь у вас есть пиво ")
            print(f"Оставшееся пиво {self.inv['Баклашка пива']}. Оставшиеся чирики {self.inv['Чирик']}")
        else:
            print("Денег нада? Играй в авокадо!")
            print(f"Оставшиеся чирики {self.inv['Чирик']}")

    def Hilling(self):
        if self.inv["Баклашка пива"] > 0:
            self.inv["Баклашка пива"] = self.inv["Баклашка пива"] - 1
            self.HP = self.HP + 1
            self.VN = self.VN + 1
            print("Вы выпили пиво и чувствуете как энергия и жизненные силы возвращаются к вам")
            print(f"Оставшееся пиво {self.inv['Баклашка пива']}")
            print(f"Оставеееся ХП: {self.HP}")
        else:
            print("У вас нет пива(((")

    def Searching(self, dif):
        n1 = random.randint(0, 5*dif)
        if n1 > 15:
            k = random.randint(2, 10)
            self.inv["Чирик"] += k
            print(f"Вы нашли заначку {k} чирик(-ов)")
            print(f"Количество чириков в карманах: {self.inv['Чирик']}")
        elif n1 < 15 and n1 > 5:
            self.inv["Баклашка пива"] += 1
            print("Вам посчастливилось найти припрятанную кормушку, этикетка гласит импортое, но вы то знаете правду")
            print(f"Оставшееся пиво {self.inv['Баклашка пива']}")
        elif n1 < 5:
            print("На вас напали!")
            self.Draka(self.location.dif_draka)

    def Inventar(self):
        for i in self.inv:
            print(f"{i}: {self.inv[i]}")

    def Setter(self, cl):
        if cl == "h":
            self.Hilling()
        elif cl == "i":
            self.Inventar()
        elif cl == "s":
            self.Searching(self.location.dif_search)
        else:
            try:
                self.location.cl_loc += 1
                self.location = self.location.list_loc[int(cl)-1]
            except:
                print("Вы ввeли некорректное заначение")