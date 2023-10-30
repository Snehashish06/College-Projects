import ctypes
import pyautogui
import subprocess



subprocess.call("cmd /c magic.vbs")
center_res = ctypes.windll.user32.GetSystemMetrics(0)/2-200, ctypes.windll.user32.GetSystemMetrics(1)/2-150
pyautogui.moveTo(center_res)
pyautogui.click()
pyautogui.write("cd c:/SchoolProj")
pyautogui.press("enter")
pyautogui.write("python -m BorrowedMoney")
pyautogui.press("enter")