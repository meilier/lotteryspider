Sleep(1000)
Local $hIE = WinGetHandle("[Class:IEFrame]")
Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")

Local $i=0
Local $A=1
IF WinExists($hIE,"") Then
   WinActivate($hIE,"")
   Local $aPos = ControlGetPos($hIE, "", $hCtrl)
   Local $aWinPos = WinGetPos($hIE)
   While ControlCommand($hIE, "", $hCtrl, "IsVisible") And $aPos[1]> .75 * $aWinPos[3] And WinExists($hCtrl)
		 Sleep(500)
		 WinActivate($hIE,"")
		 ;ControlSend($hIE ,"",$hCtrl,"{Close}"); Exit the windows promt
		 WinClose($hCtrl)
		 MsgBox(0,"Run",$i)
		 Local $hIE = WinGetHandle("[Class:IEFrame]")
		 Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")
		 Local $aPos = ControlGetPos($hIE, "", $hCtrl)
		 Local $aWinPos = WinGetPos($hIE)
		 ;$i = $i +1
		 ;If $i >2 Then ExitLoop
   WEnd
   ;MsgBox(0,"Run",$A)
EndIf

;Local $i=0
;while WinExists($hIE,"") AND $hCtrl <> 0
;	MsgBox(0,"Run",$i)
;	WinActivate($hIE,"")
;	ControlSend($hIE ,"",$hCtrl,"{ESC}"); Exit the windows promt
;	MsgBox(0,"Exit promt",$i)
;	sleep(1000)
;	Local $hIE = WinGetHandle("[Class:IEFrame]")
;	Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")
;WEnd
;Sleep(1000)
