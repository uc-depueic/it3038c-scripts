function getIP {
    (Get-NetIPAddress).IPv4Address | select-string "192"
}
$IP=getIP
$USER = $env:USERNAME
$BODY = "Test"
$hostname = $env:COMPUTERNAME
$date = get-date 
$version = get-host | select-object version

write-host "This machines ip is $IP, the user is $USER, the hostname is $hostname, using powershell $version, and today's date is $date."

out-file C:/it3038c-scripts/powershell/sysinfo.txt 