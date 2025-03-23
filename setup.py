from setuptools import setup, find_packages

setup(
    name="service-manager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyyaml",
        # Tambahkan dependensi lain di sini
    ],
    entry_points={
        "console_scripts": [
            "manage-services=manage_services:main",  # Gantilah sesuai dengan nama fungsi utama kamu
        ],
    },
    include_package_data=True,
    description="A script to manage services like Docker, PHP, MySQL, etc.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Your Name",
    author_email="your.email@example.com",
    url="https://your-project-url",
)
