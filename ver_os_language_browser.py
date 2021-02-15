import subprocess

subprocess.run('uname -a', shell=True)
subprocess.run('python3 --version', shell=True)
subprocess.run('pip3 freeze | grep selenium',shell=True)
subprocess.run('google-chrome --version', shell=True)
subprocess.run('firefox --version', shell=True)
subprocess.run('opera --version', shell=True)

