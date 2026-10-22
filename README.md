# ha-iot

Home Assistant で自宅を IoT 化するシリーズ（Zenn の記事）のコードです。

## 01: ECHONET Lite のシミュレータで照明を操作する

| パス | 中身 |
|---|---|
| `ha/compose.yaml` | Home Assistant Container と MoekadenRoom |
| `moekaden/` | MoekadenRoom（Sony CSL の ECHONET Lite のシミュレータ）を arm64 の Java 21 で動かす Dockerfile。MoekadenRoom 本体はビルドのときに GitHub から取得します（このリポジトリには含みません） |
| `tools/` | ECHONET Lite の応答を確かめるスクリプト |

```bash
cd ha
docker compose up -d --build
```

- Home Assistant: http://localhost:8123
- MoekadenRoom の画面: http://localhost:6080/vnc.html

`ha/config/` は Home Assistant の設定で、ログイン情報などが入るので Git 管理外です。
