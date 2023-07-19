""" 
O objetivo deste código é criar, atualizar, deletar alguns contatos e mostrar uma lista de contatos em ordem alfabética.
"""
lista_contatos = []
lista_contatos_ordem = []

def mostrar_funcao():
    print('=======================================================================')
    print('Escreva [Criar] para adicionar um contato.')
    print('Escreva [Mostrar] para mostrar a lista de contatos em ordem alfabética.')
    print('Escreva [Mudar] para atualizar um contato da lista de contatos.')
    print('Escreva [Apagar] para deletar um contato da lista de contatos.')
    print('Escreva [Parar] para sair da lista de contatos.')
    print('=======================================================================')
    return

def criar_contato():
    contato = input('Nome do contato: ')
    lista_contatos.append(contato)
    return
    
def mostrar_ordem():
    lista_contatos_ordem = sorted(lista_contatos, key=str.lower)
    
    for num, nome in enumerate(lista_contatos_ordem, 1):
        print(f'{num}. {nome}')       
    
    return

def atualizar():
    novo_contato = input("Qual contato atualizar: ")  
    
    for i in range(0, len(lista_contatos)):
        if lista_contatos[i] == novo_contato:
            novo = input('Nome do novo contato: ')
            lista_contatos[i] = novo
    return 

def deletar():
    apagar = str(input('Qual contato apagar: '))
    i = lista_contatos.index(apagar)
    del lista_contatos[i]
    return
    
mostrar_funcao()

comando = True

while comando != False:
    print('==================')
    comando = input("Digite: ")
    print('==================')
    
    if comando != 'Criar' and comando and 'Mostrar' and comando != 'Mudar' and comando != 'Apagar' and comando != 'Parar':
        print('Não é um comando válido')
            
    if comando == 'Criar':
        criar_contato()
        print('Contato adicionado.')
        #for nome in lista_contatos:
            #print(f'.{nome}')
         
    elif comando == 'Mostrar':
        mostrar_ordem()
        if comando == 'Mostrar' and lista_contatos == []:
            print('Não há contatos listados para exibir.')        
    
    elif comando == 'Mudar':
        atualizar()
        if lista_contatos == []:
            print('Não há contatos para atualizar.')
        else:
            print('Contato atualizado.')
         
    elif comando == 'Apagar':
        try:
            deletar()
            print('Contato apagado.')
        except ValueError:
            print('Não há contato para apagar.')
    else:
        if comando == 'Parar':
            break
    
    
    
    