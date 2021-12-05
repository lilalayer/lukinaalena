zvet = ["зелёной", "красной", "жёлтой", "белой", "чёрной"]
zvet1 = ["зелёного", "красного", "жёлтого", "белого", "чёрного"]
an = ["крысы", "коровы", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
an1 = ["тигра", "зайца", "дракона"]
print("Введите год")
x = int(input())
if x<0:
    print("Введено некорректное значение года")
if (x - 1984) < 0:
    while (x - 1984) < -60:
        x += 60
if (x - 1984) % 60 <= 11:
    if (x - 1984) % 12 == 0:
        print(f"Год {zvet[0]} {an[0]}")
    elif (x - 1984) % 12 == 1:
        print(f"Год {zvet[0]} {an[1]}")
    elif (x - 1984) % 12 == 2:
        print(f"Год {zvet1[0]} {an1[0]}")
    elif (x - 1984) % 12 == 3:
        print(f"Год {zvet1[0]} {an1[1]}")
    elif (x - 1984) % 12 == 4:
        print(f"Год {zvet1[0]} {an1[2]}")
    elif (x - 1984) % 12 == 5:
        print(f"Год {zvet[0]} {an[2]}")
    elif (x - 1984) % 12 == 6:
        print(f"Год {zvet[0]} {an[3]}")
    elif (x - 1984) % 12 == 7:
        print(f"Год {zvet[0]} {an[4]}")
    elif (x - 1984) % 12 == 8:
        print(f"Год {zvet[0]} {an[5]}")
    elif (x - 1984) % 12 == 9:
        print(f"Год {zvet[0]} {an[6]}")
    elif (x - 1984) % 12 == 10:
        print(f"Год {zvet[0]} {an[7]}")
    elif (x - 1984) % 12 == 11:
        print(f"Год {zvet[0]} {an[8]}")
elif 23 >= (x - 1984) % 60 > 11:
    if (x - 1984) % 12 == 0:
        print(f"Год {zvet[1]} {an[0]}")
    elif (x - 1984) % 12 == 1:
        print(f"Год {zvet[1]} {an[1]}")
    elif (x - 1984) % 12 == 2:
        print(f"Год {zvet1[1]} {an1[0]}")
    elif (x - 1984) % 12 == 3:
        print(f"Год {zvet1[1]} {an1[1]}")
    elif (x - 1984) % 12 == 4:
        print(f"Год {zvet1[1]} {an1[2]}")
    elif (x - 1984) % 12 == 5:
        print(f"Год {zvet[1]} {an[2]}")
    elif (x - 1984) % 12 == 6:
        print(f"Год {zvet[1]} {an[3]}")
    elif (x - 1984) % 12 == 7:
        print(f"Год {zvet[1]} {an[4]}")
    elif (x - 1984) % 12 == 8:
        print(f"Год {zvet[1]} {an[5]}")
    elif (x - 1984) % 12 == 9:
        print(f"Год {zvet[1]} {an[6]}")
    elif (x - 1984) % 12 == 10:
        print(f"Год {zvet[1]} {an[7]}")
    elif (x - 1984) % 12 == 11:
        print(f"Год {zvet[1]} {an[8]}")
elif 35 >= (x - 1984) % 60 > 23:
    if (x - 1984) % 12 == 0:
        print(f"Год {zvet[2]} {an[0]}")
    elif (x - 1984) % 12 == 1:
        print(f"Год {zvet[2]} {an[1]}")
    elif (x - 1984) % 12 == 2:
        print(f"Год {zvet1[2]} {an1[0]}")
    elif (x - 1984) % 12 == 3:
        print(f"Год {zvet1[2]} {an1[1]}")
    elif (x - 1984) % 12 == 4:
        print(f"Год {zvet1[2]} {an1[2]}")
    elif (x - 1984) % 12 == 5:
        print(f"Год {zvet[2]} {an[2]}")
    elif (x - 1984) % 12 == 6:
        print(f"Год {zvet[2]} {an[3]}")
    elif (x - 1984) % 12 == 7:
        print(f"Год {zvet[2]} {an[4]}")
    elif (x - 1984) % 12 == 8:
        print(f"Год {zvet[2]} {an[5]}")
    elif (x - 1984) % 12 == 9:
        print(f"Год {zvet[2]} {an[6]}")
    elif (x - 1984) % 12 == 10:
        print(f"Год {zvet[2]} {an[7]}")
    elif (x - 1984) % 12 == 11:
        print(f"Год {zvet[2]} {an[8]}")
elif 47 >= (x - 1984) % 60 > 35:
    if (x - 1984) % 12 == 0:
        print(f"Год {zvet[3]} {an[0]}")
    elif (x - 1984) % 12 == 1:
        print(f"Год {zvet[3]} {an[1]}")
    elif (x - 1984) % 12 == 2:
        print(f"Год {zvet1[3]} {an1[0]}")
    elif (x - 1984) % 12 == 3:
        print(f"Год {zvet1[3]} {an1[1]}")
    elif (x - 1984) % 12 == 4:
        print(f"Год {zvet1[3]} {an1[2]}")
    elif (x - 1984) % 12 == 5:
        print(f"Год {zvet[3]} {an[2]}")
    elif (x - 1984) % 12 == 6:
        print(f"Год {zvet[3]} {an[3]}")
    elif (x - 1984) % 12 == 7:
        print(f"Год {zvet[3]} {an[4]}")
    elif (x - 1984) % 12 == 8:
        print(f"Год {zvet[3]} {an[5]}")
    elif (x - 1984) % 12 == 9:
        print(f"Год {zvet[3]} {an[6]}")
    elif (x - 1984) % 12 == 10:
        print(f"Год {zvet[3]} {an[7]}")
    elif (x - 1984) % 12 == 11:
        print(f"Год {zvet[3]} {an[8]}")
elif 59 >= (x - 1984) % 60 > 47:
    if (x - 1984) % 12 == 0:
        print(f"Год {zvet[4]} {an[0]}")
    elif (x - 1984) % 12 == 1:
        print(f"Год {zvet[4]} {an[1]}")
    elif (x - 1984) % 12 == 2:
        print(f"Год {zvet1[4]} {an1[0]}")
    elif (x - 1984) % 12 == 3:
        print(f"Год {zvet1[4]} {an1[1]}")
    elif (x - 1984) % 12 == 4:
        print(f"Год {zvet1[4]} {an1[2]}")
    elif (x - 1984) % 12 == 5:
        print(f"Год {zvet[4]} {an[2]}")
    elif (x - 1984) % 12 == 6:
        print(f"Год {zvet[4]} {an[3]}")
    elif (x - 1984) % 12 == 7:
        print(f"Год {zvet[4]} {an[4]}")
    elif (x - 1984) % 12 == 8:
        print(f"Год {zvet[4]} {an[5]}")
    elif (x - 1984) % 12 == 9:
        print(f"Год {zvet[4]} {an[6]}")
    elif (x - 1984) % 12 == 10:
        print(f"Год {zvet[4]} {an[7]}")
    elif (x - 1984) % 12 == 11:
        print(f"Год {zvet[4]} {an[8]}")
