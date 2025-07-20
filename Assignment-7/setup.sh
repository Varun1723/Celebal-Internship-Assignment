#!/usr/bin/env bash

# 1. Login
az login

# 2. Set variables
LOCATION="eastus"
RG="rg-etl-demo"
STORAGE="stgetl$(date +%s)"       # unique name
CONTAINER="datalake"
SQLSRV="sqlsrv-etldemo$(date +%s)"
SQLADMIN="sqladminuser"
SQLPASS="P@ssw0rd1234!"           # change to a strong password
SQLDB="db_etl"
ADF="adf-etl-demo"

# 3. Create resource group
az group create \
  --name $RG \
  --location $LOCATION

# 4. Storage account + container
az storage account create \
  --name $STORAGE \
  --resource-group $RG \
  --location $LOCATION \
  --sku Standard_LRS

CONNSTR=$(az storage account show-connection-string \
  --name $STORAGE \
  --resource-group $RG \
  --query connectionString -o tsv)

az storage container create \
  --name $CONTAINER \
  --connection-string "$CONNSTR"

# 5. SQL Server + Database
az sql server create \
  --name $SQLSRV \
  --resource-group $RG \
  --location $LOCATION \
  --admin-user $SQLADMIN \
  --admin-password $SQLPASS

az sql db create \
  --resource-group $RG \
  --server $SQLSRV \
  --name $SQLDB \
  --service-objective S0

# 6. Open firewall to your IP (optional)
MYIP=$(curl -s https://ifconfig.me)
az sql server firewall-rule create \
  --resource-group $RG \
  --server $SQLSRV \
  --name AllowMyIP \
  --start-ip-address $MYIP \
  --end-ip-address $MYIP

# 7. Create ADF instance
az datafactory factory create \
  --resource-group $RG \
  --factory-name $ADF \
  --location $LOCATION

echo "=== Bootstrap complete ==="
echo "Storage account:   $STORAGE"
echo "Container:         $CONTAINER"
echo "SQL Server:        $SQLSRV"
echo "SQL DB:            $SQLDB"
echo "Data Factory:      $ADF"
