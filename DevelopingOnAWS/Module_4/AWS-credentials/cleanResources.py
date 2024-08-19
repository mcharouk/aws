# delete file aws-config-result.txt and aws-credentials-result.txt
import os

os.remove("aws-config-result.txt")
print("aws-config-result.txt has been deleted successfully")
os.remove("aws-credentials-result.txt")
print("aws-credentials-result.txt has been deleted successfully")
