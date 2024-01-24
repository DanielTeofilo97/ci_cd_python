from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastrar_chegada():
    if request.method == 'POST':
        placa = request.form['firstname']
        cpf = request.form['lastname']

        print(f'Placa do Veículo: {placa}, CPF: {cpf}')

        return 'Cadastro realizado com sucesso!'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')