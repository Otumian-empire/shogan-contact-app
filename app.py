import views
from config import app

# read all contacts
app.add_url_rule('/api/', view_func=views.home, methods=['GET'])

# read one contact by ID
app.add_url_rule(
    '/api/<id>', view_func=views.read_one_contact, methods=['GET'])

# create contact
app.add_url_rule('/api/', view_func=views.create_contact, methods=['POST'])

# update contact by ID
app.add_url_rule('/api/<id>', view_func=views.update_contact, methods=['PUT'])

# delete contact by ID
app.add_url_rule('/api/<id>', view_func=views.delete_one_contact,
                 methods=['DELETE'])

# delete all contact
app.add_url_rule('/api/', view_func=views.delete_all_contact,
                 methods=['DELETE'])
# ----------------------------------------------------------------- #

# readme page
app.add_url_rule('/', view_func=views.readme_page, methods=['GET'])
app.add_url_rule('/readme', view_func=views.readme_page, methods=['GET'])

# home page
app.add_url_rule('/web/', view_func=views.home_page, methods=['GET'])

# add contact page
app.add_url_rule('/web/add/', view_func=views.add_page, methods=['GET'])

# update contact page
app.add_url_rule('/web/update/<id>',
                 view_func=views.update_page, methods=['GET'])

# delete one contact
app.add_url_rule('/web/delete/<id>',
                 view_func=views.delete_page, methods=['GET'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
