#!/bin/sh
# 仮想ディスプレイ → VNC → noVNC の順に立ててから MoekadenRoom を起動する
set -e
# MoekadenRoom の画面は 854x480（_f_Back/setup.json）
Xvfb :99 -screen 0 854x480x24 &
export DISPLAY=:99
sleep 1
# VNC はパスワード無し。compose で 127.0.0.1 にだけ公開する
x11vnc -display :99 -forever -shared -nopw -rfbport 5900 -quiet &
websockify --web /usr/share/novnc 6080 localhost:5900 &
cd /opt/application.linux64
exec sh ./MoekadenRoom
