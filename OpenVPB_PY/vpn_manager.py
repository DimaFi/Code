import psutil
import subprocess
import time

# Замените на ваши параметры
VPN_GATEWAY = "45.15.157.228:1080"
TARGET_PROCESSES = ['Discord.exe', 'chrome.exe', 'obs.exe']  # Имена процессов

# Функция для получения IP-адресов активных процессов
def get_process_ips(process_name):
    process_ips = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            try:
                # Получаем соединения для процесса
                for conn in proc.connections(kind='inet'):
                    ip = conn.raddr[0]
                    process_ips.append(ip)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    return process_ips

# Функция для добавления маршрута
def add_route(ip):
    subprocess.call(['route', 'add', ip, 'mask', '255.255.255.255', VPN_GATEWAY])

# Функция для удаления маршрута
def delete_route(ip):
    subprocess.call(['route', 'delete', ip])

# Основной цикл
if __name__ == "main":
    existing_ips = set()

    while True:
        current_ips = set()
        for process in TARGET_PROCESSES:
            ips = get_process_ips(process)
            current_ips.update(ips)

        # Добавляем новые маршруты и удаляем старые
        for ip in current_ips:
            if ip not in existing_ips:
                print(f"Добавление маршрута для {ip}")
                add_route(ip)
                existing_ips.add(ip)

        for ip in list(existing_ips):
            if ip not in current_ips:
                print(f"Удаление маршрута для {ip}")
                delete_route(ip)
                existing_ips.remove(ip)

        time.sleep(5)  # Проверять каждые 5 секунд