#!/bin/bash

virt-install --location http://download.eng.bos.redhat.com/released/RHEL-7/7.6/Server/x86_64/os/ \
             --disk /var/tmp/install$1.img,size=10,format=raw \
             --os-variant rhel7.6 \
             --initrd-inject ./ks.cfg \
             --extra-args="ks=file:/ks.cfg" \
             --vcpus 2 \
             --memory 2048 \
             --noreboot \
             --name azure-install-$1
