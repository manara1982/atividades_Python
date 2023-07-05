class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def adicionar_endereco(self, endereco):
        self.enderecos.append(endereco)

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print("Endereços:")
        for endereco in self.enderecos:
            print(endereco)
        print("------------------------")


class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def excluir_cliente(self, nome_cliente):
        for cliente in self.clientes:
            if cliente.nome == nome_cliente:
                self.clientes.remove(cliente)
                print("Cliente excluído com sucesso!")
                return
        print("Cliente não encontrado.")

    def mostrar_clientes_cadastrados(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in self.clientes:
                cliente.mostrar_dados()


cadastro = CadastroClientes()

while True:
    print("1 - Cadastrar cliente")
    print("2 - Adicionar endereço a cliente")
    print("3 - Mostrar dados de um cliente")
    print("4 - Mostrar clientes cadastrados")
    print("5 - Excluir cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome_cliente = input("Digite o nome do cliente: ")
        cliente = Cliente(nome_cliente)
        cadastro.cadastrar_cliente(cliente)
        print("Cliente cadastrado com sucesso!")

    elif opcao == "2":
        if not cadastro.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            nome_cliente = input("Digite o nome do cliente: ")
            for cliente in cadastro.clientes:
                if cliente.nome == nome_cliente:
                    endereco_cliente = input("Digite o endereço: ")
                    cliente.adicionar_endereco(endereco_cliente)
                    print("Endereço adicionado com sucesso!")
                    break
            else:
                print("Cliente não encontrado.")

    elif opcao == "3":
        if not cadastro.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            nome_cliente = input("Digite o nome do cliente: ")
            for cliente in cadastro.clientes:
                if cliente.nome == nome_cliente:
                    cliente.mostrar_dados()
                    break
            else:
                print("Cliente não encontrado.")

    elif opcao == "4":
        cadastro.mostrar_clientes_cadastrados()

    elif opcao == "5":
        if not cadastro.clientes:
            print("Nenhum cliente cadastrado.")
        else:
            nome_cliente = input("Digite o nome do cliente a ser excluído: ")
            cadastro.excluir_cliente(nome_cliente)

    elif opcao == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")
