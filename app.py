from config import app
from views import home


app.add_url_rule('/', view_func=home, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

