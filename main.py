from flask import Flask
from flask import render_template
from data import db_session
from data.news import News
from data.users import User
from forms.user import RegisterForm
import os


# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
#
#
# def main():
#     db_session.global_init("db/blogs.db")
#     app.run()
    # user = User()
    # user.name = "Пользователь 1"
    # user.about = "биография пользователя 1"
    # user.email = "email1@email.ru"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    # user = User()
    # user.name = "Пользователь 2"
    # user.about = "биография пользователя 2"
    # user.email = "email2@email.ru"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    # user = User()
    # user.name = "Пользователь 3"
    # user.about = "биография пользователя 3"
    # user.email = "email3@email.ru"
    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.commit()
    # db_sess = db_session.create_session()
    # news = News(title="Первая новость", content="Привет блог!",
    #             user_id=1, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title="Вторая новость", content="Уже вторая запись!",
    #             user=user, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title="Личная запись", content="Эта запись личная",
    #             is_private=True)
    # user.news.append(news)
    # db_sess.commit()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # for news in user.news:
    #     print(news)

#
# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     news = db_sess.query(News).filter(News.is_private != True)
#     return render_template("index.html", news=news)
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def reqister():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         if form.password.data != form.password_again.data:
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Пароли не совпадают")
#         db_sess = db_session.create_session()
#         if db_sess.query(User).filter(User.email == form.email.data).first():
#             return render_template('register.html', title='Регистрация',
#                                    form=form,
#                                    message="Такой пользователь уже есть")
#         user = User(
#             name=form.name.data,
#             email=form.email.data,
#             about=form.about.data
#         )
#         user.set_password(form.password.data)
#         db_sess.add(user)
#         db_sess.commit()
#         return redirect('/login')
#     return render_template('register.html', title='Регистрация', form=form)
#
#
# if __name__ == '__main__':
#     app.run()


import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
