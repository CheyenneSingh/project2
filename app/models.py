from . import db
from werkzeug.security import generate_password_hash

class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.String(80))
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    user_name =db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    bio = db.Column(db.String(300))
    pic = db.Column(db.String(255))

    def __init__(self, first_name, last_name, user_name, email, location, gender, bio, created, pic):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.location = location
        self.gender = gender
        self.bio = bio
        self.created = created
        self.pic = pic
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

class UserPost(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_posts'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80))
    pic = db.Column(db.String(255))
    desc = db.Column(db.String(300))
    likes = db.Column(db.String(80))
    created = db.Column(db.String(80))

    def __init__(self, user_name, pic, desc, likes, created):
        self.user_name = user_name
        self.pic = pic
        self.desc = desc
        self.likes = likes
        self.created = created
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Post %r>' % (self.username)

