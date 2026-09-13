import socket
import subprocess
import sys
from datetime import datetime

def ping(host):
    try:
        result = subprocess.run(
            ["ping", "-n" if sys.platform.startswith("win") else "-c", "4", host],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error en ping: {e}"

def resolve_dns(host):
    try:
        return socket.gethostbyname_ex(host)
    except Exception as e:
        return f"Error DNS: {e}"

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        sock.close()

def main():
    target = input("IP o dominio a revisar: ").strip()

    print("\n=== WISP TOOLS - NETWORK CHECK ===")
    print(f"Fecha: {datetime.now()}")
    print(f"Objetivo: {target}\n")

    print("=== DNS ===")
    print(resolve_dns(target))

    print("\n=== PING ===")
    print(ping(target))

    ports = [53, 80, 443, 8728, 8291]

    print("\n=== PUERTOS ===")
    for port in ports:
        status = "ABIERTO" if check_port(target, port) else "CERRADO"
        print(f"Puerto {port}: {status}")

if __name__ == "__main__":
    main()
