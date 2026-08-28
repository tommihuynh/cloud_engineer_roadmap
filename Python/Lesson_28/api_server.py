from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/servers", methods=["GET"])

def get_servers():
    servers = [
        {
            "server_type": "web",
            "hostname": "web-01",
            "ip": "10.10.10.10",
            "operating_system": "Ubuntu",
            "status": "Running",
            "services": "python.com"
        },
        {
            "server_type": "database",
            "hostname": "dbb-01",
            "ip": "10.10.10.20",
            "operating_system": "Ubuntu",
            "status": "Running",
            "services": "MySQL"
        },
        {
            "server_type": "web",
            "hostname": "web-02",
            "ip": "10.10.10.11",
            "operating_system": "Ubuntu",
            "status": "Stopped",
            "services": "example.com"
        }
    ]
    return jsonify(servers)

if __name__ == "__main__":
    app.run(debug=True)
