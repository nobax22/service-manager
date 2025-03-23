import subprocess
import install
import uninstall

def show_menu():
    print("Pilih tindakan yang ingin dilakukan:")
    print("1. Instal Paket")
    print("2. Uninstal Paket")
    print("3. Keluar")
    choice = input("Masukkan pilihan (1, 2, 3): ")
    return choice

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            install_choice = input("Pilih paket untuk diinstal: \n1. Docker\n2. Nginx\n")
            if install_choice == "1":
                install.install_docker()
            elif install_choice == "2":
                install.install_nginx()
            else:
                print("Paket tidak tersedia.")
        
        elif choice == "2":
            uninstall_choice = input("Pilih paket untuk di-uninstal: \n1. Docker\n2. Nginx\n")
            if uninstall_choice == "1":
                uninstall.uninstall_docker()
            elif uninstall_choice == "2":
                uninstall.uninstall_nginx()
            else:
                print("Paket tidak tersedia.")
        
        elif choice == "3":
            print("Keluar dari skrip.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
