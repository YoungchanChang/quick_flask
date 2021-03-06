import random, json
from datetime import datetime
from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for, session, Response
from mvc.control import ValidateValue, UserControl, ValueException
from utility import log_time
quick_flask = Blueprint('quick_flask', __name__)

# http://localhost:8080/quick_flask/ping
@quick_flask.route('/ping', methods=['GET', 'POST'])
@log_time.wiki_perf_clock
def ping_pong():
    """간단한 핑테스트 및 request param 분석"""
    IP_ADDR = request.environ.get('HTTP_X_REAL_IP', request.remote_addr) # 실제 요청 ip
    print(IP_ADDR)
    x = request
    print(request.environ.get('REQUEST_URI'))
    print(request.environ.get('PATH_INFO'))
    now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #요청시간
    print(now_time)
    print(request.method)
    return "pong"

# http://localhost:8080/quick_flask/ping-json
@quick_flask.route("/ping-json", methods=['POST'])
def ping_json():
    """json형식의 데이터를 보냈을 때 응답 확인. 간편한 방식과 복잡한 방식. """
    input_json = request.get_json()
    input_json = json.loads(request.get_data().decode('utf-8'))
    return make_response(jsonify(input_json), 200)

# http://localhost:8080/quick_flask/ping_front
@quick_flask.route("/ping_front", methods=['GET'])
def ping_front():
    "프런트 페이지 동작 확인"
    return render_template("front_page.html")

# http://localhost:8080/quick_flask/sign_up
@quick_flask.route('/sign_up', methods=['POST'])
def sign_up():
    """회원가입이 확인 end-point"""
    input_json = request.get_json()  # 아래꺼랑 함께 비교한다.
    input_json = json.loads(request.get_data().decode('utf-8'))
    user_name = input_json.get("user_name") # input, param에 대한 검증 / get으로 하면 여러개 검증하기 힘듬

    svc_name = "/quick_flask_test"
    return_json = {
        "status_code": 500,
        "message": "",
        "model_name": "",
        "sender": ""
    }

    try:
        user_status =  UserControl.is_user_signed(user_name)
        data = {"success" : user_status}

        if data:
            return_json["status_code"] = 200
            return_json["final_answer"] = kakao_answer
            return_json["message"] = "success"
            return_json["model_name"] = "quick_test_model"
            return_json["sender"] = "youngchan"

        # err_log_thread = threading.Thread(target=log.save_server_logs, args=(svc_name, input_json, return_json))
        # err_log_thread.start()
        return make_response(json.dumps(data), 200)

    # 상위 클래스에서
    except ValueException:
        return make_response(jsonify(success=False), 401)

    # 예외 발생된 경우
    except Exception:
        error_msg = traceback.format_exc()
        error_json = {
            "status": {
                "status_code": 500,
                "status_type": "fail",
                "status_msg": error_msg
            }
        }
        # err_log_thread = threading.Thread(target=log.save_server_errors, args=(svc_name, input_json, error_msg))
        # err_log_thread.start()

        # 에러인 경우 중계서버에 에러 메시지 보낸다.
        # return make_response(convert_to_Json_format(error_json), 500)
        return make_response(jsonify(success=False), 401)


# http://localhost:8080/quick_flask/render_page
@quick_flask.route('/render_page', methods=['GET', 'POST'])
def render_page():
    if request.method == 'GET':
        print('set_email', request.args.get('user_email'))
        return redirect(url_for('quick_flask.blog_fullstack1'))
    else:
        return redirect(url_for('quick_flask.sign_up'))

@quick_flask.route('/blog_fullstack1')
def blog_fullstack1():
    """ 랜덤 확률로 A/B 테스트 페이지"""
    rand = random.random()
    if rand > 0.5:
        print("front_page_come")
        return render_template('front_page.html')
    else:
        print("second_page_comes")
        return render_template('front_second_page.html')