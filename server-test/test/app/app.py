from flask import Flask,jsonify, request ,render_template
import mysql.connector
import re
import joblib

app = Flask(__name__,template_folder='views')




connection = mysql.connector.connect(user = 'root',
        password = 'root',
        host= 'db',
        port= '3306',
        database= 'mockInjection')

@app.route('/')
def index2():
    return render_template('login.html')

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
    ]
    regex = re.compile(rf"\b({'|'.join(blacklist)})\b", re.IGNORECASE)
    return regex.search(input) is not None


def validPattern(input):
    pattern = r'^[ก-๏a-zA-Z\d0-9]+$'
    return not re.match(pattern, input)

def vectorizer(input):
    vector= joblib.load('./ML/vectorizerv4')
    input = [input]
    input_for_ML = vector.transform(input).toarray()
    return input_for_ML

def randomForest(input):
    model = joblib.load('./ML/random-forestv3')
    result=model.predict(input)
    return result[0]

def SVM(input):
    model = joblib.load('./ML/SVM')
    result=model.predict(input)
    return result[0]

def NaiveBay(input):
    model = joblib.load('./ML/Naive Bayv2')
    result=model.predict(input)
    return result[0]



@app.route("/", methods=['GET'])
def index():
    return jsonify({'success': True})


@app.route("/login", methods=['POST'])
def login():
    data = request.json.get('data')
    username = data.get('username')
    password = data.get('password')

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()

    if not result:
        return jsonify({'success': False}), 401
    else:
        return jsonify({'success': True})

    

@app.route("/employee", methods=['GET'])
def employee():
    id = request.args.get('id')

    cursor = connection.cursor()
    if not id:
        cursor.execute(
            "SELECT employee_id, prefixname, fname, lname, nickname, email, tel FROM employee")
        result = cursor.fetchall()
    else:
        cursor.execute(
            "SELECT employee_id, prefixname, fname, lname, nickname, email, tel FROM employee WHERE employee_id = %s", (id,))
        result = cursor.fetchone()

    if not result:
        return jsonify({'success': False}), 401
    else:
        return jsonify(result)


@app.route("/employee/uploadFile", methods=['POST'])
def employee_upload_file():
    data = request.json.get('fileText')
    cursor = connection.cursor()
    cursor.execute(data)
    connection.commit()
    return jsonify({'success': True})



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

