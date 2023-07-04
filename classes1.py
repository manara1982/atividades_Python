class Pessoa:
    def __init__(self, nome, idade, peso,):
        self.nome = nome
        self.idade = idade
        self.peso = peso 

    def apresentar(self):
       print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e peso {self.peso} kg.")

    def envelhecer(self, anos):
        self.idade += anos
# Criando um objeto da classe Pessoa
p1 = Pessoa("João", 25, 70,)

# Chamando o método apresentar
p1.apresentar()  # Saída: Olá, meu nome é João e tenho 25 anos.

# Chamando o método envelhecer
p1.envelhecer(5)

# Chamando novamente o método apresentar após o envelhecimento
p1.apresentar()  # Saída: Olá, meu nome é João e tenho 30 anos.
