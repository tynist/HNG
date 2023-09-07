from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('Peter_Ug')
    track = request.args.get('backend')

    # Get current UTC time with validation of +1 hour
    current_time = datetime.now(pytz.utc)
    time_difference = current_time.astimezone(pytz.timezone('UTC+1'))
    current_day = time_difference.strftime('%A')

    # Get GitHub URLs
    github_url_file = 'https://github.com/tynist/blob/master/yourfile.py'
    github_url_source = 'https://github.com/yourusername/yourrepository'

    # Create response JSON
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': str(time_difference),
        'track': track,
        'github_url_file': github_url_file,
        'github_url_source': github_url_source,
        'status_code': 'Success'
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
