import subprocess
import sys
import os

def install_django():
    # Instalacja Django
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'django'])

    # Dodanie Django do zmiennej środowiskowej PATH
    python_path = os.path.dirname(sys.executable)
    scripts_path = os.path.join(python_path, 'Scripts')
    if scripts_path not in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + scripts_path

    # Sprawdzenie, czy Django został poprawnie zainstalowany
    try:
        subprocess.check_call(['django-admin', '--version'])
        print("Django został pomyślnie zainstalowany i skonfigurowany.")
    except subprocess.CalledProcessError:
        print("Wystąpił problem podczas instalacji Django.")

if __name__ == '__main__':
    install_django()
