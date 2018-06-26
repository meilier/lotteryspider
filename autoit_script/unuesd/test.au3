#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.5
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here
#include<MsgBoxConstants.au3>

        Local $hIE = WinGetHandle("[Class:IEFrame]")
        Local $hCtrl = ControlGetHandle($hIE, "", "[ClassNN:DirectUIHWND1]")
        Local $aPos = ControlGetPos($hIE, "", $hCtrl)
        Local $aWinPos = WinGetPos($hIE)
		ControlGetText($hCtrl)
	    MsgBox($MB_SYSTEMMODAL, "", "Position: " & $aPos[0] & ", " & $aPos[1] & @CRLF & "Size: " & $aPos[2] & ", " & $aPos[3])
		MsgBox($MB_SYSTEMMODAL, "", "Position: " & $aWinPos[0] & ", " & $aWinPos[1] & @CRLF & "Size: " & $aWinPos[2] & ", " & $aWinPos[3])

