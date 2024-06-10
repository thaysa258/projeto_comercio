from ConexaoBD import conexao
from bd import *

conbd = conexao()

while True:
    opcao = int(input("0.sair\n1. cadastrar produto\n2. cadastrar cliente\n3. cadastrar fornecedores\n4. cadastrar funcionario\n5. cadastrar promocoes\n6. atualizar produtos\n7. atualizar cliente\n8. atualizar fornecedores\n9. atualizar funcionarios\n10. atualizar promocoes\n11. deletar produtos\n12. deletar clientes\n13. deletar fornecedores\n14. deletar  funcionarios\n15. deletar promocoes\n16. listar produtos\n17. listar clientes\n18. listar fornecedores\n19. listar funcionarios\n20. listar promocoes\n21. fazer pedido: "))
    if opcao == 0: 
        break
    elif opcao == 1:
        nproduto = input('digite o nome: ')
        dproduto = input('digite a descricao: ')
        pproduto = input (' digite o preco: ')
        quantEstoque = int(input("digite a quantidade do estoque: "))
        opc_cat = input('a categoria ja existe? s/n ')
        if opc_cat == 's': 
            nome_cat= input("digite o nome da categoria: ")
            descricao_cat = ''
        else:
            nome_cat= input("digite o nome da categoria: ")
            descricao_cat =input('digite a descriçao da categoria: ')

        opc_for = input('o fornecedor ja existe? s/n ')
        if opc_for == 's': 
            nome_for= input("digite o nome do fornecedor: ")
            
        else:
           nome_for = input("digite o nome do fornecedor: ")
           contato_for =input('digite o contato do fornecedor: ')
           endereco_for =input('digite o endereco do fornecedor: ')

        cadastrarprodutos(conbd,nproduto,dproduto,pproduto,quantEstoque, nome_cat, descricao_cat,nome_for,contato_for,endereco_for,opc_cat,opc_for)
        
    elif opcao == 2:
        nome = input('digite o nome: ')
        sobrenome = input('digite o sobrenome: ')
        endereco = input('digite o endereco: ')
        cidade = input('digite a cidade: ')
        codigopostal = input('digite o codigo postal:')

        cadastrarclientes(conbd,nome,sobrenome,endereco,cidade,codigopostal)
    elif opcao == 3:
        nome = input('digite o nome: ')
        contato = input('digite o contato: ')
        endereco = input('digite o endereco: ')
        
        cadastrarfornecedores(conbd,nome,contato,endereco)
    elif opcao == 4:
        nome = input('digite o nome: ')
        cargo= input('digite o cargo: ')
        departamento = input('digite o departamento: ')
        
        cadastrarfuncionario(conbd,nome,cargo,departamento)
    elif opcao == 5:
        nome = input('digite o nome do produto: ')
        descricao= input('digite a descricao do produto: ')
        datainicio = input('digite data inicio: ')
        datafim = input('digite data fim: ')
        
        cadastrarpromocoes(conbd,nome,descricao,datainicio,datafim)

    elif opcao == 6:
        nproduto = input('digite o nome: ')
        dproduto= input('digite a descricao: ')
        pproduto= input('digite o preco: ')
        id_produto=int(input('digite o id do produto que deseja atualizar: '))
      
        atualizarproduto(conbd,nproduto,dproduto, pproduto,id_produto)

    elif opcao == 7:
        nome = input('digite o nome: ')
        sobrenome = input('digite o sobrenome: ')
        endereco = input('digite o endereco: ')
        cidade = input('digite a cidade: ')
        codigopostal = input('digite o codigo postal: ')
        id_cliente=int(input('digite o id do cliente que deseja atualizar: '))
      
        atualizarcliente(conbd,nome,sobrenome,endereco,cidade, codigopostal,id_cliente)

    elif opcao == 8:
        nome = input('digite o nome: ')
        contato = input('digite o contato: ')
        endereco = input('digite o endereco: ')
        id_fornecedores=int(input('digite o id do fornecedor que deseja atualizar: '))
      
        atualizarfornecedores(conbd,nome,contato,endereco,id_fornecedores)

    elif opcao == 9:
        nome = input('digite o nome: ')
        cargo= input('digite o cargo: ')
        departamento = input('digite o departamento: ')
        id_funcionario=int(input('digite o id do funcionario que deseja atualizar: '))
      
        atualizarfuncionarios(conbd,nome,cargo,departamento,id_funcionario)

    elif opcao == 10:
        nome = input('digite o nome: ')
        descricao = input('digite a descricao: ')
        datainicio = input('digite a datainicio: ')
        datafim = input('digite a datafim: ')
        id_promocoes =int(input('digite o id da promocao que deseja atualizar: '))
      
        atualizarpromocoes(conbd,nome,descricao,datainicio,datafim,id_promocoes)

    elif opcao == 11:
    
        id_produto=int(input('digite o id do produto que deseja deletar: '))
        opc= input('deseja realmente deletar este produto? s/n ')
        if opc == 's':
            deletar_produtos(conbd,id_produto)
        else: break

    elif opcao == 12:

        id_cliente=int(input('digite o id do cliente que deseja deletar: '))
        opc= input('deseja realmente deletar esse cliente? s/n ')
        if opc == 's':
            deletar_clientes(conbd,id_cliente)
        else: break

    elif opcao == 13:

        id_fornecedores=int(input('digite o id do fornecedor que deseja deletar: '))
        opc= input('deseja realmente deletar esse fornecedor? s/n ')
        if opc == 's':
            deletar_fornecedores(conbd,id_fornecedores)
        else: break

    elif opcao == 14:

        id_funcionario=int(input('digite o id do funcionario que deseja deletar: '))
        opc= input('deseja realmente deletar esse funcionario? s/n ')
        if opc == 's':
            deletar_funcionario(conbd,id_funcionario)
        else: break

    elif opcao == 15:

        id_promocoes=int(input('digite o id da promocoes que deseja deletar: '))
        opc= input('deseja realmente deletar essa promocao? s/n ')
        if opc == 's':
            deletar_promocoes(conbd,id_promocoes)
        else: break

    elif opcao == 16:

        listar_produtos(conbd)

    elif opcao == 17:

        listar_clientes(conbd)

    elif opcao == 18:

        listar_fornecedores(conbd)

    elif opcao == 19:

        listar_funcionario(conbd)

    elif opcao == 20:

        listar_promocoes(conbd)

    elif opcao == 21:
        fazer_pedido(conbd)

   # teste