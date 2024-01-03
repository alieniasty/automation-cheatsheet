# Replace these variables with your actual values
$ipToCheck = ""  # Replace this with the IP you want to check
$subscriptionName = ""

# Set the Azure subscription
az account set --subscription $subscriptionName

# Get all VNets in the specified subscription
$vnetList = az network vnet list --query "[].{Name:name, AddressPrefixes:addressSpace.addressPrefixes}" --output json | ConvertFrom-Json

$found = $false

foreach ($vnet in $vnetList) {
    $vnetName = $vnet.Name
    $addressPrefixes = $vnet.AddressPrefixes

    foreach ($prefix in $addressPrefixes) {
        # Check if the IP falls within any of the VNet address ranges
        if ($ipToCheck -like $prefix) {
            Write-Output "IP $ipToCheck is within the address range of VNet $vnetName"
            $found = $true
            break
        }
    }

    if ($found) {
        break
    }
}

if (-not $found) {
    Write-Output "IP $ipToCheck is not within the address range of any VNets in the $subscriptionName subscription"
}