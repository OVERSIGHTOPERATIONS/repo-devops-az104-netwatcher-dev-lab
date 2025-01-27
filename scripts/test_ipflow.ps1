# Author: Copilot
# Create Date: 1/27/2025
# Summary: This script creates a resource group, virtual network, subnet, network security group, and a Linux virtual machine using the latest Ubuntu 20.04 LTS image.

# Variables
$resourceGroupName = 'rg-devops-az104-netwatcher-lab-dev'
$location = 'eastus'
$vmName = 'az104-netwatcher-lab-dev-vm1'


# Place myVM configuration into a variable.
$vm = Get-AzVM -ResourceGroupName $resourceGroupName -Name $vmName

# Start the IP flow verify session to test outbound flow to www.bing.com.
Test-AzNetworkWatcherIPFlow -Location $location -TargetVirtualMachineId $vm.Id -Direction 'Outbound' -Protocol 'TCP' -RemoteIPAddress '13.107.21.200' -RemotePort '80' -LocalIPAddress '10.0.0.4' -LocalPort '60000'

# Start the IP flow verify session to test outbound flow to 10.0.1.10.
Test-AzNetworkWatcherIPFlow -Location $location -TargetVirtualMachineId $vm.Id -Direction 'Outbound' -Protocol 'TCP' -RemoteIPAddress '10.0.1.10' -RemotePort '80' -LocalIPAddress '10.0.0.4' -LocalPort '60000'

# Start the IP flow verify session to test outbound flow to 10.10.10.10.
Test-AzNetworkWatcherIPFlow -Location $location -TargetVirtualMachineId $vm.Id -Direction 'Outbound' -Protocol 'TCP' -RemoteIPAddress '10.10.10.10' -RemotePort '80' -LocalIPAddress '10.0.0.4' -LocalPort '60000'

# Start the IP flow verify session to test inbound flow from 10.10.10.10.
Test-AzNetworkWatcherIPFlow -Location $location -TargetVirtualMachineId $vm.Id -Direction 'Inbound' -Protocol 'TCP' -RemoteIPAddress '10.10.10.10' -RemotePort '60000' -LocalIPAddress '10.0.0.4' -LocalPort '80'

# Get the effective security rules for the network interface of myVM.
Get-AzEffectiveNetworkSecurityGroup -NetworkInterfaceName $vmName -ResourceGroupName $resourceGroupName

