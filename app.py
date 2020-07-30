import views
from config import app

# read all contacts
app.add_url_rule('/', view_func=views.home, methods=['GET'])

# read one contact by ID
app.add_url_rule('/<id>', view_func=views.read_one_contact, methods=['GET'])

# create contact
app.add_url_rule('/', view_func=views.create_contact, methods=['POST'])

# update contact by ID
app.add_url_rule('/<id>', view_func=views.update_contact, methods=['PUT'])

# delete contact by ID
app.add_url_rule('/<id>', view_func=views.delete_one_contact,
                 methods=['DELETE'])

# delete all contact
app.add_url_rule('/', view_func=views.delete_all_contact, methods=['DELETE'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
