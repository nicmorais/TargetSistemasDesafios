string_input = input("Digite a string a ser invertida:")
rev_string = ""
rev_iterator = len(string_input)

while rev_iterator > 0:
    rev_string += string_input[rev_iterator - 1]
    rev_iterator -= 1

print("Resultado:", rev_string)