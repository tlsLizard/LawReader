minimum_python_version = '3.8'
minimum_glibc_version = '2.28'

import platform
import re


def check_python_version(minimum_version):
    current_version = platform.python_version()
    return current_version >= minimum_version


def check_glibc_version(minimum_version):
    current_version = platform.libc_ver()[1]
    current_version = re.findall(r'\d+\.\d+', current_version)[0]
    return current_version >= minimum_version


def check_env():
    status = False
    if check_python_version(minimum_python_version) and check_glibc_version(minimum_glibc_version):
        status = True
    else:
        print("unmet requirements:")
        print(f"Python {minimum_python_version}")
        print(f"glibc {minimum_glibc_version}")
    return status


"""OLD
import sys
import subprocess


def check_pyside6():
    try:
        import PySide6
        print("PySide6 is installed.")
    except ImportError:
        print("PySide6 is not installed.")

def check_python_version():
    print(f"Current Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print(f"Minimum Python version to run gui app: {minimum_python_version}")

def check_glibc_version():
    try:
        output = subprocess.check_output('ldd --version', shell=True).decode('utf-8')
        version_line = output.split("\n")[0]
        glibc_version = version_line.split(" ")[-1]
        print(f"GLIBC version: {glibc_version}")
    except Exception as e:
        print(f"Failed to get GLIBC version: {str(e)}")
    finally:
        print(f"minimum_glibc_version: {minimum_glibc_version}")

def check_env():
    check_python_version()
    check_glibc_version()
    #check_pyside6()
"""


