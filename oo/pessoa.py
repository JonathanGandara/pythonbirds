class Pessoa:
    nome = None

    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    daniel = Pessoa(nome='Daniel')
    jonathan = Pessoa(daniel, nome='Jonathan')
    print(Pessoa.cumprimentar(jonathan))
    print(id(jonathan))
    print(jonathan.cumprimentar())
    print(jonathan.nome,jonathan.idade)
    for filho in jonathan.filhos:
        print(filho.nome)
