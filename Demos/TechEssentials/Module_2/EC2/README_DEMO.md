# Demo steps

* !! Step 1 : Don't forget to assign a public ip to the instance at startup !!

* script to start an apache instance. To execute when internet connection is ok

```
sudo -s
```

```
(
mkdir demo_folder
cd demo_folder
cat >> install_sampleapp.sh << EOF
#!/bin/bash
# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html
EOF
chmod +x install_sampleapp.sh
./install_sampleapp.sh
)
```