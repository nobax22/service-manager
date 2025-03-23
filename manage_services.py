import install
import uninstall

def show_menu():
    print("\n=====================")
    print("   Manage Services   ")
    print("=====================")
    print("1. Instal Paket")
    print("2. Uninstal Paket")
    print("3. Keluar")
    choice = input("Masukkan pilihan (1, 2, 3): ")
    return choice

def install_menu():
    print("\nPilih paket yang ingin diinstal:")
    print("1. Docker")
    print("2. Nginx")
    print("3. Git")
    print("4. PHP")
    print("5. Node.js")
    print("6. Kembali")
    choice = input("Masukkan pilihan (1-6): ")
    return choice

def uninstall_menu():
    print("\nPilih paket yang ingin di-uninstal:")
    print("1. Docker")
    print("2. Nginx")
    print("3. Git")
    print("4. PHP")
    print("5. Node.js")
    print("6. Kembali")
    choice = input("Masukkan pilihan (1-6): ")
    return choice

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            # Instalasi
            while True:
                install_choice = install_menu()
                if install_choice == "1":
                    install.install_docker()
                elif install_choice == "2":
                    install.install_nginx()
                elif install_choice == "3":
                    install.install_git()
                elif install_choice == "4":
                    install.install_php()
                elif install_choice == "5":
                    install.install_nodejs()
                elif install_choice == "6":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif choice == "2":
            # Uninstalasi
            while True:
                uninstall_choice = uninstall_menu()
                if uninstall_choice == "1":
                    uninstall.uninstall_docker()
                elif uninstall_choice == "2":
                    uninstall.uninstall_nginx()
                elif uninstall_choice == "3":
                    uninstall.uninstall_git()
                elif uninstall_choice == "4":
                    uninstall.uninstall_php()
                elif uninstall_choice == "5":
                    uninstall.uninstall_nodejs()
                elif uninstall_choice == "6":
                    break
                else:
                    print("Pilihan tidak valid.")
        
        elif choice == "3":
            print("Keluar dari manajer layanan.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
