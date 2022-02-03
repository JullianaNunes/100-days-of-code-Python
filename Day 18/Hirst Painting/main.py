import colorgram

lista_cores = []
colors = colorgram.extract('image.jpg', 20)
for color in colors:
    lista_cores.append(color.rgb)

print(lista_cores)