# Define the API endpoint URL
$Url = "http://13.60.104.184:8080/payload"

# Path to the JSON file
$JsonFilePath = "C:\Users\Moran\repos\home-exam\tests\example.json"

# Read the JSON content from the file
$JsonPayload = Get-Content -Path $JsonFilePath -Raw

# Define headers (if needed)
$Headers = @{
    "Content-Type" = "application/json"
    # "Authorization" = "Bearer YOUR_TOKEN"  # Include if required
}

# Send the POST request
$response = Invoke-RestMethod -Uri $Url -Method Post -Body $JsonPayload -Headers $Headers

# Output the response
$response
