EFS_ID='{{EFS_ID}}'  && \
sudo mount -t efs -o tls $EFS_ID:/ /mnt/efs  && \
sudo ls -l /mnt/efs  && \
sudo cat /mnt/efs/HelloFromEFS.txt