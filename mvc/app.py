from flask import Flask, jsonify, request, render_template, make_response, session
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
from mvc import view
import os

# https 만을 지원하는 기능을 http 에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def create_app(test_config = None):
    app = Flask(__name__)
    app.register_blueprint(view.quick_flask, url_prefix='/quick_flask')

    @app.errorhandler(404)  # 없는 페이지를 요청했을 때의 에러
    def page_not_found(error):
        return "<h1>404 Error</h1>", 404
    return  app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port='8080')