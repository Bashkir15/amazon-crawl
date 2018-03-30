import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Database
database = "amazon_crawler"
host = ""
user = ""

# Redis
redis_host = ""
redis_port = 6379
redis_db = 0

# Request
headers = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate, sdch, br",
	"Accept-Language": "en-US,en;q=0.8",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (LHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
allowed_params = ["node", "rh", "page"]

# Proxies
proxies = [
	# Need to get a good proxy service
	# Might use https://proxybonanza.com
]
proxy_user = ""
proxy_pass = ""
proxy_port = ""

# Crawling Logic
start_file = os.path.join(current_dir, "start-urls.txt")
max_request = 2 * 10**6 # Two Million
max_details_per_listing = 9999

# Threads
max_threads = 200

# Logging & Storage
log_stdout = True
image_dir = "/tmp/crawl_images"
export_dir = "/tmp"