Sleep(5000)
Local $hIE = WinGetHandle("[Class:IEFrame]")
Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")
WinActivate($hIE,"")
ControlSend($hIE ,"",$hCtrl,"{F6}") ; Gives focus to Open Button
Sleep(800)
ControlSend($hIE ,"",$hCtrl,"{TAB}") ; Gives focus to Save Button
Sleep(800)
ControlSend($hIE ,"",$hCtrl,"{enter}") ; Submit whatever control has focus
Sleep(3000)