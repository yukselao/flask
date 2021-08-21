from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

index_bp=Blueprint('index_bp', __name__,
    template_folder='templates',
    static_folder='static')

@index_bp.route('/', defaults={'page': 'index'})
@index_bp.route('/<page>')
def show(page):
    try:
        return render_template(f'index/{page}.html')
    except TemplateNotFound:
        abort(404)

