# Define the folder path
$folderPath = "C:\Users\mineb\blog\aniadampashut.github.io"
Set-Location $folderPath
Remove-Item ".\posts\*"
# Get all files in the folder
$files = Get-ChildItem -Path ".\markdown"

# Loop through each file and execute a command
foreach ($file in $files) {
    # Replace "YourCommand" with the command you want to execute, 
    # and use $file.FullName to refer to the full path of the file
    pandoc ".\markdown\$file" -f markdown -t html -s -o ".\posts\$file.html"
}