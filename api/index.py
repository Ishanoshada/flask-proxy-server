from flask import Flask, request, Response, jsonify
import requests
import time
import logging
from werkzeug.exceptions import BadRequest
from urllib.parse import urlparse
import hashlib

app = Flask(__name__)

# Simple in-memory cache (use Redis or similar for production)
cache = {}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define allowed and blocked domains
WHITELISTED_DOMAINS = ['example.com', 'jsonplaceholder.typicode.com']  # Add allowed domains here
BLACKLISTED_DOMAINS = ['badwebsite.com', 'malicious.com']  # Add blocked domains here

# Define allowed IP addresses
ALLOWED_IPS = {'127.0.0.1', '*'}  # Add allowed IP addresses here, '*' allows all

# Helper function to sanitize URL input
def sanitize_input(url):
    parsed_url = urlparse(url)
    return parsed_url.geturl()

# Helper function to validate the URL against whitelist and blacklist
def is_valid_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname

    if not parsed_url.scheme in ['http', 'https']:
        return False
    
    if domain in BLACKLISTED_DOMAINS:
        return False
    
    if WHITELISTED_DOMAINS and domain not in WHITELISTED_DOMAINS:
        return False

    return True

# Create a cache key based on the URL and request method
def get_cache_key(url, method, body=None):
    key_base = f"{method}:{url}"
    if body:
        key_base += f":{hashlib.sha256(body).hexdigest()}"
    return key_base

# Log request details
def log_request(url, method, status_code, duration):
    logger.info(f"Request to {url} using {method} returned {status_code} in {duration:.2f}s")

# IP-based access control
def is_allowed_ip():
    client_ip = request.remote_addr
    return '*' in ALLOWED_IPS or client_ip in ALLOWED_IPS

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def proxy():
    if not is_allowed_ip():
        return jsonify({"error": "Access denied"}), 403

    start_time = time.time()
    target_url = request.args.get('url')
    
    if not target_url:
        raise BadRequest("Missing 'url' parameter")

    sanitized_url = sanitize_input(target_url)
    if not is_valid_url(sanitized_url):
        raise BadRequest("Invalid or blacklisted URL")

    cache_key = get_cache_key(sanitized_url, request.method, request.get_data())
    cached_response = cache.get(cache_key)

    # Return cached response for GET requests if available
    if cached_response and request.method == 'GET':
        logger.info(f"Cache hit for {sanitized_url}")
        return cached_response

    try:
        # Forward the request to the target URL
        resp = requests.request(
            method=request.method,
            url=sanitized_url,
            headers={key: value for (key, value) in request.headers.items() 
                      if key.lower() not in ['host', 'content-length', 'connection', 'transfer-encoding']},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=15,  # Set a timeout for external requests
        )

        # Exclude specific headers that should not be forwarded
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]

        # Create a response to return to the client
        response = Response(resp.content, resp.status_code, headers)

        # Cache successful GET requests
        if request.method == 'GET' and 200 <= resp.status_code < 300:
            cache[cache_key] = response

        duration = time.time() - start_time
        log_request(sanitized_url, request.method, resp.status_code, duration)

        return response

    except requests.RequestException as e:
        # Log error and return a failure message
        logger.error(f"Error proxying request to {sanitized_url}: {str(e)}")
        return jsonify({"error": "An error occurred while processing your request"}), 500


if __name__ == '__main__':
    app.run(debug=True)
