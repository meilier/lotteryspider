Sleep(1000)
Local $hIE = WinGetHandle("[Class:IEFrame]")


IF WinExists($hIE,"") Then
   WinActivate($hIE,"")
   WinSetOnTop($hIE, "", 1)
EndIf