from config import conn


def create_table():
    """ create table if the table does not exist """
    cursor = conn.cursor()
    cursor.execute("""
		CREATE TABLE IF NOT EXISTS contacts(
		    id serial,
		    name character varying(255) NOT NULL UNIQUE,
		    number character varying(10) NOT NULL UNIQUE,
		    created_at timestamp without time zone DEFAULT \
		    	CURRENT_TIMESTAMP NOT NULL,
		    updated_at timestamp without time zone);""")

    close_connection(cursor)


def close_connection(cursor):
    """ close connection to cursor and database """
    conn.commit()
    cursor.close()


def create(name, number):
    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO contacts (name, number) \
				VALUES(%s, %s)", (name, number))
    close_connection(cursor)


def read_all():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    s = cursor.fetchall()
    close_connection(cursor)
    return s


def read_one(id):
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, number FROM contacts \
		WHERE id=%s", (id, ))
    s = cursor.fetchone()
    close_connection(cursor)
    return s


def update(id, name, number):
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=%s, number=%s \
		WHERE id=%s", (name, number, id,))
    close_connection(cursor)


def delete_one(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=%s", (id,))
    close_connection(cursor)


def delete_all():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts")
    close_connection(cursor)


# call create_table inside db.py to make sure that always
# the table exist or is created before any CRUD
create_table()
