class User:

    '''
        Em Python, a forma como criaríamos o construtor é através da utilização de uma função especial, que é a função init.
        E pode dizer-se que é especial porque não é apenas a palavra-chave def e depois o nome da função. Tem dois pontos em destaque
        ambos os lados do nome. normalmente utilizado para inicializar os atributos.
        Dentro desta função init é onde inicializamos ou criamos o início valores para os nossos atributos.
        O importante a lembrar é que a função init vai ser chamada sempre que se cria um novo objecto a partir desta classe.
    '''

    def __init__(self, user_id, username):
        '''
         self é o objeto real que está a ser criado ou a ser inicializado.
         além disso, pode acrescentar tantos parâmetros quantos desejar.
        '''
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# O inicializador precisa de dois parâmetros (id e username)
user_1 = User('001','Julliana')
user_2 = User('002','Willian')

print(user_1.username)
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

''' Observações

Pascal Case (classes) - O nome da classe deve ter a primeira letra de cada palavra capitalizados.
E este estilo particular de nomenclatura na Programação é conhecido como caso Pascal.
Portanto, se pensarmos em Blaise Pascal como uma pessoa, então sabemos que o nome de todos,
o nome de cada pessoa, tem a primeira letra maiúscula e também a primeira letra
do seu apelido ou do seu nome do meio e basicamente cada nome subsequente em maiúsculas.
Chama-se o PascalCase de “UpperCamelCase”. Usar Pascal Case para todos os nomes de membros,
tipos e namespace públicos que consistem em várias palavras.

camelCase - O camelCase, desse modo, é muito semelhante com o PascalCase, no qual a letra inicial
de cada palavra de um termo composto usado no código é maiúscula. O camelCase é denominado de “lowerCamelCase”.
Usar Camel Case para nomes de parâmetros.

snake_case (funções ou variáveis) -  Caso cobra se refere ao estilo de escrita em que cada espaço é substituído por um caractere de
sublinhado e a primeira letra de cada palavra escrita em minúsculas.

Documentação 
 - https://www.python.org/dev/peps/pep-0008/
 - https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles
 
'''

