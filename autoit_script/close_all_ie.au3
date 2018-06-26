Sleep(1000)
Local $hIE = WinGetHandle("[Class:IEFrame]")

While WinExists($hIE,"")
   WinActivate($hIE,"")
   WinClose($hIE)
   Local $hIE = WinGetHandle("[Class:IEFrame]")
WEnd