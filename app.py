from config import app, conn


@app.route('/', methods=['GET', 'POST'])
def home():
    return "This is the index page"


if __name__ == '__main__':
    app.run(debug=True)

