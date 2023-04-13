#!/usr/bin/env bash
terraform apply
terraform output -json > terraform.out
j2 -f json ansible_inventory.j2 terraform.out -o ansible_inventory
ansible-playbook reverse_proxy.yml
ansible-playbook clickhouse.yml
ansible-playbook logbroker.yml
