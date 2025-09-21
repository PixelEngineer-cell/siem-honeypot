import socket

HOST, PORT = "0.0.0.0", 2222

def run_honeypot():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Honeypot running on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            print(f"[!] Connection from {addr}")
            conn.sendall(b"Welcome to fake SSH server\r\n")
            conn.close()

if __name__ == "__main__":
    run_honeypot()
