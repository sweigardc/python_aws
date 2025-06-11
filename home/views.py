from django.http import HttpResponse


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Python & Django on AWS Demo</title>
        <style>
            body {
                background: black;
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #222;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container {
                background: rgba(255,255,255,0.95);
                padding: 2.5rem 3rem;
                border-radius: 1.5rem;
                box-shadow: 0 8px 32px rgba(44, 62, 80, 0.15);
                text-align: center;
            }
            h1 {
                color: #2d5be3;
                margin-bottom: 0.5em;
                font-size: 2.5rem;
            }
            p {
                font-size: 1.25rem;
                color: #444;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome!</h1>
            <p>This is a demonstration of <strong>Python</strong> and <strong>Django</strong> deployed on <strong>AWS</strong>.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)