from cx_Freeze import setup, Executable

setup(
    name="YourApp",
    version="1.0",
    description="Your description",
    executables=[Executable("free_vbucks.py")]
)