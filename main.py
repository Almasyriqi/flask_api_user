import pymysql
from app import app 
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/user')
def user():
    try:
        _json = request.args
        print(_json['data'])
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        userRows = cursor.fetchall()
        respon = jsonify(userRows)
        respon.status_code = 200
        print("coba print aja")
        return respon
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()