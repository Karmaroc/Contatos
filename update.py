def update():
    dic.update(dic2)
    return print(dic)

dic = {'nome': 'Vitor',
       'sobrenome': 'Vieira',
       'idade': '23',
       'pais': 'Brasil'
       }

dic2 = {'pais': 'Holanda'}

update()