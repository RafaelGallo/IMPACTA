from ac04_banco import Cliente, Banco, Conta


# ------------------------ CLIENTE --------------------------------------
# Criação do cliente
cli = Cliente('Joao', 99999999, 'email@mail.com')

# Exibição de dados do cliente
print(cli.get_nome())                       # Joao
print(cli.get_telefone())                   # 99999999
print(cli.get_email())                      # email@mail.com

# Alteração de dados do cliente
cli.set_telefone(77777777)
cli.set_email('novoemail@mail.com')

# Exibição de dados do cliente
print(cli.get_nome())                       # Joao
print(cli.get_telefone())                   # 77777777
print(cli.get_email())                      # novoemail@mail.com

# ------------------------ CONTA ---------------------------------------

c = Conta(cli, 7, 300)
print(c.get_numero())                       # 7
print(c.get_saldo())                        # 300
print(c.get_cliente().get_nome())           # Joao

# realiza operações na conta
c.depositar(250)
c.sacar(50)
c.sacar(150)
print(c.get_saldo())                        # 350

# Verifica o extrato da conta
extrato = c.extrato()
print(len(extrato))                         # 4 (foram feitas quatro operações na conta)
print(extrato)                              # [('saldo_inicial', 300), ('deposito', 250), ('saque', 50), ('saque', 150)]

# ------------------------ BANCO ---------------------------------------

# Criação do Banco
b = Banco('Banco LP2')

# Exibição de dados do banco
print(b.get_nome())                         # Banco LP2

# Abertura da primeira conta
b.abrir_conta(cli, 500)

# Abertura da segunda conta
b.abrir_conta(cli, 1000)

# Lista de contas no banco
lista = b.listar_contas()
print(len(lista))                           # 2 (deve ter dois objetos Conta na lista)

# dados da primeira conta
print(lista[0].get_numero())                # 1
print(lista[0].get_saldo())                 # 500
print(lista[0].get_cliente().get_nome())    # Joao

# dados da segunda conta
print(lista[1].get_numero())                # 2
print(lista[1].get_saldo())                 # 1000
print(lista[1].get_cliente().get_nome())    # Joao

# realiza operações na primeira conta
lista[0].depositar(250)
lista[0].sacar(50)
print(lista[0].get_saldo())                 # 700

# realiza operações na segunda conta
lista[1].depositar(1000)
lista[1].depositar(300)
lista[1].sacar(150)
print(lista[1].get_saldo())                 # 2150

# Verifica o extrato da primeira conta
extrato = lista[0].extrato()
print(len(extrato))                         # 3 (foram feitas três operações na conta)
print(extrato)                              # [('saldo_inicial', 500), ('deposito', 250), ('saque', 50)]

# Verifica o extrato da segunda conta
extrato = lista[1].extrato()
print(len(extrato))                         # 4 (foram feitas quatro operações na conta)
print(extrato)                              # [('saldo_inicial', 1000), ('deposito', 1000), ('deposito', 300), ('saque', 150)]
