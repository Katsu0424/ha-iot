# ECHONET Lite: ノードプロファイル(0x0EF001)の「自ノードインスタンスリスト S」(EPC 0xD6) を
# マルチキャストで Get し、5 秒間の応答を表示する
# 使い方（リポジトリの直下で。HA と同じ Docker ネットワークから）:
#   docker run --rm --network ha_default -v "$PWD/tools/el_probe.py:/el_probe.py:ro" python:3.13-slim python /el_probe.py
import socket, struct, time
MCAST = "224.0.23.0"; PORT = 3610
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", PORT))
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struct.pack("4s4s", socket.inet_aton(MCAST), socket.inet_aton("0.0.0.0")))
s.settimeout(1.0)
# EHD=1081, TID=0001, SEOJ=05FF01(コントローラ), DEOJ=0EF001, ESV=62(Get), OPC=1, EPC=D6(自ノードインスタンスリストS)
frame = bytes.fromhex("1081" "0001" "05FF01" "0EF001" "62" "01" "D6" "00")
s.sendto(frame, (MCAST, PORT))
print("sent Get D6 to", MCAST)
end = time.time() + 5
while time.time() < end:
    try:
        data, addr = s.recvfrom(1500)
    except socket.timeout:
        continue
    if data == frame:
        continue
    print(addr[0], data.hex())
