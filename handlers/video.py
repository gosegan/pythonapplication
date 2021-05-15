import time

import webapp2
from google.appengine.ext import ndb
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.commentData import commentData
from model.videoData import videoData


class VideoHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if usr:
            login_logout_url = users.create_logout_url("/")
        else:
            login_logout_url = users.create_login_url("/")

        str_key = self.request.GET["id"]
        key = ndb.Key(urlsafe=str_key)
        item = key.get()

        list_data = commentData.query(commentData.video_key == item.key).order(-commentData.hours)

        object = {
            "login_logout_url": login_logout_url,
            "usr": usr,
            'list_data': list_data,
            "item": item
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("video.html", **object))

    def post(self):
        comment = self.request.get("text", "anonymous")
        grade = self.request.get('active')
        usr = users.get_current_user()
        str_key = self.request.GET["id"]
        key = ndb.Key(urlsafe=str_key)
        video = key.get()

        if usr:
            nick = usr.nickname()
            # nick = usr.email()
            # nick = usr.user_id()
            # users.is_current_user_admin()

        # Guarder eco
        comment_data = commentData(text=comment, author=nick, rate=grade, video_key=video.key)
        comment_data.put()

        # video_data = videoData(video=vid)
        # video_data.put()

        time.sleep(0.1)

        # Recuparar todos los ecos
        list_data = commentData.query(commentData.video_key == video.key).order(-commentData.hours)

        str_key = self.request.GET["id"]
        key = ndb.Key(urlsafe=str_key)
        item = key.get()

        # Preparar pantilla
        jinja = jinja2.get_jinja2(app=self.app)
        data = {
            "usr": usr,
            'list_data': list_data,
            "item": item
        }
        self.response.write(
            jinja.render_template("video.html", **data)
        )


app = webapp2.WSGIApplication([
    ('/video', VideoHandler)
], debug=True)
