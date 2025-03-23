import subprocess

def install_docker():
    print("Instalasi Docker...")
    subprocess.run(["sudo", "apt", "install", "docker.io", "-y"])
    subprocess.run(["sudo", "systemctl", "start", "docker"])
    subprocess.run(["sudo", "systemctl", "enable", "docker"])

def install_nginx():
    print("Instalasi Nginx...")
    subprocess.run(["sudo", "apt", "install", "nginx", "-y"])
    subprocess.run(["sudo", "systemctl", "start", "nginx"])
    subprocess.run(["sudo", "systemctl", "enable", "nginx"])

# Fungsi lainnya untuk instalasi paket-paket lainnya
