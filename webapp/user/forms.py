from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    user_name = StringField('Имя пользователя', validators=[DataRequired()], render_kw={'class': 'form_control'})
    remember_me = BooleanField('Запомить меня', default=True, render_kw={"class": "form-check-input"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form_control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    user_name = StringField('Имя пользователя', validators=[DataRequired()], render_kw={'class': 'form_control'})
    email = StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={'class': 'form_control'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={'class': 'form_control'})
    password_2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={'class': 'form_control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
