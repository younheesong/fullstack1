from db_model.mongodb import conn_mongodb
from datetime import datetime

class BlogSession():
    blog_page = {'A': 'page_A.html', 'B':'page_B.html'}
    session_count = 0

    @staticmethod 
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime("%d/%m/%Y %H:%M:%S")

        mongodb = conn_mongodb()
        mongodb.insert_one({
            'session_ip' : session_ip,
            'user_email' : user_email,
            'page' : webpage_name,
            'access_time' : now_time
        })

    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id:
            return BlogSession.blog_page[blog_id]
        else:
            if BlogSession.session_count ==0:
                BlogSession.session_count =1
                return 'page_A.html'
            else:
                BlogSession.session_count = 0
                return 'page_B.html'
            

