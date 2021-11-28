import psycopg2
import json
from flask import Flask, json, request, jsonify


app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register():
    try:
        payload = json.loads(request.data)
        username = payload["username"]
        name = payload["name"]
        email = payload["email"]
        password = payload["password"]
        
        # create generate refferal code
        ref_code = "testref"

        connection = psycopg2.connect(host="localhost",database="micro_db",user="admin",password="password")
        cursor = connection.cursor()

        # email checking
        query = f"SELECT * FROM app_user WHERE email='{email}'"
        cursor.execute(query)

        if cursor.rowcount == 1:
            cursor.close()
            connection.close()
            return jsonify({
                "message":"email has been used",
                "email": email
            }), 400

        query = f"INSERT INTO app_user(id, username, name, email, password, refferal_code) VALUES (uuid_generate_v4(), '{username}', '{name}', '{email}', '{password}', '{ref_code}')"

        cursor.close()
        connection.close()

        return jsonify({
            "message":"Registration Success",
        }), 200

    except Exception as err:
        print(f"ERROR: {err}")
        return jsonify({
            "message":f"ERROR: {err}"
            }), 500

if __name__ == '__main__':
    app.run(port=7020, debug=True)
