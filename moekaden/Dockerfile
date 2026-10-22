# MoekadenRoom（ECHONET Lite のシミュレータ、Sony CSL）を Docker で動かす
# Mac 向けの実行ファイルは無いので Linux64 版の jar を arm64 の Java 8 で動かす。
# 描画は Processing 標準の JAVA2D なので、同梱の amd64 ネイティブ（JOGL）は使わない。
# 画面は Xvfb に出し、noVNC でブラウザから見る（http://localhost:6080/vnc.html）
# スクショ: docker exec moekaden import -window root /tmp/shot.png（imagemagick）
FROM eclipse-temurin:8-jre

RUN apt-get update \
 && apt-get install -y --no-install-recommends xvfb x11vnc novnc websockify imagemagick unzip curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# master の 2020-12-24 のコミットに固定し、zip のハッシュも確かめる
ARG MOEKADEN_COMMIT=aa1798a0b08ff0b10ebfa48e7bdbc9c7c10839b4
ARG MOEKADEN_SHA256=17f96a87c2fa9e7b59228cc528f57789c016c09e2bf719ac9a573dbe802e0474
RUN curl -fsSL -o /tmp/app.zip "https://github.com/SonyCSL/MoekadenRoom/raw/${MOEKADEN_COMMIT}/misc/application.linux64.zip" \
 && echo "${MOEKADEN_SHA256}  /tmp/app.zip" | sha256sum -c - \
 && unzip -q /tmp/app.zip -d /opt \
 && rm /tmp/app.zip

COPY start.sh /start.sh
RUN chmod +x /start.sh

# ECHONET Lite は IPv4 のマルチキャスト（224.0.23.0:3610）
ENV JAVA_TOOL_OPTIONS=-Djava.net.preferIPv4Stack=true
EXPOSE 6080
CMD ["/start.sh"]
