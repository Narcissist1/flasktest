from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

#
# @app.route('/login', methods=['POST','GET'])
# def login():
#     error = None
#     if request.method=='POST':
#         if valid_login


if __name__ == '__main__':
    app.run(debug=True)
