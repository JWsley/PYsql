from datetime import datetime
import mysql.connector


class Db:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            password = 'q1w2e3',
            database = 'db_banco_crud'
        )

        self.meu_cursor = self.conexao.cursor()


    def exib(self):
        self.meu_cursor.execute('select * from pessoas'  )
        list = self.meu_cursor.fetchall()
        for i in list:
           print('==================================================')
           print("•",i,">>>")
           print('==================================================')

#U

    def update(self):
        nome  = input('Informe um novo nome:')
        cod  = int(input('Informe o codigo:'))
        sql = f'update pessoas set nome = "{nome}" where id="{cod}"'
        self.meu_cursor.execute(sql)
        self.conexao.commit()





#D

    def delete(self):
        cod2  = int(input('Informe o codigo:'))
        sql2 = f'delete from pessoas 2 where id = {cod2}'
        self.meu_cursor.execute(sql2)
        self.conexao.commit()



    def create(self):
        nome  = input('Informe um novo nome:')
        dataNasc  = datetime(input('Informe o codigo:'))
        self.meu_cursor.execute(f'insert into pessoas (nome,dataNasc) value ("{nome}","{dataNasc}")')
        self.conexao.commit()   #EXECUTA O SCRIPT SQL NO BANCO


        
obj_db = Db()


resp = ''

while resp != '0' and resp !='1' and resp != '2' and resp != 3:
    print('0-printar tela....1-Update  2-Delete')


    resp = input('|:')



if resp == 3:
   obj_db.create()
if resp == '2':
   obj_db.delete()
if resp == '1':
   obj_db.update()
if resp == '0':
   obj_db.exib()




