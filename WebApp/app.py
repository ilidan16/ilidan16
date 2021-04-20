from flask import Flask, render_template, url_for

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


if __name__ == "__main__":
    app.run(debug = True)