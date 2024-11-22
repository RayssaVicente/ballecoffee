from flask import Blueprint, render_template, request, jsonify
from database.comentarios import COMENTARIOS

receitas_routes = Blueprint('receitas', __name__)

"""
Rotas da página Receitas
 - /receitas/listaComentarios (GET) - Listar os comentários
 - /receitas/listaComentarios (POST) - Inserir o comentário no servidor
 - /receitas/new (GET) - Renderizar o formulário para criar um cliente
 - /receitas/<id> (GET) - Obter os dados de um cliente
 - /receitas/<id>/edit (GET) - Renderizar um formulário para editar um comentário
 - /receitas/<id>/update (PUT) - Atualizar um comentário  
 - /receitas/<id>/delete (DELETE) - Deletar o comentário do usuário
"""

@receitas_routes.route('/')
def home():
    comentarios = COMENTARIOS
    return render_template('receitas.html', comentarios=COMENTARIOS)

@receitas_routes.route('/', methods=['POST'])
def inserir_comentario():
    # Adicionando um novo comentario
    novo_comentario = {
        "nomeEstabelecimento": request.form.get("nomeEstabelecimento"),
        "nomeBebida": request.form.get("nomeBebida"),
        "comentario": request.form.get("comentario"),
        "avaliacao": request.form.get("avaliacao"),
    }

   
    novo_comentario["id"] = max([c["id"] for c in COMENTARIOS], default=0) + 1

    
    COMENTARIOS.append(novo_comentario)

    
    return render_template('receitas.html', comentarios=COMENTARIOS)
    


@receitas_routes.route('/<int:comentario_id>/delete', methods=['DELETE'])
def deletar_comentario(comentario_id):
    # Deletar comentário
    global COMENTARIOS
    comentario = next((c for c in COMENTARIOS if c['id'] == comentario_id), None)

    if not comentario:
        return jsonify({'error': 'Comentário não encontrado'})

    # Remover o comentário da lista
    COMENTARIOS = [c for c in COMENTARIOS if c['id'] != comentario_id]

    return jsonify({'deleted': 'ok'})
