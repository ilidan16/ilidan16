from flask import Flask, render_template, url_for, request

menu = ["Установка", "Первое приложение", "Обратная связь"]

app = Flask(__name__)

@app.route('/')
def index():
    print( url_for('index') )
    return render_template('index.html', menu=menu)

@app.route('/about')
def about():
    print( url_for('about') )
    return render_template('about.html')


@app.route('/contact', methods=["POST", 'GET'])
def contact():
    if request.method == 'POST':
        print(request.form)

        
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug = True)