





def formatter_to(number_to):
    if len(number_to) == 25:
        number_to = number_to.split()
        #number_to = ' '.join(number_to)
        name_card = ' '.join(number_to[:1])
        return f'{name_card} **{number_to[-1][:-16]}'

    number_to = number_to.split()
    result = len(number_to) - 1
    #number_to = ' '.join(number_to)
    name_card = ' '.join(number_to[:result])
    return f'{name_card} {number_to[-1][0:4]} {number_to[-1][5:7]}** **** {number_to[-1][:-12]}'

number_to = "Maestro 3000704277834087"

print(formatter_to(number_to))