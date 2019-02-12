from flask import render_template, url_for, flash, redirect, request, abort
from datetime import datetime
import os
from db_query import prod_history

#
# # defining route pages for the site, using routes.
# @app.route('/')
# def home():
#     posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=1)
#     return render_template('home.html', posts=posts)
#
#
#
# @app.route('/dashboard')
# def dashboard():
#     results = prod_history()
#     posts= results.query.order_by(Post.date_posted.desc())
#     return render_template('dashboard.html', title="display name", post=user, user_posts= user_posts, posts=posts)
