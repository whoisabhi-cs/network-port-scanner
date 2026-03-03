import socket
import threading
import argparse
import json
from scanner.banner_grab import grab_banner

results = []

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        s.close()

        if result == 0:
            banner = grab_banner(target, port)

            service_info = banner.split("\n")[0] if banner else "Unknown"

            print(f"[OPEN] Port {port} → {service_info}")

            results.append({
                "port": port,
                "service": service_info
            })

    except:
        pass


def main():
    parser = argparse.ArgumentParser(description="Multithreaded Network Port & Service Scanner")

    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-sp", "--start-port", type=int, default=1, help="Start port")
    parser.add_argument("-ep", "--end-port", type=int, default=1024, help="End port")
    parser.add_argument("-o", "--output", help="Output file name (JSON)")

    args = parser.parse_args()

    threads = []

    print(f"\nScanning {args.target} from port {args.start_port} to {args.end_port}\n")

    for port in range(args.start_port, args.end_port + 1):
        t = threading.Thread(target=scan_port, args=(args.target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()