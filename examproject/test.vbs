
set oWShell = CreateObject("WScript.Shell")
set objFSO = CreateObject("Scripting.FileSystemObject")
objStartFolder = "UML/Diagrams"

Set objFolder = objFSO.GetFolder(objStartFolder)

Set colFiles = objFolder.Files
counter = 0
For Each objFile in colFiles
	If InStrRev(objFile.name, ".svg") <> 0 Then
		folderArr = Split(objFile.name, "__", -1, 1)
		Folder = ""
		For i=0 to UBound(folderArr)-1 Step 1
			Folder = Folder & folderArr(i) & "/"
			If not objFSO.FolderExists(Folder) Then
				objFSO.CreateFolder(Folder)
			End If
		Next
		'oWShell.Run("inkscape -f UML/Diagrams/" & objFile.Name & " -A test/test.pdf") 
		'counter = counter + 1
		Return
	End If
Next


WScript.Echo("Done! Converted " & counter & " files to pdf.")