from flask import Flask, render_template, request, flash
#import semester_1.primality_test as test

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simplicity', methods=["POST", 'GET'])
def simplicity():
    if request.method == 'POST':
        number = request.form['enter']

        if len(request.form['enter']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')

        

    
    return render_template('simplicity.html')

if __name__ == "__main__":
    app.run(debug = True)