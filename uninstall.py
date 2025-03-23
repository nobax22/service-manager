import subprocess

def uninstall_docker():
    print("Uninstal Docker...")
    subprocess.run(["sudo", "apt", "remove", "docker.io", "-y"])
    subprocess.run(["sudo", "apt", "autoremove", "-y"])

def uninstall_nginx():
    print("Uninstal Nginx...")
    subprocess.run(["sudo", "apt", "remove", "nginx", "-y"])
    subprocess.run(["sudo", "apt", "autoremove", "-y"])

# Fungsi lainnya untuk uninstalasi paket-paket lainnya
