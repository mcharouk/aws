$userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"

Invoke-WebRequest -Uri "https://{{cloudfront_url}}/images/orange-cat.jpg" -UserAgent $userAgent -MaximumRedirection 50 -OutFile "test_files/orange-cat-mobile.jpg"