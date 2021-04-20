from flask import Flask, render_template, request, flash

menu = ["Установка", "Первое приложение", "Обратная связь"]

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["POST", 'GET'])
def contact():


    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')

        
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug = True)