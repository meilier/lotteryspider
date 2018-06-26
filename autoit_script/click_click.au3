Sleep(3000)
Local $hIE = WinGetHandle("[Class:IEFrame]")
Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")


IF WinExists($hIE,"") Then
   WinActivate($hIE,"")
   Local $hIE = WinGetHandle("[Class:IEFrame]")
   Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")
   ControlClick($hIE,"",$hCtrl,"primary",1,793,27)
   Sleep(800)
   ControlSend($hIE,"",$hCtrl,"{enter}")
EndIf

