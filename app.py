from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

#-------------Banco de Dados----------------------
# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Tabelas
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String(100), nullable=False)
    observacoes = db.Column(db.Text)

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)
    nota_segundo_semestre = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

# Criar as tabelas no banco de dados
with app.app_context():
    db.create_all()

#-----------ROTAS----------------------------------------------------
@app.route('/')
def home():
    return jsonify({"mensagem": "API de Gestão Escolar"}), 200

#Rota para os professores

#Criar um professor
@app.route('/professores', methods=['POST'])
def criar_professor():
    dados = request.json
    novo_professor = Professor(
        nome=dados['nome'],
        idade=dados['idade'],
        materia=dados['materia'],
        observacoes=dados.get('observacoes', '')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify({"mensagem": "Professor cadastrado com sucesso!"}), 201

#Listar professores
@app.route('/professores', methods=['GET'])
def listar_professores():
    professores = Professor.query.all()
    resultado = [
        {
            "id": p.id, 
            "nome": p.nome, 
            "idade": p.idade, 
            "materia": p.materia, 
            "observacoes": p.observacoes
         }

        for p in professores
    ]
    return jsonify(resultado)


#Buscar Professor por ID
@app.route('/professores/<int:id>', methods=['GET'])
def buscar_professor(id):
    professor = Professor.query.get(id)

    if not professor:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    resultado = {
        "id": professor.id, 
        "nome": professor.nome, 
        "idade": professor.idade, 
        "materia": professor.materia, 
        "observacoes": professor.observacoes
    }

    return jsonify(resultado)


#Atualizar Professor
@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({"erro": "Professor não encontrado"}), 404

    dados = request.json
    professor.nome = dados['nome']
    professor.idade = dados['idade']
    professor.materia = dados['materia']
    professor.observacoes = dados.get('observacoes', '')
    
    db.session.commit()
    return jsonify({"mensagem": "Professor atualizado com sucesso!"})

#Excluir um professor
@app.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    professor = Professor.query.get(id)
    if not professor:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
    db.session.delete(professor)
    db.session.commit()
    return jsonify({"mensagem": "Professor deletado com sucesso!"})


#Rota para alunos

#Adicionar aluno
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.json

    data_nascimento = datetime.strptime(dados['data_nascimento'], '%Y-%m-%d').date()  # Converte a string de data para um objeto datetime.date

    novo_aluno = Aluno(
        nome=dados['nome'],
        idade=dados['idade'],
        data_nascimento=data_nascimento,
        nota_primeiro_semestre=dados.get('nota_primeiro_semestre'),
        nota_segundo_semestre=dados.get('nota_segundo_semestre'),
        media_final=dados.get('media_final')
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno cadastrado com sucesso!"}), 201

#Listar Alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    resultado = [
        {
            "id": a.id, 
            "nome": a.nome, 
            "idade": a.idade, 
            'data_nascimento': a.data_nascimento.strftime('%Y-%m-%d'),
            "nota_primeiro_semestre": a.nota_primeiro_semestre, 
            "nota_segundo_semestre": a.nota_segundo_semestre, 
            "media_final": a.media_final
        }
        for a in alunos
    ]
    return jsonify(resultado)

#Buscar aluno por ID
@app.route('/alunos/<int:id>', methods=['GET'])
def buscar_alunos(id):
    alunos = Aluno.query.get(id)
    if not alunos:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    return jsonify({
    "id": alunos.id, 
    "nome": alunos.nome, 
    "idade": alunos.idade, 
    "data_nascimento": alunos.data_nascimento, 
    "nota_primeiro_semestre": alunos.nota_primeiro_semestre, 
    "nota_segundo_semestre": alunos.nota_segundo_semestre, 
    "media_final": alunos.media_final
})


#Atualizar Aluno
@app.route('/aluno/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    alunos = Aluno.query.get(id)
    if not alunos:
        return jsonify({"erro": "Aluno não encontrado"}), 404

    dados = request.json
    alunos.nome=dados['nome']
    alunos.idade=dados['idade']
    alunos.data_nascimento=dados['data_nascimento']
    alunos.nota_primeiro_semestre=dados.get('nota_primeiro_semestre')
    alunos.nota_segundo_semestre=dados.get('nota_segundo_semestre')
    alunos.media_final=dados.get('media_final')
    
    db.session.commit()
    return jsonify({"mensagem": "Aluno atualizado com sucesso!"})

#Excluir Aluno
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_alunos(id):
    alunos = Aluno.query.get(id)
    if not alunos:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    
    db.session.delete(alunos)
    db.session.commit()
    return jsonify({"mensagem": "Aluno deletado com sucesso!"})

if __name__ == '__main__':
    app.run(debug=True)
