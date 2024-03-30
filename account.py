import os

def clean_term():
    os_system = os.name
    if os_system == 'posix': # distro Linux ou Mac
        os.system('clear')
    elif os_system == 'nt': # Windows
        os.system('cls')

users = []
max_users = 5

def login():
    # Verifica se o número de usuários é igual a 5, caso passe ele dirá que foi atingido o limite
    if len(users) >= max_users:
        print('Limite de usuários atingido.')
        return
    user = {}
    user['name'] = input('Qual seu nome?\n')
    user['music'] = input('Qual sua música favorita?\n')
    users.append(user) # Adiciona o usuário
    print('O usuário foi registrado.')

def view_users():
    print('\nLista de usuários:')
    for idx, user in enumerate(users, start=1):
        print(f'\nUsuário {idx}:')
        print(f"Nome: {user['name']}")
        print(f"Música Favorita: {user['music']}")

# Limpa o terminal antes de começar o programa
clean_term()

while True:
    print('''
1. Cadastro
2. Ver lista
3. Sair
''')
    
    menu = input('Use os números de 1 a 3 para escolher:\n')

    if menu == '1':
        login()
    elif menu == '2':
        view_users()
    elif menu == '3':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
