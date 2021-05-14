import logging.config
import time
from decimal import *
import threading
from os import path
print((path.dirname(path.abspath(__file__))))
logging.config.fileConfig(path.join((path.dirname(path.abspath(__file__))), 'log_setting.conf'))

logger = logging.getLogger(__name__)

def wiki_perf_clock(func):
    def perf_clocked(*args):
        input_value = str()

        # 실행 함수명
        method_name = func.__name__

        # 함수 시작 시간
        start_time = time.perf_counter()
        end_time = Decimal()
        try:
            input_value = str(args) # 들어온 인자값
            result = func(*args) # 함수 종료 시간 계산

            end_time = time.perf_counter() - start_time
        except Exception as e:
            logger.info(f"Exception {e} occured")
            return None
        logger.error(f"{method_name} 메소드, 끝난시간 {end_time} 그리고 {input_value}")
        # log_thread = threading.Thread(target=MRC_PERFORMANCE_LOG, args=(method_name, "success", end_time, input_value, str(result)))
        # log_thread.start()
        return result
    return perf_clocked

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("log genereated")