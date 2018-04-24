import os

from flask import Flask, flash, request
from flask.json import jsonify

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)


class ContactForm(FlaskForm):
    email = StringField(validators=[
        validators.Length(min=6, max=35, message='Length of e-mail is incorrect'),
        validators.Email(message='E-mail is not correct'), validators.DataRequired(message='E-mail must be entered')
    ])
    password = PasswordField(validators=[
        validators.Length(min=6),
        validators.InputRequired(), validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField(validators=[
        validators.Length(min=6),
        validators.DataRequired()
    ])

    def flash_errors(self):
        for field, errors in self.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" % (
                    getattr(self, field).label.text,
                    error
                ))


@app.route('/form/user', methods=['POST'])
def home():
        form = ContactForm(request.form)
        status_output = {0: 'Проверка пройдена', 1: 'Ошибка валидации'}
        if form.validate():
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(form.errors)
            return status_check and error_list


@app.route('/locales')
def find_file():
    my_locals = {'ru': 'russian', 'en': 'english'}
    return jsonify(my_locals)


@app.route('/sum/<int:a>,<int:b>')
def summing(a, b):
    return 'Sum: {}'.format(a + b)


@app.route('/greet/<user_name>')
def user(user_name):
    return 'hello user! {}'.format(user_name)


@app.route('/serve/<path:filename>')
def files(filename):
    file_dir = os.path.dirname(__file__)
    try:
        rel_path = 'files/'+filename
        file = os.path.join(file_dir, rel_path)
        with open(file) as f:
            return 'Content of file:\n{}'.format(f.read())
    except FileNotFoundError as e:
        return 'Sorry! {}'.format(e), 404


if __name__ == '__main__':
    app.run()
