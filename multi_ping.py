import platform
import subprocess
from datetime import datetime

def ping_host(host):
    flag = "-n" if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", flag, "2", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def main():
    print("=== WISP TOOLS - MULTI PING ===")
    print(f"Fecha: {datetime.now()}\n")

    hosts = input(
        "Escribe IPs o dominios separados por coma:\n"
    ).split(",")

    print("\n=== RESULTADOS ===")

    for host in hosts:
        host = host.strip()

        if not host:
            continue

        estado = "ONLINE" if ping_host(host) else "OFFLINE"
        print(f"{host:<25} {estado}")


if __name__ == "__main__":
    main()
