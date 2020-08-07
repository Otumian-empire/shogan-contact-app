# shogan-contact-app
This is a simple sql app (actually a flask app) that CRUD of a postgres database


## How to
There simply two ways for this to work, with `Pipfile` or `requirements.txt`
* Clone app from github, `git clon https://github.com/Otumian-empire/shogan-contact-app.git`
* Create a database, `sample_db`
* In the root directory, create a `.env` file with the content:
    ``` env
    DB_USER='postgres'
    DB_PASSWORD='your-password'
    DB_HOST='127.0.0.1'
    DB_PORT='5432'
    DB_NAME='sample_db'
    ```
* Database user is `postgres`
* Datbas password is required
* In the `.sql` file, update the owner, `ALTER SCHEMA public OWNER TO postgres;` to your database user. Ignore if user is `postgres`
* Save and import the updated `.sql` file into phppgadmin
* `cd` in root directory
* #### with `Pipfile`
    * `pipenv install`
    * `pipenv shell`
* #### with `requirements.txt`
    * `pip3 install -r requirements.txt`
* `python app`
* open `http://127.0.0.1:5000` in browser
* Press `CTRL+C` to quit
