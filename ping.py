import traceback
import os
from ping3 import ping, verbose_ping

# 将异常信息写入日志文件并转换为可支持的编码
def log_exception(e):
    with open('ping_exe_error_log.txt', 'a', encoding='utf-8') as f:
        f.write(f"Exception occurred: {e}\n")
        traceback.print_exc(file=f)

# 主程序
if __name__ == '__main__':
    try:
        # 让用户输入要ping的IP地址和范围
        start_ip_str = input("请输入要ping的起始IP地址（例如：192.168.1.1）：")
        end_ip_str = input("请输入要ping的结束IP地址（例如：192.168.1.30）：")

        # 将输入的IP地址转换为整数
        start_ip = int(start_ip_str.split('.')[-1])
        end_ip = int(end_ip_str.split('.')[-1])

        # 循環 Ping 每個 IP 地址
        for i in range(start_ip, end_ip + 1):
            ip = f"{start_ip_str.rsplit('.', 1)[0]}.{i}"
            print(f"Pinging {ip}...")
            
            # 执行 ping 命令
            try:
                response_time = ping(ip, timeout=2)
                if response_time is not None:
                    print(f"{ip} Ping Success, Response Time: {response_time:.2f} ms")
                else:
                    print(f"{ip} Ping Fail")
                    log_exception(f"{ip} Ping Fail")
            except Exception as e:
                log_exception(e)

            # 添加延迟，以便观察结果
            import time
            time.sleep(1)
    except Exception as e:
        log_exception(e)
