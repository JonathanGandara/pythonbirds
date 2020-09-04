class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 31

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    daniel = Pessoa(nome='Daniel')
    jonathan = Pessoa(daniel, nome='Jonathan')
    print(Pessoa.cumprimentar(jonathan))
    print(id(jonathan))
    print(jonathan.cumprimentar())
    print(jonathan.nome,jonathan.idade)
    for filho in jonathan.filhos:
        print(filho.nome)
    jonathan.sobrenome = 'Gandara'
    del jonathan.filhos
    jonathan.olhos = 1
    del jonathan.olhos
    print(jonathan.__dict__)
    print(daniel.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(jonathan.olhos)
    print(daniel.olhos)
    print(id(Pessoa.olhos), id(jonathan.olhos), id(daniel.olhos))
    print(Pessoa.metodo_estatico(), jonathan.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), jonathan.nome_e_atributos_de_classe())