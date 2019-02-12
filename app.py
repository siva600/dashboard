from flask import Flask
from db_query import prod_history
from flask import render_template, url_for, flash, redirect, request, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

#
# # defining route pages for the site, using routes.
# @app.route('/')
# def home():
#     posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)
#     return render_template('home.html', posts=posts)
#


@app.route('/dashboard')
def dashboard():
    results = prod_history()
    return render_template('dashboard.html', title="display name", date=JOBDATE,
                           s_name= SERVICE_NAME, artifact=ARTIFACT, posts=results)


if __name__ == '__main__':
    app.run()
