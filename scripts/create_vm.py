# Author: Copilot
# Create Date: 1/27/2025
# Summary: This script creates a resource group, virtual network, subnet, network security group, and a Linux virtual machine using the latest Ubuntu 20.04 LTS image.
# Note: before running the following CLI must be run: pip install azure-mgmt-resource azure-mgmt-network azure-mgmt-compute


from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network.models import VirtualNetwork, Subnet, NetworkSecurityGroup
from azure.mgmt.compute.models import VirtualMachine, HardwareProfile, StorageProfile, OSProfile, NetworkProfile, NetworkInterfaceReference, ImageReference, LinuxConfiguration, SshConfiguration, SshPublicKey

# Variables
resource_group_name = 'rg-devops-az104-netwatcher-lab-dev'
location = 'eastus'
vnet_name = 'vnet-az104-netwatcher-lab-dev'
subnet_name = 'vsub-az104-netwatcher-lab-dev'
subnet_prefix = '10.0.0.0/24'
vnet_prefix = '10.0.0.0/16'
nsg_name = 'az104-netwatcher-lab-dev-nsg'
vm_name = 'az104-netwatcher-lab-dev-vm1'
image_reference = {
    'publisher': 'Canonical',
    'offer': '0001-com-ubuntu-server-focal',
    'sku': '20_04-lts-gen2',
    'version': 'latest'
}

# Authenticate
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, '<subscription_id>')
network_client = NetworkManagementClient(credential, '<subscription_id>')
compute_client = ComputeManagementClient(credential, '<subscription_id>')

# Create a resource group
resource_client.resource_groups.create_or_update(resource_group_name, {'location': location})

# Create a virtual network
vnet_params = VirtualNetwork(location=location, address_space={'address_prefixes': [vnet_prefix]})
subnet_params = Subnet(name=subnet_name, address_prefix=subnet_prefix)
vnet_params.subnets = [subnet_params]
network_client.virtual_networks.begin_create_or_update(resource_group_name, vnet_name, vnet_params).result()

# Create a network security group
nsg_params = NetworkSecurityGroup(location=location)
network_client.network_security_groups.begin_create_or_update(resource_group_name, nsg_name, nsg_params).result()

# Create a virtual machine
nic = network_client.network_interfaces.get(resource_group_name, '<nic_name>')
vm_params = VirtualMachine(
    location=location,
    hardware_profile=HardwareProfile(vm_size='Standard_DS1_v2'),
    storage_profile=StorageProfile(
        image_reference=ImageReference(**image_reference)
    ),
    os_profile=OSProfile(
        computer_name=vm_name,
        admin_username='<admin_username>',
        admin_password='<admin_password>',
        linux_configuration=LinuxConfiguration(
            disable_password_authentication=True,
            ssh=SshConfiguration(
                public_keys=[
                    SshPublicKey(
                        path='/home/<admin_username>/.ssh/authorized_keys',
                        key_data='<ssh_public_key>'
                    )
                ]
            )
        )
    ),
    network_profile=NetworkProfile(
        network_interfaces=[
            NetworkInterfaceReference(
                id=nic.id
            )
        ]
