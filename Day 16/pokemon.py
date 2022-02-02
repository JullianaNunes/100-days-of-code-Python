from prettytable import PrettyTable

tabela = PrettyTable()

# O primeiro valor é o nome da coluna e os outros são os valores que vão ficar nessa coluna
tabela.add_column("Nome do Pokémon", ['Eevee','Leafeon','Espeon'])
tabela.add_column("Tipo", ['Normal','Grass','Psychic'])

# Alinha o texto da tabela para esquerda
tabela.align = 'l'

print(tabela)

''' Documentação
 - https://pypi.org/project/prettytable/
 - https://pokemondb.net/pokedex/game/x-y
 - https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
'''