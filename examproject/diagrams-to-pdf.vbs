
set oWShell = CreateObject("WScript.Shell")
set objFSO = CreateObject("Scripting.FileSystemObject")
objStartFolder = "UML/Diagrams"

Set objFolder = objFSO.GetFolder(objStartFolder)

Set colFiles = objFolder.Files
counter = 0
For Each objFile in colFiles
	If InStrRev(objFile.name, ".svg") <> 0 Then
		splitArr = Split(objFile.name, "__", -1, 1)
		last = UBound(splitArr)
		
		Folder = "img/diagrams/" & splitArr(0) & "/"
		If not objFSO.FolderExists(Folder) Then
			objFSO.CreateFolder(Folder)
		End If
		
		oWShell.Run("inkscape -f UML/Diagrams/" & objFile.Name & " -A " & Folder & Replace(splitArr(last), ".svg", ".pdf")) 
		counter = counter + 1
	End If
Next


WScript.Echo("Done! Converted " & counter & " files to pdf.")