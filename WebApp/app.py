from flask import Flask, render_template, request, flash
import primality_test as test

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simplicity', methods=["POST", 'GET'])
def simplicity():
    if request.method == 'POST':
        number = int(request.form['enter'])
        result = test.primality_test_2_0(number)

        if result:
            flash('Да')
        else:
            flash('Нет')

        

    
    return render_template('simplicity.html')

if __name__ == "__main__":
    app.run(debug = True)