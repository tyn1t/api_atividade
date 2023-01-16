from flask import Flask ,request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#    'Anderlan':'123',
 #   'galleani':'321'
 #   }


#@auth.verify_password
#def varificacao(login, senha):
#    if not (login,senha):
#        return False
#    return USUARIOS.get('login') == 'senha':

@auth.verify_password
def varificacao(login, senha):
    if not (login,senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.ids
             }
        except AttributeError:
            response = {
                'Status':'Error',
                'Mensagem':'Pessoa nao encontrada'
            }
        return response
    
    def pus(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in  dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome':pessoa.nome,
            'idade':pessoa.idade,
            'id':pessoa.ids
            }
        return  response
    
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com  sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso','mensagem':mensagem}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.ids,'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response
    
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.ids,
            'nome':pessoa.nome,
            'idade':pessoa.idade
            }
        return response

class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        print(atividades)
        response = [{'id': i.ids, 'nome': i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id': atividade.ids
            }
        return response
api.add_resource(Pessoa, '/pessoa/<string:nome>/')    
api.add_resource(ListaPessoas,  '/pessoa/' )
api.add_resource(ListaAtividade,  '/atividade/' )

if __name__=="__main__":
    app.run(debug=True)
