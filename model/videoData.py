from google.appengine.ext import ndb


class videoData(ndb.Model):
    hours = ndb.DateTimeProperty(auto_now_add=True)
    video = ndb.StringProperty()
