Sleep(3000)
Local $hIE = WinGetHandle("[Class:IEFrame]")
Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")

If WinExists($hIE,"") Then
 ;MsgBox(0, "message", "exist")
 WinActivate($hIE,"")
 ControlSend($hIE ,"",$hCtrl,"{F6}") ; Gives focus to Open Button
 Sleep(500)
 ControlSend($hIE ,"",$hCtrl,"{TAB}") ; Gives focus to Save Button
 Sleep(500)
 ControlSend($hIE ,"",$hCtrl,"{enter}") ; Submit whatever control has focus

Else
 MsgBox(0, "message", "no exist")
EndIf
 Sleep(500)

WinWait($hIE,"打开文件夹")
ControlSend($hIE ,"",$hCtrl,"{F6}") ; Gives focus to Open Button
Sleep(500)
ControlSend($hIE ,"",$hCtrl,"{ESC}"); Exit the windows promt
Sleep(2000)