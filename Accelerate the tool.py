import os
import socket
import platform

print("仅支持部分网站")

def get_hosts_file_path():
    system = platform.system()
    if system == "Linux" or system == "Darwin":
        return "/etc/hosts"
    elif system == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    else:
        raise Exception("Unsupported operating system.")

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception as e:
        print(f"获取 {domain} 的 IP 地址失败：{str(e)}")
        return None

def add_ip_to_hosts(ip_address, domain):
    try:
        hosts_file_path = get_hosts_file_path()
        with open(hosts_file_path, 'r', encoding='utf-8') as hosts_file:  # 指定编码方式为 UTF-8
            lines = hosts_file.readlines()
        with open(hosts_file_path, 'w', encoding='utf-8') as hosts_file:  # 指定编码方式为 UTF-8
            for line in lines:
                if not (line.strip().startswith(ip_address) and line.strip().endswith(domain)):
                    hosts_file.write(line)
            hosts_file.write(f"{ip_address}\t{domain}\n")
        print(f"IP 地址 {ip_address} 已添加到 hosts 文件中。")
    except Exception as e:
        print(f"添加 IP 地址到 hosts 文件失败：{str(e)}")

# 示例按钮点击事件
def button_click_event(choice):
    if choice == "1":
        domains = ["github.com", "github.io", "api.github.com", "gist.github.com"]  # 设置要加速的 GitHub 域名列表
    elif choice == "2":
        domains = ["microsoft.com", "learn.microsoft.com"]  # 设置要加速的 Microsoft 域名列表
    elif choice == "3":
        domains = ["discord.com", "discordapp.com"]  # 设置要加速的 Discord 域名列表
    else:
        print("无效的选项，请重新输入。")
        return
    
    for domain in domains:
        ip_address = get_ip_address(domain)  # 获取对应域名的 IP 地址
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

# 菜单界面
while True:
    print("请选择操作：")
    print("1. GitHub 加速")
    print("2. Microsoft 加速")
    print("3. Discord 加速")
    print("4. 退出")
    choice = input("请输入选项: ")
    
    if choice == "4":
        break
    else:
        button_click_event(choice)
