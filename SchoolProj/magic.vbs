Option Explicit
dim obj 

Set obj = CreateObject("wscript.shell")
obj.run "C:\SchoolProj\On_My_Way.mp3"
obj.run "cmd.exe"
wscript.quit