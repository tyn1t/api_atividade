from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome="Galleani", idade=29)
    print(pessoa)
    pessoa.save()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def Consulta_todos_usuario():
    usuario = Usuarios.query.all()
    print(usuario)
    
# Realiza consulta na tabela pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    print(pessoa.idade)

#Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()
def exclui_usuario(login):
    usuario = Usuarios.query.filter_by(login=login).first()
    usuario.delete()
# Exclui daddos na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

if __name__=="__main__":
    insere_usuario('A','123456')
    insere_usuario('p','1234567')
    #exclui_usuario('A')
    Consulta_todos_usuario()

    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
