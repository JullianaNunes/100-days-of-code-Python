import colorgram

# Extract 20 colors from an image.
cores = colorgram.extract('image.jpg', 20)

lista_cores = []

for cor in cores:

    # Extrair  cores para usar em outro lugar
    r = cor.rgb.r
    g = cor.rgb.g
    b = cor.rgb.b
    nova = (r, g, b)
    lista_cores.append(nova)

nova_lista = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127,
195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]