# Flet UI カスタマイズ検証用 .CLAUDE.md

以下は、**ローカル（localhost）だけで Flet の UI カスタマイズを完全検証するための手順書**です。

---

## ✅ 2. プロジェクト構成

```
fletui/
├── main.py
└── assets/
    └── fonts/
        └── Inter-Regular.ttf
```

`assets/fonts/` には任意のフォントファイル（ttf/otf）を入れる。

---

## ✅ 3. main.py（UI カスタマイズを一気に試せるテンプレート）

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet UI Customization Test"
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary="#6750A4", secondary="#EADDFF"),
        use_material3=True,
        font_family="Inter",
    )
    page.fonts = {
        "Inter": "assets/fonts/Inter-Regular.ttf",
    }

    # カード（角丸 + 影 + グラデ）
    card = ft.Container(
        width=300,
        height=150,
        padding=20,
        border_radius=20,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#FCE4EC", "#F8BBD0"],
        ),
        shadow=ft.BoxShadow(
            spread_radius=1, blur_radius=20, color="#00000020"
        ),
        content=ft.Text("Custom Card", size=20, weight=ft.FontWeight.W_600),
    )

    # ボタン（状態別スタイル）
    button = ft.ElevatedButton(
        "Custom Button",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=14),
            bgcolor={
                ft.MaterialState.DEFAULT: "#6750A4",
                ft.MaterialState.HOVERED: "#7F67BE",
            },
            padding=20,
        ),
    )

    # レスポンシブレイアウト
    layout = ft.ResponsiveRow([
        ft.Container(card, col={"xs":12, "md":6}),
        ft.Container(button, col={"xs":12, "md":6}),
    ])

    page.add(layout)

ft.app(target=main)
```

---

## ✅ 4. 起動

```bash
flet run main.py
```

ブラウザが自動で開き、`http://localhost:8550` で UI が確認できる。

---

## ✅ 5. 検証できる項目一覧

### ✅ テーマ（Material3）

- primary/secondary の色
- Typography（TextTheme）
- corner radius / elevation / padding

### ✅ コンポーネント装飾

- Container
- shadow / border / gradient
- 背景画像

### ✅ 状態別スタイル

- Hover / Focus / Pressed
- Disabled

### ✅ レスポンシブ

- ResponsiveRow (Bootstrap-like 12 カラム)

### ✅ フォント

- カスタムフォント（ttf/otf）
- 字形・太さテスト

### ✅ 画像/SVG

- assets に置くだけで読み込み可能

### ✅ デザイン組の Figma コンポーネント再現性検証

- ピクセル合わせ（近似）
- コンポーネントの共通化
- トークン（色/角丸/影）をテーマ化

---

## ✅ 6. 高度な検証（Flutter 拡張）

Flet Extensions を使えば、Figma で作った特殊 UI コンポーネントを Flutter で実装し Flet から呼び出せる。

例：

- 特殊スライダー
- カスタムドロップダウン
- アニメーション UI

ローカル環境だけでテスト可能。

---

## ✅ 7. 実務的な使い方

1. **デザイントークン（色/角丸/影）を Theme に落とす**
2. 主要 UI（Button/Card/TextField）を先に共通化
3. 画面幅を変えてレスポンシブ挙動を確認
4. フォント反映が正しいかチェック
5. 必要なら Flutter 拡張でギャップを埋める

---

## ✅ 必要なら「Figma → Flet トークン変換スクリプト」も作成できます

Figma の色・影・角丸を自動で Python (Flet Theme) に変換する CLI の作成も可能です。

URL かトークン表があれば、次のステップを作ります。
