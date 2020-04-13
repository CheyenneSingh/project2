"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm,ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from flask_bootstrap import Bootstrap
from flask_wtf.file import *
from werkzeug.utils import secure_filename

# from flask.ext.uploads import UploadSet, IMAGES
# from flask.ext.sqlalchemy import SQLAlchemy
from app.models import UserProfile
from datetime import *

bootstrap = Bootstrap(app)

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = ProfileForm()
    # if current_user.is_authenticated:
    #     # if user is already logged in, just redirect them to our secure page
    #     # or some other page like a dashboard
    #     return redirect(url_for('secure_page'))

    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    if request.method == 'POST' and form.validate_on_submit():
        firstName = form.fname.data
        lastName = form.lname.data
        email = form.email.data
        location = form.location.data
        sex = form.sex.data
        bio = form.bio.data
        if form.photo.data:
            #filename = secure_filename(form.fle.data.filename)
            #form.fle.data.save('uploads/' + filename)
            im = request.files['photo']
            im_fn = form.fname.data + '_' + secure_filename(im.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], im_fn)
            im.save(file_path)
        user = UserProfile.query.filter_by(email=email).first()
        #if user is not None and check_password_hash(user.password, password):
        if user is None:
            profile=UserProfile(firstName, lastName, location,email,sex,bio, datetime.now(),im_fn)
            db.session.add(profile)
            db.session.commit()
        return redirect(url_for('showProfiles'))
    flash_errors(form)
    return render_template('form.html', form=form)


@app.route('/profile/<id>')
def  showSingleProfile(id):
    profile = UserProfile.query.filter_by(id=id).first()
    imgURL = url_for('static', filename='img/uploads/'+profile.img)
    user = {'id':profile.id,'fname':profile.first_name,'image':imgURL,'lname':profile.last_name, 'location':profile.location,'sex':profile.sex,'bio':profile.bio, 'email':profile.email}
    return render_template('viewProfile.html', user=user,datestring=profile.added.strftime("%a, %d %b, %Y"))



@app.route('/profiles', methods=['GET', 'POST'])
def showProfiles():
    users = db.session.query(UserProfile).all()
    file_path = os.path.join(app.config['UPLOAD_FOLDER'])
    print(users)
    return render_template('profiles.html', users=users,file_path=file_path)



# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
