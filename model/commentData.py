from google.appengine.ext import ndb


class commentData(ndb.Model):
    hours = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty(required=True)
    author = ndb.StringProperty()
    rate = ndb.StringProperty()
