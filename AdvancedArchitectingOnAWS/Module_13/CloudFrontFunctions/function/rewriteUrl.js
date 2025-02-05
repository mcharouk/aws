
// write me a cloudfront function that rewrites the url with it matches the corresponding header
function handler(event) {
    var request = event.request;
    var headers = request.headers;
    var host = headers.host.value;
    var uri = request.uri;
    

    const SUFFIXES = {
        mobile: '-mobile.jpg',
        tablet: '-tablet.jpg',
        smarttv: '-smarttv.jpg'
    };

    const HEADERS = {
        mobile: 'cloudfront-is-mobile-viewer',
        tablet: 'cloudfront-is-tablet-viewer',
        smarttv: 'cloudfront-is-smarttv-viewer'
    };

    if (!uri.endsWith('.jpg')) {
        return request;
    }

    if (uri.endsWith(SUFFIXES.mobile) || 
        uri.endsWith(SUFFIXES.tablet) || 
        uri.endsWith(SUFFIXES.smarttv)) {
        return request;
    }

    let new_uri = uri;
    if (headers[HEADERS.tablet] && headers[HEADERS.tablet].value === 'true') {
        new_uri = uri.slice(0, -4) + SUFFIXES.tablet;
    } else if (headers[HEADERS.smarttv] && headers[HEADERS.smarttv].value === 'true') {
        new_uri = uri.slice(0, -4) + SUFFIXES.smarttv;
    } else if (headers[HEADERS.mobile] && headers[HEADERS.mobile].value === 'true') {
            new_uri = uri.slice(0, -4) + SUFFIXES.mobile;        
    } else {
        return request;
    }
    
    return {
        statusCode: 302,
        statusDescription: 'Found',
        headers: {
            "location": { "value": `https://${host}${new_uri}` }
        }
    };
}