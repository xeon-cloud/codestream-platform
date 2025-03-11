from flask import Flask, render_template
import oauth.config as cf

app = Flask(__name__)

@app.route('/auth')
def auth():
    return render_template('auth.html', ya_client_id=cf.YA_CLIENT_ID)

@app.route('/register')
def register():
    return render_template('reg.html', ya_client_id=cf.YA_CLIENT_ID)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)