import Character
char = Character.Character()


while True:
    char.location.getter()
    # print("H хилл | S поиск | I инвентарь")
    char.Setter(input("Ваше действие: "))

    if char.HP == 0:
        print("Работяга не смог выжить в этом жестоком мире")
        break