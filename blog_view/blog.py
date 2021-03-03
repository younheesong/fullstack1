from flask import Flask, render_template, url_for, redirect, Blueprint, request, session
from flask_login import current_user, login_user, logout_user
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
import datetime
blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['POST', 'GET'])
def set_email():
    if request.method== 'GET':
        print("user_email", request.args.get('user_email'))
    else:
        print("user_email", request.form["user_email"])
        print("page_id", request.form["blog_id"])
        user = User.create(user_email = request.form["user_email"], blog_id =request.form["blog_id"])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        return redirect('/blog/blog_fullstack1')

@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.blog_fullstack1'))


@blog_abtest.route('/blog_fullstack1')
def blog_fullstack1():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], "anonymous", webpage_name)
        return render_template(webpage_name)

    
