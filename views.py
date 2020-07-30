from flask import jsonify, request

import db


def home():
    status = False
    data = {}

    data = db.read_all()

    if data:
        status = True

    return jsonify({"status": status, "data": data})


def read_one_contact(id):
    status = False
    data = {}

    data = db.read_one(id)

    if data:
        status = True

    return jsonify({"status": status, "data": data})


def create_contact():
    status = False

    if request.method == 'POST':
        if request.form['name'] and request.form['number']:
            name = request.form['name']
            number = request.form['number']

            if db.create(name, number):
                status = True

    return jsonify({"status": status})


def update_contact(id):
    status = False

    if request.method == 'PUT':
        if request.form['name'] and request.form['number']:

            name = request.form['name']
            number = request.form['number']

            if db.update(id, name, number):
                status = True

    return jsonify({"status": status})


def delete_one_contact(id):
    status = False

    if request.method == 'DELETE':
        if db.delete_one(id):
            status = True

    return jsonify({"status": status})


def delete_all_contact():
    status = False

    if request.method == 'DELETE':
        if db.delete_all():
            status = True

    return jsonify({"status": status})
