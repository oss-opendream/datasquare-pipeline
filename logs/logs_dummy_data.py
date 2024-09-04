import random
import time
import pytz
from datetime import datetime

def generate_dummy_log():

    # 더미 데이터를 생성할 수 있는 구성 요소들
    method_path_pairs = [
        ("GET", "/profile"),
        ("POST", "/profile"),
        ("GET", "/profile/profile_edit"),
        ("PUT", "/profile/profile_edit"),
        ("GET", "/profile/team"),
        ("POST", "/profile/team"),
        
        ("GET", "/admin"),
        ("GET", "/admin/account/create"),
        ("POST", "/admin/account/create"),
        ("GET", "/admin/teams/set"),
        ("POST", "/admin/teams/set"),
        ("GET", "/admin/teams"),
        ("POST", "/admin/teams/update"),
        ("GET", "/admin/teams/members"),
        
        ("GET", "/data_request/publish"),
        ("POST", "/data_request/publish"),
        ("GET", "/data_request/views"),
        ("GET", "/data_request/edit"),
        ("PUT", "/data_request/edit"),
        ("DELETE", "/data_request/delete"),

        ("GET", "/admin/org"),
        ("POST", "/admin/org"),
        ("GET", "/admin/org/databases"),

        ("GET", "/signin"),
        ("POST", "/signin/post"),
        ("GET", "/signup"),
        ("POST", "/signup"),
        ("GET", "/logout"),

        ("POST", "/issue_comment/create"),
        ("PUT", "/issue_comment/modify"),
        ("DELETE", "/issue_comment/delete"),

        ("GET", "/feed"),
        ("GET", "/feed/my_issues"),
        ("GET", "/feed/search"),

        ("GET", "/databases"),

        ("GET", "/pages/personal.html"),
        ("POST", "/pages/personal_edit.html"),
        ("GET", "/pages/team_profile_view.html"),
        ("GET", "/pages/org.html"),
        ("POST", "/pages/sign_in.html"),
        ("POST", "/pages/sign_up.html"),
        ("GET", "/pages/team_create.html"),
        ("GET", "/pages/feed.html"),
        ("GET", "/pages/data_request.html"),
        ("GET", "/pages/data_request_view.html"),
        ("POST", "/pages/data_request_edit.html"),
    ]

    status_codes = [200, 301, 302, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, \
                     414, 415, 416, 417, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "curl/7.68.0"
    ]
  
    
    tz = pytz.timezone('Asia/Seoul')
    # now = datetime.now(tz)
    # offset = now.strftime('%z')
    # timezone_code = get_timezone_code(offset)


    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    time_stamp = datetime.now(tz).strftime("%d/%b/%Y:%H:%M:%S %z")
    method, path = random.choice(method_path_pairs)
    # method = random.choice(methods)
    # path = random.choice(paths)
    status = random.choice(status_codes)
    bytes_sent = random.randint(200, 5000)
    user_agent = random.choice(user_agents)
    
    log_entry = f'{ip} - - [{time_stamp}] "{method} {path} HTTP/1.1" {status} {bytes_sent} "{user_agent}"'
    
    return log_entry

# 파일 형식으로 저장할 때
# date = datetime.now().strftime("%Y%m%d")
# with open(f"./{date}_logs.txt", 'w') as f:
#     while True:
#         logs =  generate_dummy_log() + '\n'
        
#         f.write(logs)


# test main
if __name__ == "__main__":
    print(generate_dummy_log())