<# 
  PowerShell: Generic retry wrapper for flaky operations 
#>
function Invoke-WithRetry {
    param(
        [ScriptBlock]$Action,
        [int]$MaxRetries = 3,
        [int]$DelaySeconds = 5
    )
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            return & $Action
        }
        catch {
            Write-Host "Attempt $i failed: $($_.Exception.Message). Retrying in $DelaySeconds sec..."
            Start-Sleep -Seconds $DelaySeconds
        }
    }
    throw "All $MaxRetries attempts failed."
}

# Example usage:
$result = Invoke-WithRetry -Action { Invoke-WebRequest -Uri "ftp://myserver/data.csv" }
