per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада:"))
banks = list((per_cent.keys()))
deposit = list((per_cent.values()))

for i in range(len(deposit)):
    deposit[i]=round(deposit[i]*money/100,2)
    print("Накопленные за год средства в банке", banks[i], "составят %.2f рублей" %(deposit[i]))
print("Максимальная сумма, которую вы можете заработать — %.2f рублей" %(max(deposit)))

