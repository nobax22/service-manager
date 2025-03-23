/your_project_directory
│
├── manage_services.py # Skrip utama untuk memilih tindakan (antarmuka pengguna)
├── install.py # Skrip untuk instalasi layanan
├── uninstall.py # Skrip untuk uninstalasi layanan
├── requirements.txt # (Opsional) Daftar dependensi yang diperlukan
└── other_files/ # (Opsional) File tambahan (misalnya konfigurasi, log, dll)

# Service Manager Script

This script allows you to install, manage, and uninstall various services such as Docker, PHP, MySQL, and more on your system.

## Prerequisites

- Python 3.x
- Sudo privileges for installing some services

## Installation

1. Clone or download this repository.
2. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   Usage
   To run the script, use the following command:
   python manage_services.py
   Follow the interactive menu to install or uninstall services.
   ```
