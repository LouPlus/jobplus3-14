from flask import Flask, render_template, redirect, url_for, make_response, request

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'a random string'
    })

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello World!, {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
    resp = make_response(render_template('user_index.html', username=username))
    resp.set_cookie('username', username)
    return resp

if __name__ == '__main__':
    app.run()
    
