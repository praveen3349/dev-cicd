from flask import Flask, jsonify, Response, request
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask API Dashboard</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/
              bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;\
              400;600;700&display=swap" rel="stylesheet">
        <style>
            :root {
                --primary-blue: #007bff;
                --primary-gradient-start: #6dd5ed;
                --primary-gradient-end: #2193b0;
                --card-bg: white;
                --text-dark: #333;
                --text-light: #666;
                --shadow-light: rgba(0,0,0,0.08);
                --shadow-medium: rgba(0,0,0,0.15);
                --border-radius-lg: 15px;
                --transition-ease: all 0.3s ease;
            }

            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(
                    135deg,
                    var(--primary-gradient-start),
                    var(--primary-gradient-end)
                );
                font-family: 'Inter', sans-serif;
                color: var(--text-dark);
                overflow: hidden;
            }
            .card {
                background: var(--card-bg);
                padding: 3.5rem 4rem;
                border-radius: var(--border-radius-lg);
                box-shadow: 0 10px 30px var(--shadow-medium);
                text-align: center;
                animation: fadeIn 0.8s ease-out forwards;
                border: none;
            }
            h1 {
                font-weight: 700;
                color: var(--primary-blue);
                margin-bottom: 1rem;
                font-size: 2.5rem;
            }
            p.lead {
                color: var(--text-light);
                font-size: 1.15rem;
                margin-bottom: 2rem;
                font-weight: 300;
            }
            .btn-primary {
                background-color: var(--primary-blue);
                border-color: var(--primary-blue);
                padding: 14px 30px;
                font-size: 1.1rem;
                border-radius: 30px;
                transition: var(--transition-ease);
                box-shadow: 0 4px 10px rgba(0, 123, 255, 0.2);
            }
            .btn-primary:hover {
                background-color: #0056b3;
                border-color: #0056b3;
                transform: translateY(-2px);
                box-shadow: 0 6px 15px rgba(0, 123, 255, 0.3);
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-30px) scale(0.95); }
                to { opacity: 1; transform: translateY(0) scale(1); }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask API Dashboard</h1>
            <p class="lead">Monitor and manage your API health with CI/CD.</p>
            <a href="/status" class="btn btn-primary btn-lg\
                    ">Check API Status</a>
        </div>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')


@app.route('/status')
def status():
    current_time_ist = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

    if request.args.get("json") == "true":
        return jsonify({
            'status': 'healthy',
            'message': 'API is running smoothly ✅',
            'uptime': '100%',
            'version': 'v1.0.0',
            'last_updated': current_time_ist
        })

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Status - Flask App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/
              bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;\
                400;600;700&display=swap" rel="stylesheet">
        <style>
            :root {{
                --success-green: #28a745;
                --status-gradient-start: #fbc2eb;
                --status-gradient-end: #a6c1ee;
                --card-bg: white;
                --text-dark: #333;
                --text-light: #666;
                --shadow-light: rgba(0,0,0,0.08);
                --shadow-medium: rgba(0,0,0,0.15);
                --border-radius-lg: 15px;
                --transition-ease: all 0.3s ease;
            }}

            body {{
                background: linear-gradient(
                    135deg,
                    var(--status-gradient-start),
                    var(--status-gradient-end)
                );
                font-family: 'Inter', sans-serif;
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: var(--text-dark);
                overflow: hidden;
            }}
            .status-card {{
                background: var(--card-bg);
                padding: 3rem 4rem;
                border-radius: var(--border-radius-lg);
                box-shadow: 0 10px 30px var(--shadow-medium);
                text-align: center;
                animation: zoomIn 0.8s ease-out forwards;
                border: none;
            }}
            .status-card h2 {{
                color: var(--success-green);
                font-weight: 700;
                margin-bottom: 1.5rem;
                font-size: 2.2rem;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
            }}
            .status-card h2 .icon {{
                font-size: 2.5rem;
                line-height: 1;
            }}
            .status-info {{
                margin-top: 1.5rem;
                font-size: 1.1rem;
                color: var(--text-light);
                text-align: left;
                line-height: 1.8;
            }}
            .status-info p {{
                margin-bottom: 0.5rem;
                display: flex;
                align-items: center;
            }}
            .status-info strong {{
                color: var(--text-dark);
                font-weight: 600;
                min-width: 100px;
                display: inline-block;
            }}
            .btn-back-home {{
                margin-top: 2rem;
                color: var(--primary-blue);
                text-decoration: none;
                font-weight: 600;
                transition: var(--transition-ease);
                display: inline-flex;
                align-items: center;
                gap: 5px;
            }}
            .btn-back-home:hover {{
                color: #0056b3;
                transform: translateX(-5px);
            }}
            @keyframes zoomIn {{
                from {{ transform: scale(0.9); opacity: 0; }}
                to {{ transform: scale(1); opacity: 1; }}
            }}
        </style>
    </head>
    <body>
        <div class="status-card">
            <h2><span class="icon">✅</span> API Status: Healthy</h2>
            <div class="status-info">
                <p><strong>Message:</strong> API is running smoothly</p>
                <p><strong>Uptime:</strong> 100%</p>
                <p><strong>Version:</strong> v1.0.0</p>
                <p><strong>Last Updated:</strong> {current_time_ist}</p>
            </div>
            <a href="/" class="btn-back-home">← Back to Home</a>
        </div>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
