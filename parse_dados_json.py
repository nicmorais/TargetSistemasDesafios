import json

file = open('dados.json')
values = json.load(file)
max_value, min_value, sum_values, count = 0, 0, 0, 0

for i in values:
    amount = i['valor']

    if amount == 0:
        continue

    if count == 0:
      min_value = amount

    count += 1

    if amount > max_value:
        max_value = amount
    elif amount < min_value:
        min_value = amount
    sum_values += amount

mean = sum_values / count

days_count = 0
for i in values:
    amount = i['valor']
    if amount > mean:
        days_count += 1

print("Maior valor: R$", max_value)
print("Menor valor: R$", min_value)
print("Dias com valor maior que média: ", days_count)