# class Musica:
#     nome = ''
#     artista = ''
#     duracao = int

# musica1 = Musica()
# musica1.nome = 'Bohemian Rhapsody'
# musica1.artista = 'Queen'
# musica1.duracao = 355

# musica2 = Musica()
# musica2.nome = 'Imagine'
# musica2.artista = 'John Lennon'
# musica2.duracao = 183

# musica3 = Musica()
# musica3.nome = 'Shape of You'
# musica3.artista = 'Ed Sheeran'
# musica3.duracao = 234

# print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')

class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)