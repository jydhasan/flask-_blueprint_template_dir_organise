from flask import render_template
from flask import Blueprint
blog_bp = Blueprint('blog', __name__, static_folder='static',
                    static_url_path='/blog/static', template_folder='templates')


@blog_bp.route('/blog')
def blog_home():
    return render_template('blog_home.html')
