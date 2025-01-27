# Author: Copilot
# Create Date: 1/27/2025
# Summary: This script creates a resource group, virtual network, subnet, network security group, and a Linux virtual machine using the latest Ubuntu 20.04 LTS image.

# Variables
$resourceGroupName = 'rg-devops-az104-netwatcher-lab-dev'
$location = 'eastus'
$vnetName = 'vnet-az104-netwatcher-lab-dev'
$subnetName = 'vsub-az104-netwatcher-lab-dev'
$subnetPrefix = '10.0.0.0/24'
$vnetPrefix = '10.0.0.0/16'
$nsgName = 'az104-netwatcher-lab-dev-nsg'
$vmName = 'az104-netwatcher-lab-dev-vm1'
$image = 'Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest'

# Create a resource group.
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Create subnets configuration.
$Subnet = New-AzVirtualNetworkSubnetConfig -Name $subnetName -AddressPrefix $subnetPrefix

# Create a virtual network.
New-AzVirtualNetwork -Name $vnetName -ResourceGroupName $resourceGroupName -Location $location -AddressPrefix $vnetPrefix -Subnet $Subnet

# Create a network security group.
New-AzNetworkSecurityGroup -Name $nsgName -ResourceGroupName $resourceGroupName -Location $location

# Create a Linux virtual machine using the latest Ubuntu 20.04 LTS image.
New-AzVm -ResourceGroupName $resourceGroupName -Name $vmName -Location $location -VirtualNetworkName $vnetName -SubnetName $subnetName -SecurityGroupName $nsgName -Image $image
