EFS_ID='{{EFS_ID}}'  && \
sudo mount -t efs -o tls $EFS_ID:/ /mnt/efs  && \
sudo chmod 777 /mnt/efs  && \
sudo echo "Hello From EFS" > /mnt/efs/HelloFromEFS.txt  && \
sudo cat /mnt/efs/HelloFromEFS.txt