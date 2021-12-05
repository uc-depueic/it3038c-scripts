
    $Memory = Get-ComputerInfo  -Property "OsFreeVirtualMemory"
    $Total = Get-ComputerInfo -Property "OsTotalVirtualMemorySize"
    Get-Date
    $variable.property
    $Memory = $Memory.OsFreeVirtualMemory

    $Total = "5373428"
    $TotalInt = [int]$Total
    $Memory = "1677240"
    $MemoryInt = [int]$Memory
    $Amount = $Total - $Memory


if ($Amount -lt 75000)  {
    write-host ("You should considering adding more memory soon you curently only have $Memory bytes remaining.")

    
    }   else { write-host ("Your System has $Memory bytes of memory left.")

out-file C:\Memory\Memoryleft.txt 
    
Start-Sleep -s 86400
    
}

    