import socket, json, datetime

HOST, PORT = "0.0.0.0", 2222
LOG_FILE = "honeypot_logs.json"

def log_event(addr, data):
    event = {
        "timestamp": datetime.datetime.now().isoformat(),
        "ip": addr[0],
        "port": addr[1],
        "data": data.decode(errors="ignore") if data else ""
    }
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")

def run_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Honeypot running on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"[!] Connection from {addr}")
            conn.sendall(b"Welcome to fake SSH server\r\n")
            log_event(addr, b"Connection established")
            conn.close()

if __name__ == "__main__":
    run_honeypot()
