import subprocess
import time
import random

while True:
	randnumb = random.randint(1, 1000)
	if randnumb == 7:
		subprocess.run("rick.bat", shell=True)
	time.sleep(1)