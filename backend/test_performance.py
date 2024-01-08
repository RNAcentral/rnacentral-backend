import requests

endpoint_url = "http://0.0.0.0:8001/api/v2/rna/URS0000049E57_511145"  # DRF
# endpoint_url = "http://127.0.0.1:8000/rna/URS0000049E57_511145"  # FastAPI
num_requests = 100
total_time = 0

for _ in range(num_requests):
    # Make the API request
    response = requests.get(endpoint_url)

    # Get the time taken for the request and add it to the total
    total_time += response.elapsed.total_seconds()

# Calculate the average response time
average_time = total_time / num_requests

print(f"Total time taken for {num_requests} requests: {total_time} seconds")
print(f"Average response time for {num_requests} requests: {average_time} seconds")
