import os
import socket
import platform

try:
    import tldextract
except ImportError:
    print("未找到依赖库 tldextract，正在尝试安装...")
    os.system("pip install tldextract")
    import tldextract

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
        with open(hosts_file_path, 'r', encoding='utf-8') as hosts_file:
            lines = hosts_file.readlines()
        with open(hosts_file_path, 'w', encoding='utf-8') as hosts_file:
            for line in lines:
                if not (line.strip().startswith(ip_address) and line.strip().endswith(domain)):
                    hosts_file.write(line)
            hosts_file.write(f"{ip_address}\t{domain}\n")
        print(f"IP 地址 {ip_address} 已添加到 hosts 文件中。")
    except Exception as e:
        print(f"添加 IP 地址到 hosts 文件失败：{str(e)}")

def get_subdomains(domain):
    try:
        ext = tldextract.extract(domain)
        suffix = f"{ext.domain}.{ext.suffix}"
        ip_address = get_ip_address(suffix)
        if ip_address:
            subdomains = []
            for i in range(256):
                subdomain = f"sub{i}.{suffix}"
                subdomain_ip_address = get_ip_address(subdomain)
                if subdomain_ip_address and subdomain_ip_address != ip_address:
                    subdomains.append(subdomain)
            return subdomains
    except Exception as e:
        print(f"获取 {domain} 的子域名失败：{str(e)}")
        return []

def add_subdomains_to_hosts(domain):
    subdomains = get_subdomains(domain)
    for subdomain in subdomains:
        ip_address = get_ip_address(subdomain)
        if ip_address:
            add_ip_to_hosts(ip_address, subdomain)

def speed_up_pip():
    domains = ["pypi.org", "files.pythonhosted.org"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_git():
    domains = ["github.com", "github.io", "api.github.com", "gist.github.com", "gitlab.com"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_microsoft():
    domains = ["microsoft.com", "learn.microsoft.com"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_discord():
    domains = ["discord.com", "discordapp.com"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_outlook():
    domains = ["outlook.com", "office.com"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_bilibili():
    domains = ["bilibili.com", "www.bilibili.com"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_huggingface():
    domains = ["huggingface.co", "cdn.huggingface.co", "s3.amazonaws.com"]
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def speed_up_custom_domain():
    domain = input("请输入要加速的域名: ")
    ip_address = get_ip_address(domain)
    if ip_address:
        add_ip_to_hosts(ip_address, domain)
        add_subdomains_to_hosts(domain)

def speed_up_custom_website():
    domains = ["www.google.com", "news.google.com.hk", "bilibili.tv", "example.com", "www.example.com", "www.wikipedia.org", "www.reddit.com", "www.amazon.com", "www.youtube.com","www.netflix.com", "www.airbnb.com", "www.stackoverflow.com"]
    # 替换为你要加速的网站域名列表
    for domain in domains:
        ip_address = get_ip_address(domain)
        if ip_address:
            add_ip_to_hosts(ip_address, domain)

def clean_hosts_file():
    try:
        hosts_file_path = get_hosts_file_path()
        with open(hosts_file_path, 'w', encoding='utf-8') as hosts_file:
            hosts_file.write("")
        print("hosts文件已清空。")
    except Exception as e:
        print(f"清空hosts文件失败：{str(e)}")

def button_click_event(choice):
    if choice == "1":
        speed_up_git()
    elif choice == "2":
        speed_up_pip()
    elif choice == "3":
        speed_up_microsoft()
    elif choice == "4":
        speed_up_discord()
    elif choice == "5":
        speed_up_outlook()
    elif choice == "6":
        speed_up_custom_domain()
    elif choice == "7":
        clean_hosts_file()
    elif choice == "8":
        speed_up_bilibili()
    elif choice == "9":
        speed_up_huggingface()
    elif choice == "10":
        speed_up_custom_website()
    else:
        print("无效的选项，请重新输入。")

while True:
    print("请选择操作：")
    print("1. Git 加速")
    print("2. Pip 加速")
    print("3. Microsoft 加速")
    print("4. Discord 加速")
    print("5. Outlook 加速")
    print("6. 其他域名加速(无法正确获取二级域名)")
    print("7. 清理 hosts 文件")
    print("8. 哔哩哔哩加速")
    print("9. Hugging Face 加速")
    print("10. 更多网站加速")
    choice = input("请输入选项: ")
    
    button_click_event(choice)
