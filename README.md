HNG
# Stage One: Creating and Hosting an API Endpoint

Welcome to Stage One of the HNG Internship Program! In this stage, you will create and host an API endpoint using the programming language of your choice. The endpoint will accept specific GET request query parameters and return information in JSON format.

## Objective

The objective of this stage is to create a publicly accessible API endpoint that meets the specified requirements.

## Requirements:
---------------

The information required in the JSON response includes:

-  Slack name
-  Current day of the week
-  Current UTC time (with validation of +/-2 minutes)
-  Track
-  GitHub URL of the file being run
-  GitHub URL of the full source code
-  Status Code of Success (200)


### JSON Response Example

```
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
```

## Acceptance Criteria

-  Endpoint Creation: Provide a publicly accessible endpoint.
-  GET Parameters: The endpoint should accept two GET request query parameters: slack_name and track.
-  Example: http://example.com/api?slack_name=example_name&track=backend.
-  Slack Name: The response should include the slack_name passed as a GET request query parameter.
-  Current Day of the Week: Display the current day of the week in full (e.g., Monday, Tuesday, etc.).
-  Current UTC Time: Return the current UTC time, accurate within a +/-2 minute window.
-  Track: The response should display the track of the intern (Backend). This will be based on the track
-  GET parameter passed to the endpoint.
-  GitHub File URL: Include a direct link to the specific file in the GitHub repository that's being executed.
-  GitHub Repo URL: Include a link to the main page of the GitHub repository containing the project's entire source code.
-  Status Code: Return 200 as an integer.
-  JSON Format: The endpoint's response should adhere to the specified JSON format.

## Testing
Before submission, ensure the following:
-  The endpoint is accessible.
-  The returned JSON matches the defined format.
-  Validate the correctness of each data point in the JSON response.


Node js
Postman 
Render
