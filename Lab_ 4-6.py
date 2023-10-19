bear = input('Enter an animal: ').lower()
pizza = input('Enter an dish: ').lower()

bear = bear.replace('-', '').replace(' ', '')
pizza = pizza.replace('-', '').replace(' ', '')

if bear[0] == pizza[0] and bear[0] == pizza[-1]:
    print('true')
else:
    print('false')
    