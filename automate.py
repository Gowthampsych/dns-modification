import os
import ctypes
from ctypes import wintypes
import sys
import time

# Define constants
SEE_MASK_NOCLOSEPROCESS = 0x00000040
SEE_MASK_FLAG_NO_UI = 0x00000400
SW_SHOWNORMAL = 1

class ShellExecuteInfo(ctypes.Structure):
    _fields_ = [("cbSize", wintypes.DWORD),
                ("fMask", wintypes.ULONG),
                ("hwnd", wintypes.HANDLE),
                ("lpVerb", ctypes.c_wchar_p),
                ("lpFile", ctypes.c_wchar_p),
                ("lpParameters", ctypes.c_wchar_p),
                ("lpDirectory", ctypes.c_wchar_p),
                ("nShow", wintypes.INT),
                ("hInstApp", wintypes.HANDLE),
                ("lpIDList", wintypes.LPVOID),
                ("lpClass", ctypes.c_wchar_p),
                ("hkeyClass", wintypes.HANDLE),
                ("dwHotKey", wintypes.DWORD),
                ("hIcon", wintypes.HANDLE),
                ("hProcess", wintypes.HANDLE)]

def execute_as_admin(path):
    sei = ShellExecuteInfo()
    sei.cbSize = ctypes.sizeof(sei)
    sei.fMask = SEE_MASK_NOCLOSEPROCESS | SEE_MASK_FLAG_NO_UI
    sei.lpVerb = "runas"
    sei.lpFile = sys.executable
    sei.lpParameters = path
    sei.nShow = SW_SHOWNORMAL

    # Execute as admin
    ctypes.windll.shell32.ShellExecuteExW(ctypes.byref(sei))
    return sei.hProcess

def main():
    # Step 1: Execute attack.py
    print("Executing attack.py...")
    attack_process = execute_as_admin("attack.py")
    ctypes.windll.kernel32.WaitForSingleObject(attack_process)
    
    # Step 2: Wait for 3 seconds
    time.sleep(3)
    
    # Step 3: Execute sniff.py
    print("Executing sniff.py...")
    sniff_process = execute_as_admin("sniff.py")
    ctypes.windll.kernel32.WaitForSingleObject(sniff_process, -1)

    # Step 4: Execute uploadcsv.py
    print("Executing uploadcsv.py...")
    uploadcsv_process = execute_as_admin("uploadcsv.py")
    ctypes.windll.kernel32.WaitForSingleObject(uploadcsv_process, -1)

    # Step 5: Execute downloadcsv.py
    print("Executing downloadcsv.py...")
    downloadcsv_process = execute_as_admin("downloadcsv.py")
    ctypes.windll.kernel32.WaitForSingleObject(downloadcsv_process, -1)

    # Step 6: Execute DnsModule.py
    print("Executing DnsModule.py...")
    dnsmodule_process = execute_as_admin("DnsModule.py")
    ctypes.windll.kernel32.WaitForSingleObject(dnsmodule_process, -1)

    # Step 7: Execute attack2.py
    print("Executing attack2.py...")
    attack2_process = execute_as_admin("attack2.py")
    ctypes.windll.kernel32.WaitForSingleObject(attack2_process)
    
    # Step 8: Execute sniff.py again
    print("Executing sniff.py again...")
    sniff_process = execute_as_admin("sniff.py")
    ctypes.windll.kernel32.WaitForSingleObject(sniff_process, -1)

if __name__ == "__main__":
    main()





# import os
# import ctypes
# from ctypes import wintypes
# import sys
# import time

# # Define constants
# SEE_MASK_NOCLOSEPROCESS = 0x00000040
# SEE_MASK_FLAG_NO_UI = 0x00000400
# SW_SHOWNORMAL = 1

# class ShellExecuteInfo(ctypes.Structure):
#     _fields_ = [("cbSize", wintypes.DWORD),
#                 ("fMask", wintypes.ULONG),
#                 ("hwnd", wintypes.HANDLE),
#                 ("lpVerb", ctypes.c_wchar_p),
#                 ("lpFile", ctypes.c_wchar_p),
#                 ("lpParameters", ctypes.c_wchar_p),
#                 ("lpDirectory", ctypes.c_wchar_p),
#                 ("nShow", wintypes.INT),
#                 ("hInstApp", wintypes.HANDLE),
#                 ("lpIDList", wintypes.LPVOID),
#                 ("lpClass", ctypes.c_wchar_p),
#                 ("hkeyClass", wintypes.HANDLE),
#                 ("dwHotKey", wintypes.DWORD),
#                 ("hIcon", wintypes.HANDLE),
#                 ("hProcess", wintypes.HANDLE)]

# def execute_as_admin(path, output_file):
#     # Prepare parameters for ShellExecuteEx
#     sei = ShellExecuteInfo()
#     sei.cbSize = ctypes.sizeof(sei)
#     sei.fMask = SEE_MASK_NOCLOSEPROCESS | SEE_MASK_FLAG_NO_UI
#     sei.lpVerb = "runas"
#     sei.lpFile = sys.executable
#     sei.lpParameters = path + " > " + output_file  # Redirect output to file
#     sei.nShow = SW_SHOWNORMAL

#     # Execute as admin
#     ctypes.windll.shell32.ShellExecuteExW(ctypes.byref(sei))
#     return sei.hProcess

# def main():
#     # Step 1: Execute attack.py
#     print("Executing attack.py...")
#     attack_process = execute_as_admin("attack.py", "attack_output.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(attack_process)
    
#     # Step 2: Wait for 3 seconds
#     time.sleep(3)
    
#     # Step 3: Execute sniff.py
#     print("Executing sniff.py...")
#     sniff_process = execute_as_admin("sniff.py", "sniff_output.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(sniff_process, -1)

#     # Step 4: Execute uploadcsv.py
#     print("Executing uploadcsv.py...")
#     uploadcsv_process = execute_as_admin("uploadcsv.py", "uploadcsv_output.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(uploadcsv_process, -1)

#     # Step 5: Execute downloadcsv.py
#     print("Executing downloadcsv.py...")
#     downloadcsv_process = execute_as_admin("downloadcsv.py", "downloadcsv_output.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(downloadcsv_process, -1)

#     # Step 6: Execute DnsModule.py
#     print("Executing DnsModule.py...")
#     dnsmodule_process = execute_as_admin("DnsModule.py", "dnsmodule_output.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(dnsmodule_process, -1)

#     # Step 7: Execute attack2.py
#     print("Executing attack2.py...")
#     attack2_process = execute_as_admin("attack2.py", "attack2_output.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(attack2_process)
    
#     # Step 8: Execute sniff.py again
#     print("Executing sniff.py again...")
#     sniff_process = execute_as_admin("sniff.py", "sniff_output_2.txt")
#     ctypes.windll.kernel32.WaitForSingleObject(sniff_process, -1)

# if __name__ == "__main__":
#     main()
