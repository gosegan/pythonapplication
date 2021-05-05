import time

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.commentData import commentData, videoData


class MainHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if usr:
            login_logout_url = users.create_logout_url("/")
        else:
            login_logout_url = users.create_login_url("/")

        list_data = commentData.query().order(-commentData.hours)
        object = {
            "login_logout_url": login_logout_url,
            "usr": usr,
            'list_data': list_data
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("index.html", **object))

    def post(self):
        comment = self.request.get("text", "anonymous")
        grade = self.request.get('active')
        usr = users.get_current_user()
        vid = 'eU8h3CjhFjs'

        if usr:
            nick = usr.nickname()
            # nick = usr.email()
            # nick = usr.user_id()
            # users.is_current_user_admin()

        # Guarder eco
        comment_data = commentData(text=comment, author=nick, rate=grade)
        comment_data.put()

        # video_data = videoData(video=vid)
        time.sleep(0.1)

        # Recuparar todos los ecos
        list_data = commentData.query().order(-commentData.hours)
        # list_video = videoData.query()

        # Preparar pantilla
        jinja = jinja2.get_jinja2(app=self.app)
        data = {
            "usr": usr,
            'list_data': list_data
            # 'list_video': list_video
        }
        self.response.write(
            jinja.render_template("index.html", **data)
        )


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
