

```
# firstboot
executes a couple of ansible playbooks after first boot (systemd only)
[Unit]
Description=kickoff ansible Postinstallation tasks
After=network.target sshd.service
Requires=sshd.service


[Service]
Type=oneshot
ExecStart=/bin/bash -c 't=3; while ! nm-online && [ $t -gt 0 ]; do sleep 10; t=$(( --t )); done; /etc/init.d/firstboot.sh  && systemctl disable firstboot.service >> /root/firstboot.log'
ExecStop=/bin/echo "Do nothing"

[Install]
WantedBy=multi-user.target
```
