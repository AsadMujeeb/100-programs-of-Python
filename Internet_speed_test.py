import speedtest

test = speedtest.Speedtest()

test.download()
test.upload()

download_speed = test.results.download / 1024 / 1024  # Convert to Mbps
upload_speed = test.results.upload / 1024 / 1024  # Convert to Mbps

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
