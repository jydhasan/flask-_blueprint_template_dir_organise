from flask import Flask
from blog.routes import blog_bp
from admin.controllers.admin_route import admin_bp

app = Flask(__name__)
app.register_blueprint(blog_bp)
app.register_blueprint(admin_bp)

# Additional configuration and routes can be added here

if __name__ == '__main__':
    app.run()
