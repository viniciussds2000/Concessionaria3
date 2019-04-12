from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/adm_page')
def adm_page():
    return render_template('adm_page.html')

@app.route('/detalhes')
def detalhes_compra():
    return render_template('detalhes.html')

@app.route('/final_reserva')
def fin_compra():
    return render_template('tela_compra.html')




if __name__ == '__main__':
    app.run(debug=True)


