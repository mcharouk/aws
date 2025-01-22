import time

import boto3

crawler_name = "training-data-crawler"

# run crawler
glue_client = boto3.client("glue")

try:
    glue_client.start_crawler(Name=crawler_name)
    # wait until it's done
    while True:
        time.sleep(5)
        crawler = glue_client.get_crawler(Name=crawler_name)
        # print last crawl status
        if crawler["Crawler"]["State"] == "READY":
            break
        else:
            print("Crawler is still running")
    print("Crawler is done")
except glue_client.exceptions.CrawlerRunningException:
    print("Crawler is already running")
