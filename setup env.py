import subprocess
import sys
import os
import venv

# Menentukan nama direktori virtual environment
env_dir = '.venv'

# Membuat virtual environment
def create_virtualenv():
    if not os.path.exists(env_dir):
        print(f'Membuat virtual environment di direktori {env_dir}...')
        venv.create(env_dir, with_pip=True)
    else:
        print(f'Virtual environment sudah ada di {env_dir}, melanjutkan...')

# Mengaktifkan virtual environment
def activate_virtualenv():
    if sys.platform == 'win32':
        activate_script = os.path.join(env_dir, 'Scripts', 'activate.bat')
    else:
        activate_script = os.path.join(env_dir, 'bin', 'activate')
    return activate_script

# Menginstal dependensi dari requirements.txt
def install_requirements():
    print('Menginstal dependensi dari requirements.txt...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def main():
    create_virtualenv()
    install_requirements()
    print(f'Setup selesai. Virtual environment ada di {env_dir}')

if __name__ == '__main__':
    main()
