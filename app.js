const express = require('express'); // Import the Express module
const app = express(); // Create an Express application
const port = process.env.PORT || 3000; // Get port from PORT env var, default to 3000

// Define a route for the /api endpoint
app.get('/api', (req, res) => {
    const { slack_name, track } = req.query;
    const currentDay = new Date().toLocaleDateString('en-US', { weekday: 'long' });
    const utcTime = new Date().toISOString();

  // Create a response object
  const response = {
    slack_name,
    current_day: currentDay,
    utc_time: utcTime,
    track: track || 'backend',
    github_file_url: 'https://github.com/tynist/HNG/blob/main/app.js',
    github_repo_url: 'https://github.com/tynist/HNG',
    status_code: 200,
  };

  res.json(response);  // Send the response as JSON
});

// Start the Express server and listen on port 3000
app.listen(port, console.log(
  `Server started on port ${port}`));
