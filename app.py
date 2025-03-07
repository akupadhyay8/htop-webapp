from flask import Flask
import subprocess
import datetime
import getpass
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Replace with your full name
    full_name = "Your Full Name"  

    # Get the system username
    username = getpass.getuser()

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Run the 'top' command (batch mode: -b, one iteration: -n 1)
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"], text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        top_output = f"Error retrieving top output: {e.output}"

    # Build the HTML response
    response = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Server Monitoring - htop</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }}
            pre {{ background: #222; color: #0f0; padding: 15px; border-radius: 8px; white-space: pre-wrap; }}
        </style>
    </head>
    <body>
        <h1>Server Monitoring - htop</h1>
        <p><strong>Name:</strong> {full_name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>TOP Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    # Listen on all interfaces (required for Codespaces)
    app.run(host='0.0.0.0', port=5000, debug=True)
