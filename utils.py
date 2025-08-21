from models import Pessoas

def insere_pessoa():
    pessoa = Pessoas(nome='Leylson', idade=28)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    # Busca pela coluna filtrada
    pessoa = Pessoas.query.filter_by(nome='Leylson').first()
    # Busca todos os registro Nome Pessoa
    #pessoa = Pessoas.query.all()
    print(pessoa.idade)

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rodrigues').first()
    pessoa.idade = 31
    pessoa.save()
    print(pessoa.idade)

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rodrigues').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoa()
    #consulta_pessoa()
    consulta_pessoas()
    #altera_pessoa()
    #exclui_pessoa()