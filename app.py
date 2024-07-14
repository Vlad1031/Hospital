# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message

from views.employees import employees, subdivision_employees
from views.gallery import gallery_images, gallery_all_images
# from views.general_info import general_info_list

app = Flask(__name__)

app.config.from_pyfile('views/config.py')


app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', app.config.get('MAIL_SERVER'))
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT', app.config.get('MAIL_PORT'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', app.config.get('MAIL_USERNAME'))
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', app.config.get('MAIL_PASSWORD'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', app.config.get('MAIL_USE_TLS'))
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL', app.config.get('MAIL_USE_SSL'))

mail = Mail(app)


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('home.html', employees=employees,
                           subdivision_employees=subdivision_employees,
                           gallery_images=gallery_images)


@app.route('/gallery')
def gallery():
    return render_template('gallery.html', gallery_all_images=gallery_all_images)


@app.route('/info')
def general_info():
    return render_template('general_info.html')
    # return render_template('general_info.html', general_info_list=general_info_list)


@app.route('/booking')
def booking():
    return render_template('booking.html')


@app.route('/send_email',methods=['POST'])
def send_email():
    if request.method == 'POST':
        specialty = request.form['specialty']
        fullName = request.form['fullName']
        phone = request.form['phone']
        email = request.form['email']
        appointmentDate = request.form['appointmentDate']
        age = request.form['age']
        gender = request.form['gender']
        consent = request.form.get('consent', False)

        # Відправляємо електронний лист
        msg = Message('Запис на прийом', sender=email, recipients=['olgopilcpmsd@ukr.net'])
        msg.body = """
            Деталі запису:
            Спеціальність: {specialty}
            ПІБ пацієнта: {fullName}
            Номер телефону: {phone}
            Електронна пошта: {email}
            Дата та час прийому: {appointmentDate}
            Вік: {age}
            Стать: {gender}
            Згода на обробку персональних даних: {consent}
            """.format(specialty=specialty, fullName=fullName, phone=phone, email=email,
                       appointmentDate=appointmentDate, age=age, gender=gender, consent=consent)

        try:
            mail.send(msg)
            return redirect(url_for('success'))
        except Exception as e:
            return str(e)
            # return redirect(url_for('error_msg'))

    return 'Помилка: неправильний метод запиту'


@app.route('/success')
def success():
    return render_template('partials/success.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
