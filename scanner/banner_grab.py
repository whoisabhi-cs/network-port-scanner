import socket

def grab_banner(host, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((host, port))

        # Try receiving first (some services send banner automatically)
        try:
            banner = s.recv(1024)
            if banner:
                s.close()
                return banner.decode(errors="ignore")
        except:
            pass

        # If nothing received, try HTTP request
        try:
            s.send(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            banner = s.recv(1024)
            s.close()
            return banner.decode(errors="ignore")
        except:
            s.close()
            return None

    except:
        return None