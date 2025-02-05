$userAgent = "Mozilla/5.0 (SMART-TV; Linux; Tizen 5.0) AppleWebKit/538.1 (KHTML, like Gecko) Version/5.0 TV Safari/538.1"

Invoke-WebRequest -Uri "https://{{cloudfront_url}}/images/orange-cat.jpg" -UserAgent $userAgent -MaximumRedirection 50 -OutFile "test_files/orange-cat-smarttv.jpg"