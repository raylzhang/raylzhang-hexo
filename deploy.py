import paramiko
import os
import datetime
import subprocess
import argparse

'''############################# 解析参数 #############################'''
# 创建参数解析器
parser = argparse.ArgumentParser(description='Description of your script')

# 添加需要的命令行参数
# parser.add_argument('-s', '--server', help='Remote server hostname or IP address')
# parser.add_argument('-p', '--port', type=int, help='SSH port')
# parser.add_argument('-u', '--username', help='SSH username')
# parser.add_argument('-k', '--key', help='Path to private key')
# parser.add_argument('-r', '--remote-folder', help='Path to remote folder')
# parser.add_argument('-l', '--local-folder', help='Path to local folder')
parser.add_argument("-b", "--backup", help="Does backup remote folder or not")

# 解析命令行参数
args = parser.parse_args()

# 读取参数值
# server = args.server
# port = args.port
# username = args.username
# private_key_path = args.key
# remote_folder = args.remote_folder
# local_folder = args.local_folder
is_backup = True if args.backup == "true" else False

# 远程服务器
host = "ray"
port = 22
username = "root"
password = ""
# private_key_path = "/Users/raylzhang/.ssh/id_rsa" # 私钥路径

# 远程文件和本地文件
remote_folder = "/docker/nginx/data/hexo"
local_folder = "/Users/raylzhang/prj-ray/raylzhang-hexo/public"

# 创建SSH客户端
client = paramiko.SSHClient()

try:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机

    # 使用私钥认证连接远程服务器
    # private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    # client.connect(hostname=host, port=port, username=username, pkey=private_key)
    client.connect(hostname=host, port=port, username=username, password=password)

    '''############################# 生成静态文件 #############################'''
    os.chdir(os.path.dirname(local_folder))  # 进入 local_folder 上一级目录
    # 运行 hexo generate 命令
    """
    shell：是否使用 shell 解释器来执行命令，默认为 False
    capture_output：是否捕获标准输出和标准错误流，默认为 False
    text：是否将输出流转换为文本字符串，默认为 False。
    """
    result = subprocess.run("hexo generate", shell=True, capture_output=True, text=True)
    if result.returncode == 0:  # returncode 为 0 表示执行成功, 1 表示执行失败
        print("Hexo generated 成功，准备上传文件...")
    else:
        print("Hexo generated 失败，退出！")
        exit(1)

    '''############################# 备份远程文件 #############################'''
    if is_backup:
        """检查远程文件夹是否存在
        stdin 标准输入
        stdout 标准输出
        stderr 标准错误 """
        stdin, stdout, stderr = client.exec_command(f"ls {remote_folder}")  # 在字符串前面加上f，表示在字符串中可以使用大括号{}来插入变量
        if stdout.channel.recv_exit_status() == 0:  # 0 表示执行成功
            print(f"远程 {remote_folder} 存在，开始备份...")
            now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")  # 20230614211516
            backup_folder = f"{remote_folder}_{now}"
            stdin, stdout, stderr = client.exec_command(f"mv {remote_folder} {backup_folder}")
            print(f"备份成功，地址：{backup_folder}，开始上传本地文件夹...")
        else:
            print(f"远程 {remote_folder} 不存在，直接上传本地文件夹...")
    else:
        stdin, stdout, stderr = client.exec_command(f"rm -rf {remote_folder}")
        print(f"远程 {remote_folder} 删除成功，开始上传本地文件夹...")

    '''############################# 上传本地文件 #############################'''
    cmd = f"scp -r {local_folder} {username}@{host}:{remote_folder}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print("上传成功！")
    else:
        print("上传失败，退出！")
        exit(1)
except paramiko.AuthenticationException:
    print("SSH认证失败，请检查密钥和认证配置！")
except paramiko.SSHException as e:
    print(f"SSH连接失败：{str(e)}")
except Exception as e:
    print(f"发生异常：{str(e)}")
finally:
    client.close()
