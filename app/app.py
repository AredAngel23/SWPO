from flask import Flask

# Import from Views
from views.home_views import home_views
from views.user_views import user_views
from views.loan_views import loan_views
from views.error_views import error_views
from views.admin_views import admin_views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'

app.register_blueprint(home_views)
app.register_blueprint(user_views)
app.register_blueprint(loan_views)
app.register_blueprint(error_views)
app.register_blueprint(admin_views)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)