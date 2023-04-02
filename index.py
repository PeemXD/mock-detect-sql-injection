import time
from flask import Flask, jsonify, request
import joblib
import mysql.connector
from flask_cors import CORS
import re
import threading

mutex = threading.Lock()

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

count = 0
ruleBaseCount = 0
NaiveBayCount = 0
randomforestCount = 0
knnCount = 0
NaiveBayCount_smote = 0
randomforestCount_smote = 0
knnCount_smote = 0


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


def vectorizerOld(input):
    vector = joblib.load('ML/vectorizerv3')
    input = [input]
    input_for_ML = vector.transform(input).toarray()
    return input_for_ML


def randomForestOld(input):
    model = joblib.load('ML/random-forestv3')
    result = model.predict(input)
    return result[0]


def vectorizer(input):
    vector = joblib.load('ML-last/vectorizerFinal')
    input = [input]
    input_for_ML = vector.transform(input).toarray()
    return input_for_ML


def naiveBay(input):
    model = joblib.load('ML-last/NaiveBay')
    result = model.predict(input)
    return result[0]


def randomForest(input):
    model = joblib.load('ML-last/randomforest')
    result = model.predict(input)
    return result[0]


def KNN(input):
    model = joblib.load('ML-last/knn')
    result = model.predict(input)
    return result[0]


def vectorizerSmote(input):
    vector = joblib.load('ML-smote-v2/vectorizer_smotev2')
    input = [input]
    input_for_ML = vector.transform(input).toarray()
    return input_for_ML


def naiveBaySmote(input):
    model = joblib.load('ML-smote-v2/NaiveBay_SMOTEv2')
    result = model.predict(input)
    return result[0]


def randomForestSmote(input):
    model = joblib.load('ML-smote-v2/randomforest_SMOTEv2')
    result = model.predict(input)
    return result[0]


def KNNSmote(input):
    model = joblib.load('ML-smote-v2/knn_SMOTEv2')
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

    #! RuleBase
    # if (haveBlackListWordInFile(username) or haveBlackListWordInFile(password)):
    #     mutex.acquire()
    #     count += 1
    #     mutex.release()
    #     return jsonify({'success': "This injection"})
    # else:
    #     return jsonify({'success': "This is not injection"})

    #! ML
    # outPut1A = vectorizer(username)
    # outPut1B = vectorizer(password)
    # outPut2A = naiveBay(outPut1A)
    # outPut2B = naiveBay(outPut1B)
    # # outPut2A = randomForest(outPut1A)
    # # outPut2B = randomForest(outPut1B)
    # # outPut2A = KNN(outPut1A)
    # # outPut2B = KNN(outPut1B)
    # if outPut2A or outPut2B:
    #     mutex.acquire()
    #     count += 1
    #     mutex.release()
    #     return jsonify({'success': "This injection"})
    # else:
    #     return jsonify({'success': "This is not injection"})

    #! test ML
    outPut1A = vectorizer(username)
    outPut1B = vectorizer(password)
    outPut2A1 = naiveBay(outPut1A)
    outPut2A2 = naiveBay(outPut1B)
    outPut2B1 = randomForest(outPut1A)
    outPut2B2 = randomForest(outPut1B)
    outPut2C1 = KNN(outPut1A)
    outPut2C2 = KNN(outPut1B)

    global NaiveBayCount, randomforestCount, knnCount, count
    if outPut2A1 or outPut2A2:
        NaiveBayCount += 1
    if outPut2B1 or outPut2B2:
        randomforestCount += 1
    if outPut2C1 or outPut2C2:
        knnCount += 1
    count += 1
    return jsonify({'success': True})

    #! core api
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
    print(id)
    #! test
    # ? RuleBase
    outPutRuleBase = haveBlackListWord(id)

    # ? No smote
    outPutV = vectorizer(id)
    outPutVOld = vectorizerOld(id)
    outPutNB = naiveBay(outPutV)
    outPutRF = randomForestOld(outPutVOld)
    outPutKNN = KNN(outPutV)

    # ? have smote
    outPutVSmote = vectorizerSmote(id)
    outPutNBSmote = naiveBaySmote(outPutVSmote)
    outPutRFSmote = randomForestSmote(outPutVSmote)
    outPutKNNSmote = KNNSmote(outPutVSmote)

    global count,  ruleBaseCount, NaiveBayCount, randomforestCount, knnCount, NaiveBayCount_smote, randomforestCount_smote, knnCount_smote
    count += 1
    while True:  # wait until all ml success
        if outPutNB is not None and outPutRF is not None and outPutKNN is not None:
            break
        time.sleep(0.1)  # wait for 100 milliseconds before checking again
    # print(count, outPut2A, outPut2B, outPut2C)
    if (outPutRuleBase):
        # mutex.acquire()
        ruleBaseCount += 1
        # mutex.release()
    if outPutNB:
        NaiveBayCount += 1
    if outPutRF:
        randomforestCount += 1
    if outPutKNN:
        knnCount += 1
    if outPutNBSmote:
        NaiveBayCount_smote += 1
    if outPutRFSmote:
        randomforestCount_smote += 1
    if outPutKNNSmote:
        knnCount_smote += 1
    return jsonify({'success': True})

    #! RuleBase
    # if (haveBlackListWordInFile(id)):
    #     # mutex.acquire()
    #     global count
    #     count += 1
    #     # mutex.release()
    #     return jsonify({'success': "This injection"})
    # else:
    #     return jsonify({'success': "This is not injection"})

    #! core api
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
    global count,  ruleBaseCount, NaiveBayCount, randomforestCount, knnCount, NaiveBayCount_smote, randomforestCount_smote, knnCount_smote
    result = jsonify({'total': count,
                      'RuleBase': '% .4f' % (ruleBaseCount/count),
                      'NaiveBay': '% .4f' % (NaiveBayCount/count),
                      'randomforest': '% .4f' % (randomforestCount/count),
                      'knn': '% .4f' % (knnCount/count),
                      'NaiveBay_smote': '% .4f' % (NaiveBayCount_smote/count),
                      'randomforest_smote': '% .4f' % (randomforestCount_smote/count),
                      'knn_smote': '% .4f' % (knnCount_smote/count), })
    # NaiveBayCount, randomforestCount, knnCount, count = 0
    return result


if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    print("Server started on http://localhost:3000")
    app.run(host='localhost', port=3000)
