# PowerShell: Register a Self‑hosted Integration Runtime in ADF

# Install Az.DataFactory module if needed
Install-Module -Name Az.DataFactory -Force -Scope CurrentUser

# --- EDIT THESE ---
$rgName      = "RG-DataFactory"       # your resource group
$dfName      = "ADF-Factory"          # your Data Factory name
$irName      = "SelfHostedIR"         # desired IR name
$key1        = "<KEY1_FROM_PORTAL>"   # get from ADF > Integration Runtimes
$key2        = "<KEY2_FROM_PORTAL>"

# Create or update the SHIR
New-AzDataFactoryIntegrationRuntime `
  -ResourceGroupName $rgName `
  -DataFactoryName    $dfName `
  -Name               $irName `
  -Type               SelfHosted `
  -Key1               $key1 `
  -Key2               $key2

Write-Host "Self‑hosted IR '$irName' configured in '$dfName'."
