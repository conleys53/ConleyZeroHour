from cx_Freeze import setup, Executable

# NO GUI
executables = [
    Executable(
        "main.py",
        base="Win32GUI",
        target_name="ConleyZeroHour.exe"
    )
]

# dependencies
build_exe_options = {
    "packages": ["requests", "json", "platform", "os", "subprocess", "plyer", "win10toast_click"],
    "include_files": ["api.txt", "notified_vulnerabilities.json"],
    "excludes": ["tkinter"]
}

setup(
    name="ConleyZeroHour",
    version="1.0",
    description="AI-powered Windows Security Alert System",
    options={"build_exe": build_exe_options},
    executables=executables
)
