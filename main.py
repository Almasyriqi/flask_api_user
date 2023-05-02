import pymysql
from app import app 
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/user')
def user():
    try:
        _param = request.args
        _form = request.form
        print("Request data dari param : " + _param['data'])
        print("Request data dari form : " + _form['data'])
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user")
        userRows = cursor.fetchall()
        respon = jsonify(userRows)
        respon.status_code = 200
        return respon
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        
@app.route('/user/<int:user_id>')
def user_details(user_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM user WHERE id =%s", user_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
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