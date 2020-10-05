# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:39:35 2020

@author: vincent.rubin

This script is based on : https://docs.microsoft.com/en-us/samples/azure-samples/resource-manager-python-template-deployment/resource-manager-python-template-deployment/

"""

import os.path
from deployerDB import Deployer as deployDB
from deployerBack import Deployer as deployBack
from deployerFront import Deployer as deployFront

# This script expects that the following environment vars are set:
#
# AZURE_TENANT_ID: with your Azure Active Directory tenant id or domain
# AZURE_CLIENT_ID: with your Azure Active Directory Application Client ID
# AZURE_CLIENT_SECRET: with your Azure Active Directory Application Secret

my_subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', '11111111-1111-1111-1111-111111111111')   # your Azure Subscription Id
my_resource_group = 'taigaRV'            # the resource group for deployment
my_pub_ssh_key_path = os.path.expanduser('~/.ssh/id_rsa.pub')   # the path to your rsa public key file

msg = "\nInitializing the Deployer class with subscription id: {}, resource group: {}" \
    "\nand public key located at: {}...\n\n"
msg = msg.format(my_subscription_id, my_resource_group, my_pub_ssh_key_path)
print(msg)

# Initialize the deployer class
depDB = deployDB(my_subscription_id, my_resource_group, my_pub_ssh_key_path)
depFront = deployFront(my_subscription_id, my_resource_group, my_pub_ssh_key_path)
depBack = deployBack(my_subscription_id, my_resource_group, my_pub_ssh_key_path)

print("Beginning the deployment... \n\n")
# Deploy the template
depDB.deploy()
depBack.deploy()
depFront.deploy()

print("Done deploying!!\n\nYou can connect via: `ssh azureSample@{}.westus.cloudapp.azure.com`".format(depDB.dns_label_prefix))
print("Done deploying!!\n\nYou can connect via: `ssh azureSample@{}.westus.cloudapp.azure.com`".format(depBack.dns_label_prefix))
print("Done deploying!!\n\nYou can connect via: `ssh azureSample@{}.westus.cloudapp.azure.com`".format(depFront.dns_label_prefix))

# Destroy the resource group which contains the deployment
# deployer.destroy()