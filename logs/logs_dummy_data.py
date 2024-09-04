import random
import time
from datetime import datetime

def generate_dummy_log():

    # 더미 데이터를 생성할 수 있는 구성 요소들
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    paths = ["/", "/index.html", "/about", "/contact", "/products", "/api/v1/item"]
    status_codes = [200, 301, 302, 404, 500]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "curl/7.68.0"
    ]

    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    time_stamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S %z")
    method = random.choice(methods)
    path = random.choice(paths)
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
