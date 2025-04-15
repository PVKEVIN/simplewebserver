
from http.server import HTTPServer, BaseHTTPRequestHandler
content ="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP / IP PROTOCOLS</title>
    <link rel="icon" href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFP9zs1zRTbw-P-Osmmg5hqaGtWJi0gNHASCbw8ycJlnm1K3AI_HRqAUtA06erx9X4SQA&usqp=CAU">
    <style>
        body {
            background-color: #0f0f0f;
            color: #f0f0f0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            text-align: center;
        }

        h1 {
            margin-bottom: 40px;
            font-size: 2.5em;
        }

        .layer-section {
            margin-bottom: 60px;
        }

        .layer-title {
            font-size: 1.8em;
            color: #00bcd4;
            margin-bottom: 20px;
            border-bottom: 2px solid #00bcd4;
            display: inline-block;
            padding-bottom: 5px;
        }

        .tile-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }

        .tile {
            background-color: #1e1e1e;
            border: 1px solid #333;
            border-radius: 10px;
            padding: 15px 25px;
            min-width: 120px;
            transition: transform 0.3s ease, background-color 0.3s ease;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }

        .tile:hover {
            background-color: #2e2e2e;
            transform: scale(1.05);
        }

        @media (max-width: 600px) {
            .tile {
                width: 100%;
                max-width: 300px;
            }
        }
    </style>
</head>
<body>

    <h1>TCP / IP PROTOCOLS</h1>

    <!-- Application Layer -->
    <div class="layer-section">
        <div class="layer-title">Application Layer</div>
        <div class="tile-container">
            <div class="tile">HTTP</div>
            <div class="tile">RDP</div>
            <div class="tile">DNS</div>
            <div class="tile">SMTP</div>
            <div class="tile">TELNET</div>
            <div class="tile">SNMP</div>
        </div>
    </div>

    <!-- Transport Layer -->
    <div class="layer-section">
        <div class="layer-title">Transport Layer</div>
        <div class="tile-container">
            <div class="tile">TCP</div>
            <div class="tile">UDP</div>
        </div>
    </div>

    <!-- Internet Layer -->
    <div class="layer-section">
        <div class="layer-title">Internet Layer</div>
        <div class="tile-container">
            <div class="tile">IP</div>
            <div class="tile">ICMP</div>
            <div class="tile">IGMP</div>
            <div class="tile">ARP</div>
            <div class="tile">IPSec</div>
        </div>
    </div>

    <!-- Network Access Layer -->
    <div class="layer-section">
        <div class="layer-title">Network Access Layer</div>
        <div class="tile-container">
            <div class="tile">Ethernet (IEEE 802.3)</div>
            <div class="tile">Token Ring</div>
            <div class="tile">PPP</div>
            <div class="tile">Frame Relay</div>
        </div>
    </div>

</body>
</html>
"""

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

