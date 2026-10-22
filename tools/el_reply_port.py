# ECHONET Lite の応答が、要求を送ったポートと 3610 のどちらに返るかを確かめる
# 3610 で待つソケットと、空きポートから送るソケットを用意し、ユニキャストで Get を送る
# 使い方（リポジトリの直下で。HA と同じ Docker ネットワークから）:
#   docker run --rm --network ha_default -v "$PWD/tools/el_reply_port.py:/p.py:ro" python:3.13-slim python /p.py 172.20.0.3
import select, socket, sys, time

target = sys.argv[1]
listen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen.bind(("", 3610))
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sender.bind(("", 0))
print("sender port:", sender.getsockname()[1])
# EHD=1081, TID=0002, SEOJ=05FF01, DEOJ=0EF001, ESV=62(Get), OPC=1, EPC=D6
sender.sendto(bytes.fromhex("1081000205FF010EF0016201D600"), (target, 3610))
end = time.time() + 5
while time.time() < end:
    ready, _, _ = select.select([listen, sender], [], [], 0.5)
    for s in ready:
        data, addr = s.recvfrom(1500)
        name = "port 3610" if s is listen else "sender port"
        print(f"{name} <- {addr[0]}:{addr[1]} {data.hex()}")
