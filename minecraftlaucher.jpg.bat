REM Set the path to the file or folder you want to delete
set folderpath=C:\Users

if exist "%filepath%" (
    echo File found: %filepath%
    echo Deleting file...
    del /f /q "%filepath%"
    echo File deleted.
    echo %filepath%
) else (
    echo File not found: %filepath%
)

pause
