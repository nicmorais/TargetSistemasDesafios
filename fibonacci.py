first_number = 0
second_number = 1
total = 0
max_value = int(input("Digite o valor: "))

while total < max_value:
    # Total = numero atual + seu sucessor
    total = first_number + second_number
    # Primero numero torna-se o segundo numero
    first_number = second_number
    # Segundo numero torna-se o total
    second_number = total
    # Repete-se o processo, parar caso chegue no numero escolhido

if total == max_value:
    # Se parou no numero escolhido
    print("Valor inserido pertence a sequencia")
else:
    print("Valor inserido nao pertence a sequencia.")