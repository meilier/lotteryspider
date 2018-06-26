Sleep(1000)
Local $hIE = WinGetHandle("[Class:IEFrame]")

IF WinExists($hIE,"") Then
   WinActivate($hIE,"")
   WinClose($hIE)
EndIf