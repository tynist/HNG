from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get current UTC time
    current_utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Create the response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_time": current_utc_time,
        "track": track,
        "github_file_url": "https://github.com/tynist/HNG/blob/main/stage_one/app.py",
        "github_repo_url": "https://github.com/tynist/HNG/tree/main",
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=7777)
