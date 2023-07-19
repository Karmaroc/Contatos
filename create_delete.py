""" 
Declarei uma lista vazia, duas funções diferentes e um loop while que sucede até 10 elementos na lista.
A primeira função adiciona um elemento na lista e a segunda função elimina o último elemento duas vezes,
incluindo a str 'apagar' da variável 'nome' dentro da condicional if. 
"""

arm = []

def criar():    
    arm.append(nome)
    return

def apagar():
    arm.pop() 
    arm.pop()
    return

while len(arm) < 10:
    nome = input("Digite um elemento: ")        

    criar()

    if nome == 'apagar':
        apagar()
        
    print(arm)
        
    

        

        
        


    


