from flask import Flask, jsonify, request
import joblib
import mysql.connector
from flask_cors import CORS
import re
import threading

mutex = threading.Lock()
count = 0

app = Flask(__name__)
CORS(app)

# Connect to MySQL
# connection = mysql.connector.connect(user='root',
#                                      password='root',
#                                      host='db',
#                                      port='3306',
#                                      database='mockInjection')
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="mockinjection",
)
cursor = connection.cursor()


def haveBlackListWord(input):
    blacklist = [
        "UNION",
        "SELECT",
        "SLEEP",
        "INSERT",
        "UPDATE",
        "DELETE",
        "SHOW",
        "users",
        "service",
        "customer",
        "work_background",
        "graduation_certificate",
        "address",
        "id_card",
        "house_registration",
        "database",
        "table",
        "column",
    ]
    # i -> case-insensitive -> not care upper/lower case
    # '|'.join(blacklist) --> 'badword1|badword2|badword3'
    regex = re.compile(rf"\b({'|'.join(blacklist)})\b", re.IGNORECASE)
    return regex.search(input) is not None


def haveBlackListWordInFile(input):
    blacklist = [
        "UNION",
        "SELECT",
        "SLEEP",
        "SHOW",
        "users",
        "service",
        "customer",
        "work_background",
        "graduation_certificate",
        "address",
        "id_card",
        "house_registration",
        "database",
        "table",
        "column",
        "=",
        "--",
    ]
    regex = re.compile(rf"\b({'|'.join(blacklist)})\b", re.IGNORECASE)
    return regex.search(input) is not None


def validPattern(input):
    pattern = r'^[ก-๏a-zA-Z\d0-9]+$'
    return re.match(pattern, input) is not None


def vectorizer(input):
    vector = joblib.load('./ML/vectorizerv3')
    input = [input]
    input_for_ML = vector.transform(input).toarray()
    return input_for_ML


def randomForest(input):
    model = joblib.load('./ML/random-forestv3')
    result = model.predict(input)
    return result[0]


def SVM(input):
    model = joblib.load('./ML/SVM')
    result = model.predict(input)
    return result[0]


def NaiveBay(input):
    model = joblib.load('./ML/Naive Bayv2')
    result = model.predict(input)
    return result[0]


@app.route("/", methods=['GET'])
def index():
    return jsonify({'success': True})


@app.route("/login", methods=['POST'])
def login():
    data = request.json.get('data')
    username = data.get('username')
    password = data.get('password')

    if (haveBlackListWordInFile(username) or haveBlackListWordInFile(password)):
        mutex.acquire()
        count += 1
        mutex.release()
        return jsonify({'success': "This injection"})
    else:
        return jsonify({'success': "This is not injection"})

    # outPut1 = vectorizer(username)
    # outPut2 = randomForest(outPut1)
    # if outPut2:
    #     mutex.acquire()
    #     count += 1
    #     mutex.release()
    #     return jsonify({'success': "This injection"})
    # else:
    #     return jsonify({'success': "This is not injection"})

    # sql = f'SELECT * FROM users WHERE username = "{username}" AND password = "{password}"'
    # print(sql)
    # cursor.execute(sql)
    # result = cursor.fetchall()

    # if not result:
    #     return jsonify({'success': False})
    # else:
    #     return jsonify({'success': True})


@ app.route("/employee", methods=['GET'])
def employee():
    id = request.args.get('id')
    # print(id)

    if (haveBlackListWordInFile(id)):
        # mutex.acquire()
        global count
        count += 1
        # mutex.release()
        return jsonify({'success': "This injection"})
    else:
        return jsonify({'success': "This is not injection"})
    # outPut1 = vectorizer(id)
    # outPut2 = randomForest(outPut1)
    # if outPut2:
    #     global count
    #     mutex.acquire()
    #     count += 1
    #     mutex.release()
    #     return jsonify({'success': "This injection"})
    # else:
    #     return jsonify({'success': "This is not injection"})

    # if not id:
    #     sql = f'SELECT employee_id, prefixname, fname, lname, nickname, email, tel FROM employee'
    #     print(sql)
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    # else:
    #     sql = f'SELECT employee_id, prefixname, fname, lname, nickname, email, tel FROM employee WHERE employee_id = "{id}"'
    #     print(sql)
    #     cursor.execute(sql)
    #     result = cursor.fetchall()
    #     print(result)

    # if not result:
    #     return jsonify({'success': False}), 401
    # else:
    #     return jsonify(result)


@ app.route("/employee/uploadFile", methods=['POST'])
def employee_upload_file():
    data = request.json.get('fileText')
    sql = f'{data}'

    if (haveBlackListWordInFile(sql)):
        return jsonify({'success': "This injection"})

    cursor.execute(sql)
    connection.commit()
    return jsonify({'success': True})


@ app.route("/count", methods=['GET'])
def getCount():
    return jsonify({'success': True, 'count': count})


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    app.run(host='localhost', port=3000)
    print("Server started on http://localhost:3000")
