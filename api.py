from flask import Flask, render_template, request, redirect, url_for
import usuarios

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    """Exibe a página inicial com a lista de usuários."""
    usuarios_cadastrados = usuarios.get_users()
    return render_template('index.html', usuarios=usuarios_cadastrados)

@app.route('/add', methods=['POST'])
def add_usuario():
    """Adiciona um novo usuário e redireciona para a página inicial."""
    nome = request.form['nome']
    idade = request.form['idade']
    email = request.form['email']
    telefone = request.form['telefone']
    usuarios.add_user(nome, idade, email, telefone)
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_usuario(id):
    """Exclui um usuário e redireciona para a página inicial."""
    usuarios.delete_user(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
