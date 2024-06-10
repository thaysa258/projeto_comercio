from aifc import Error
import datetime
from os import name 

def cadastrarprodutos(conbd,nome,descricao,preco,quantEstoque,nome_cat,descricao_cat,nome_for,contato_for,endereco_for,opc_cat,opc_for) :
    mycursor = conbd.cursor()
    sql = "insert into Produtos(nome,descricao,preco) values (%s,%s,%s)"
    valores =( nome,descricao,preco)
    mycursor.execute(sql,valores)
    ID_Produto = mycursor.lastrowid

    sql1 = "insert into estoque (ID_Produto,quantidade) values (%s, %s)"
    valores1 =(ID_Produto,quantEstoque)
    mycursor.execute(sql1, valores1)
    if opc_cat == 's': 
        sql3 = 'select ID_Categoria from categoriasprodutos where Nome = %s'
        mycursor.execute(sql3, (nome_cat,))
        id_categoria = mycursor.fetchone()[0]
        int(id_categoria)
        sql4 = 'update produtos set ID_Categoria = %s where ID_Produto = %s'
        val4 = (id_categoria, ID_Produto)
        mycursor.execute(sql4, val4)
    else:
        sql2 = "insert into categoriasprodutos (ID_Categoria,Nome,Descricao) values (%s, %s, %s)"
        valores2 = (ID_Produto,nome_cat,descricao_cat)
        mycursor.execute(sql2, valores2)
        ID_Categoria = mycursor.lastrowid
        sql8 = 'update produtos set ID_Categoria = %s where ID_Produto = %s'
        val8 = (ID_Categoria, ID_Produto)
        mycursor.execute(sql8, val8)


    if opc_for== 's': 
        sql5 = 'select ID_Fornecedor from fornecedores where Nome = %s'
        mycursor.execute(sql5, (nome_for,))
        id_fornecedor = mycursor.fetchone()[0]
        int(id_fornecedor)
        sql6 = 'update produtos set ID_Fornecedor = %s where ID_Produto = %s'
        val6 = (id_fornecedor, ID_Produto)
        mycursor.execute(sql6, val6)

    else:
        sql7 = "insert into fornecedores (Nome,Contato,Endereco) values (%s, %s, %s)"
        val7 = (nome_for,contato_for, endereco_for)
        mycursor.execute(sql7,val7)
        ID_Fornecedor = mycursor.lastrowid
        sql9 = 'update produtos set ID_Fornecedor = %s where ID_Produto = %s'
        val9 = (ID_Fornecedor, ID_Produto)
        mycursor.execute(sql9, val9)

    conbd.commit()
    print ('produto cadastrado com sucesso')
    mycursor.close()


def cadastrarclientes(conbd,nome,sobrenome,endereco,cidade,codigopostal):
    mycursor = conbd.cursor()
    sql = "insert into clientes(nome,sobrenome,endereco,cidade,codigopostal) values (%s,%s,%s,%s,%s)"
    valores =( nome,sobrenome,endereco,cidade,codigopostal)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('clientes cadastrado com sucesso')

    mycursor.close()

def cadastrarfornecedores(conbd,nome,contato,endereco):
    mycursor = conbd.cursor()
    sql = "insert into fornecedores(nome,contato,endereco) values (%s,%s,%s)"
    valores =( nome,contato,endereco)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('fornecedores cadastrado com sucesso')

    mycursor.close()

def cadastrarfuncionario(conbd,nome,cargo,departamento):
    mycursor = conbd.cursor()
    sql = "insert into fornecedor(nome,cargo,departamento) values (%s,%s,%s)"
    valores =( nome,cargo,departamento)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('funcionario cadastrado com sucesso')

    mycursor.close()

def cadastrarpromocoes(conbd,nome,descricao,datainicio,datafim):
    mycursor = conbd.cursor()
    sql = "insert into fornecedor(nome,descricao,datainicio,datafim) values (%s,%s,%s,%s)"
    valores =( nome,descricao,datainicio,datafim)
    mycursor.execute(sql,valores)
    conbd.commit()
    datainicio = datetime.strptime(datainicio,"%d-%m-%y").strftime("%y-%m-%d")
    datafim =  datetime.strptime(datafim,"%d-%m-%y").strftime("%y-%m-%d")
    print(datainicio)
    print(datafim)
    print ("produto cadastrado com sucesso")

    mycursor.close()

def atualizarproduto(conbd,nome,descricao,preco,id_produto):
    mycursor = conbd.cursor()
    sql = "update produtos set Nome = %s, Descricao = %s, Preco = %s where ID_Produto = %s; "
    valores =(nome,descricao,preco,id_produto)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('produto atualizado com sucesso')

    mycursor.close()

def atualizarcliente(conbd,Nome,Sobrenome,Endereco,Cidade,Codigopostal,ID_Cliente):
    mycursor = conbd.cursor()
    sql = "update cliente set Nome = %s, Sobrenome = %s, Cidade = %s, Codigopostal = %s, where ID_Produto = %s; "
    valores =(Nome,Sobrenome,Endereco,Cidade,Codigopostal,ID_Cliente)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('cliente atualizado com sucesso')

    mycursor.close()

def atualizarfornecedores(conbd,Nome,Contato, Endereco,ID_Fornecedores):
    mycursor = conbd.cursor()
    sql = "update fornecedores set Nome = %s, Contato = %s, Endereco = %s,where ID_Fornecedores = %s; "
    valores =(Nome,Contato,Endereco,ID_Fornecedores)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('fornecedores atualizado com sucesso')

    mycursor.close()

