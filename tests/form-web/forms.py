from flask.ext.wtf import Form
from wtforms import StringField,TextField, BooleanField
#from flask.ext.wtf import Required
from wtforms.validators import DataRequired,Required

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)