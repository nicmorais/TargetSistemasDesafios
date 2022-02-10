total_states = {'SP': 67836.43,
                'RJ': 36678.66,
                'MG': 29229.88,
                'ES': 27165.48,
                'Outros': 19849.53}

sum_states = 0
for state, amount in total_states.items():
    sum_states += amount

for state, amount in total_states.items():
    percentage = (amount / sum_states) * 100
    print(state, "- Participação:", "{:.2f}".format(percentage), "%")