def atualizarfuncionarios(conbd,nome,cargo,departamento,ID_Funcionarios):
    mycursor = conbd.cursor()
    sql = "update funcionarios set Nome = %s, Cargo = %s, Departamento = %s,where ID_Funcionarios = %s; "
    valores =(nome,cargo,departamento,ID_Funcionarios)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('funcionario atualizado com sucesso')

    mycursor.close()

def atualizarpromocoes(conbd,nome,descricao,datainicio,datafim):
    mycursor = conbd.cursor()
    sql = "update promocoes set Nome = %s, descricao = %s,datainicio = %s, datafim = %s where ID_Promocoes = %s; "
    valores =(nome, descricao, datainicio, datafim)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('promocoes atualizado com sucesso')
    
    mycursor.close()

def deletar_produtos(conbd,id_produto):
    mycursor = conbd.cursor()
    sql = "delete from produtos where ID_Produto= %s "
    valores = (id_produto,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('produto deletado com sucesso')

    mycursor.close()

def deletar_clientes(conbd,id_clientes):
    mycursor = conbd.cursor()
    sql = "delete from clientes where ID_Clientes= %s "
    valores = (id_clientes,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('cliente deletado com sucesso')

    mycursor.close()

def deletar_fornecedores(conbd,id_fornecedores):
    mycursor = conbd.cursor()
    sql = "delete from fornecedores where ID_Fornecedores= %s "
    valores = (id_fornecedores,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('fornecedor deletado com sucesso')

    mycursor.close()

def deletar_funcionario(conbd,id_funcionario):
    mycursor = conbd.cursor()
    sql = "delete from funcionario where ID_fFuncionario= %s "
    valores = (id_funcionario,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('funcionario deletado com sucesso')

    mycursor.close()

def deletar_promocoes(conbd,id_promocoes):
    mycursor = conbd.cursor()
    sql = "delete from promocoes where ID_Promocoes= %s "
    valores = (id_promocoes,)
    mycursor.execute(sql,valores)
    conbd.commit()
    print ('promocoes deletado com sucesso')

    mycursor.close()

def listar_produtos(conbd):
    mycursor = conbd.cursor()
    sql = "select * from produtos"
    mycursor.execute(sql)
    produtos = mycursor.fetchall()
    for produto in produtos:
        print (f'{produto[1]},{produto[2]},{produto[3]}')  

def listar_clientes(conbd):
    mycursor = conbd.cursor()
    sql = "select * from clientes"
    mycursor.execute(sql)
    clientes = mycursor.fetchall()
    for cliente in clientes:
        print(f'{cliente[1]}, {cliente[2]}, {cliente[3]},{cliente[4]}')  

def listar_fornecedores(conbd):
    mycursor = conbd.cursor()
    sql = "select * from fornecedores"
    mycursor.execute(sql)
    fornecedores = mycursor.fetchall()
    for fornecedore in fornecedores:
        print(f'{fornecedores[1]}, {fornecedores[2]}, {fornecedores[3]}')  

def listar_funcionario(conbd):
    mycursor = conbd.cursor()
    sql = "select * from funcionarios"
    mycursor.execute(sql)
    funcionario = mycursor.fetchall()
    for funcionario in funcionario:
        print(f'{funcionario[1]}, {funcionario[2]}, {funcionario[3]}')  

def listar_promocoes(conbd):
    mycursor = conbd.cursor()
    sql = "select * from promocoes"
    mycursor.execute(sql)
    promocoes = mycursor.fetchall()
    for promocoes in promocoes:
        print(f'{promocoes[1]}, {promocoes[2]}, {promocoes[3]}, {promocoes[4]}')

def obterProdutoID(conbd, nome):
    try:
        with conbd.cursor() as cursor:
            sql = 'SELECT ID_Produto FROM produtos WHERE Nome = %s'
            cursor.execute(sql, (nome,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                print(f"Produto com nome '{nome}' não encontrado.")
                return None
    except Error as e:
        print(f"Ocorreu um erro ao obter o ID do produto: {e}")
        return None


def deletarProduto(conbd, nome_produto):
    try:
        produto_id = obterProdutoID(conbd, nome_produto)
        if not produto_id:
            return
        
        conbd.start_transaction()
        with conbd.cursor() as cursor:
            sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
            cursor.execute(sql_detalhes_pedido, (produto_id,))

        with conbd.cursor() as cursor:
            sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
            cursor.execute(sql_estoque, (produto_id,))

        with conbd.cursor() as cursor:
            sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
            cursor.execute(sql_produto, (produto_id,))
        conbd.commit()
        print("Produto e suas referências deletadas com sucesso")

    except Error as e:
        conbd.rollback()
        print(f"Ocorreu um erro ao deletar o produto: {e}")

    finally:
        conbd.close()

def fazer_pedido(cliente,produto,quantidade,preco):
    ("insert into pedidos (cliente,produto,quantidade,preco) values(%s,%s,%s,%s)")
    valores = (cliente,produto,quantidade,preco)
    
    sql_produto = 'DELETE FROM produtos WHERE ID_Produto = %s'
    cursor.execute(sql_produto, (ID_Produto,))

    sql_estoque = 'DELETE FROM estoque WHERE ID_Produto = %s'
    cursor.execute(sql_estoque, (produto_id,))

    sql_detalhes_pedido = 'DELETE FROM detalhespedido WHERE ID_Produto = %s'
    cursor.execute(sql_detalhes_pedido, (produto_id,)) # teste

  
   
    
    

   