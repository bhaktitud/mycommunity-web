from flask import render_template, request, Blueprint
from mycommunity.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    """Renders the home page."""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template(
        'index.html',
        title='Home Page',
        posts=posts
    )


@main.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact us',
        message='Contact us.'
    )


@main.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        message='Description.'
    )
