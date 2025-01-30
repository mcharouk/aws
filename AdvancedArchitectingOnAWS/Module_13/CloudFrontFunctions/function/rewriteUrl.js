mobile_picture_suffix = "-mobile.jpg"
tablet_picture_suffix = "-tablet.jpg"
smarttv_picture_suffix = "-smarttv.jpg"

cloudfront_header_mobile = "CloudFront-Is-Mobile-Viewer"
cloudfront_header_tablet = "CloudFront-Is-Tablet-Viewer"
cloudfront_header_smartTV = "CloudFront-Is-SmartTV-Viewer"

// write me a cloudfront function that rewrites the url with it matches the corresponding header
function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var host = request.headers.host.value;
    var uri = request.uri;
    var new_uri = uri;   
    var new_uri_suffix = null; 

    if (uri.endsWith(".jpg")){
        if (headers[cloudfront_header_mobile] && headers[cloudfront_header_mobile].value === "true") {
            new_uri_suffix = mobile_picture_suffix;
        } else if (headers[cloudfront_tablet_mobile] && headers[cloudfront_tablet_mobile].value === "true") {
            new_uri_suffix = tablet_picture_suffix;
        } else if (headers[cloudfront_header_smartTV] && headers[cloudfront_header_smartTV].value === "true") {
            new_uri_suffix = smarttv_picture_suffix;
        }

        if (new_uri_suffix !== null) {
            new_uri = uri.slice(0, -4) + new_uri_suffix;
        }
    }

    var response = {
        statusCode: 302,
        statusDescription: 'Found',
        headers: {
            "location": { "value": "https://" + host + new_uri }
        }
    };

    return response;
}