tickets, sum = int(input("Введите кол-во билетов: ")), 0
for i in range(1,tickets + 1):
    age = int(input(f"Введите возраст {i}-го посетителя: "))
    if 25 <= age:
        sum += 1390
    elif 18 <= age < 25:
        sum += 990
if tickets > 3:
    sum *= 0.9
print('Общая стоимость билетов равна {:.2f} рублей'.format(sum))

