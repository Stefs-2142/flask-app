from flask import Flask
from flask import render_template

from flask_login import LoginManager, login_required
from flask_login import current_user

from webapp.model import db, News
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.weather import weather_by_city


def create_app():

    app = Flask(__name__)
    app.debug = True
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)







    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Hi Admin'
        else:
            return 'Ты не админ!'
    return app
