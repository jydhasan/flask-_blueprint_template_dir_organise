from flask import Blueprint, render_template, request, redirect, url_for, flash
# create a blueprint object
admin_bp = Blueprint('admin', __name__, static_folder='../static',
                     static_url_path='/admin/static', template_folder='../templates')


@admin_bp.route('/admin')
def admin_home():
    return render_template('index.html')
