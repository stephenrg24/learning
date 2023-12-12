import tkinter as tk
from tkinter import ttk
import subprocess

def run_maintenance():
    if run_chkdsk_var.get():
        subprocess.run(["chkdsk", "/f"], shell=True)
    if run_sfc_var.get():
        subprocess.run(["sfc", "/scannow"], shell=True)
    if run_dism_var.get():
        subprocess.run(["dism", "/online", "/cleanup-image", "/restorehealth"], shell=True)

def run_updates():
    if choco_upgrade_var.get():
        subprocess.run(["powershell", "-Command", "choco upgrade all -y"], shell=True)
    if winget_upgrade_var.get():
        subprocess.run(["powershell", "-Command", "winget upgrade --all"], shell=True)

def install_winrar():
    subprocess.run(["powershell", "-Command", "winget install winrar"], shell=True)

def install_7zip():
    subprocess.run(["powershell", "-Command", "winget install 7zip"], shell=True)

def uninstall_7zip():
    subprocess.run(["powershell", "-Command", "winget uninstall 7zip"], shell=True)

def install_steam():
    subprocess.run(["powershell", "-Command", "winget install steam"], shell=True)

def uninstall_steam():
    subprocess.run(["powershell", "-Command", "winget uninstall steam"], shell=True)

def uninstall_winrar():
    subprocess.run(["powershell", "-Command", "winget uninstall winrar"], shell=True)

root = tk.Tk()
root.title("Advanced System Maintenance")
root.geometry("800x400")

tab_control = ttk.Notebook(root)

maintenance_tab = ttk.Frame(tab_control)
updates_tab = ttk.Frame(tab_control)
install_tab = ttk.Frame(tab_control)

tab_control.add(maintenance_tab, text='Maintenance')
tab_control.add(updates_tab, text='Updates')
tab_control.add(install_tab, text='Install/Uninstall')

tab_control.pack(expand=1, fill='both')

# Maintenance tab components
run_chkdsk_var = tk.BooleanVar()
run_chkdsk_toggle = ttk.Checkbutton(maintenance_tab, text="Run chkdsk", variable=run_chkdsk_var)
run_chkdsk_toggle.pack()

run_sfc_var = tk.BooleanVar()
run_sfc_toggle = ttk.Checkbutton(maintenance_tab, text="Run sfc /scannow", variable=run_sfc_var)
run_sfc_toggle.pack()

run_dism_var = tk.BooleanVar()
run_dism_toggle = ttk.Checkbutton(maintenance_tab, text="Run dism /online /cleanup-image /restorehealth", variable=run_dism_var)
run_dism_toggle.pack()

run_maintenance_button = ttk.Button(maintenance_tab, text="Run Maintenance", command=run_maintenance)
run_maintenance_button.pack()

# Updates tab components
choco_upgrade_var = tk.BooleanVar()
choco_upgrade_toggle = ttk.Checkbutton(updates_tab, text="Chocolatey Upgrade All", variable=choco_upgrade_var)
choco_upgrade_toggle.pack()

winget_upgrade_var = tk.BooleanVar()
winget_upgrade_toggle = ttk.Checkbutton(updates_tab, text="Winget Upgrade All", variable=winget_upgrade_var)
winget_upgrade_toggle.pack()

run_updates_button = ttk.Button(updates_tab, text="Run Updates", command=run_updates)
run_updates_button.pack()

# Install/Uninstall tab components
utility_frame = ttk.LabelFrame(install_tab, text='Utilities')
utility_frame.grid(row=0, column=0, padx=5, pady=5)

install_winrar_button = ttk.Button(utility_frame, text="Install WinRAR", command=install_winrar)
install_winrar_button.grid(row=0, column=0, padx=5, pady=5)

uninstall_winrar_button = ttk.Button(utility_frame, text="Uninstall WinRAR", command=uninstall_winrar)
uninstall_winrar_button.grid(row=1, column=0, padx=5, pady=5)

install_7zip_button = ttk.Button(utility_frame, text="Install 7Zip", command=install_7zip)
install_7zip_button.grid(row=0, column=1, padx=5, pady=5)

uninstall_7zip_button = ttk.Button(utility_frame, text="Uninstall 7Zip", command=uninstall_7zip)
uninstall_7zip_button.grid(row=1, column=1, padx=5, pady=5)

gaming_frame = ttk.LabelFrame(install_tab, text='Gaming')
gaming_frame.grid(row=0, column=1, padx=5, pady=5)

install_steam_button = ttk.Button(gaming_frame, text="Install Steam", command=install_steam)
install_steam_button.grid(row=0, column=0, padx=5, pady=5)

uninstall_steam_button = ttk.Button(gaming_frame, text="Uninstall Steam", command=uninstall_steam)
uninstall_steam_button.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
