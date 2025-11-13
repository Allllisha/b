# Flet UI カスタマイズ検証用 開発ルール（v1.8準拠）

本ドキュメントは、**Flet UI カスタマイズの検証・開発における標準ルール**を定義します。
eiseikanri プロジェクトの v1.8 ルールに完全準拠し、再利用性と保守性を確保します。

---

## 1. 目的（Purpose）

本プロジェクトは、Flet 0.28.2 を用いた UI カスタマイズの検証および実装を目的とし、以下を実現します：

- Material3 デザインシステムの適用
- カスタムフォント・カラースキームの統一
- レスポンシブレイアウトの実装
- Figma デザイントークンの Python コード変換
- 安全で保守性の高いコード管理（v1.8 準拠）

---

## 2. 開発ルール（v1.8 完全準拠）

本プロジェクトは以下のルールに従います：

✅ **Python 3.12 / Miniconda / Flet 0.28.2 固定**
✅ **flet pack で EXE 化**（PyInstaller 禁止）
✅ **PyMuPDF 禁止** → ReportLab/PyPDF を使用（必要な場合）
✅ **環境変数を使わない**
✅ **1 画面 1 機能**
✅ **カラーコード：#1B5A1A**（プライマリカラー）
✅ **排他：.lock**（ファイル操作時）
✅ **操作ログ：.log / getpass.getuser() 使用**
✅ **フォルダ構成は複数形で統一**（views, utils, assets）
✅ **config.json で設定を一元化**
✅ **requirements.txt にライブラリ明記**（バージョン固定）

---

## 3. プロジェクト構成（v1.8 準拠）

```
fletui/
├── main.py
├── config.json
├── requirements.txt
├── views/
│   ├── dashboard.py
│   ├── theme_test.py
│   └── component_gallery.py
├── utils/
│   ├── theme_loader.py
│   ├── logging.py
│   └── locking.py
├── assets/
│   ├── fonts/
│   │   └── TsukuhouMincho-Regular.ttf
│   └── templates/
│       └── design_tokens.json
├── logs/
│   └── actions.log
└── storage/
    └── (アプリデータ)
```

**重要な規則：**
- フォルダ名は複数形（views, utils, assets, logs）
- 1 画面 = 1 ファイル（views/ 内）
- 設定は config.json に集約
- ログは logs/actions.log に記録

---

## 4. config.json（設定一元化）

```json
{
  "app": {
    "name": "Flet UI Customization Demo",
    "version": "1.0.0"
  },
  "colors": {
    "primary": "#1B5A1A",
    "secondary": "#625B71",
    "surface": "#FFFBFE",
    "background": "#FFFBFE"
  },
  "fonts": {
    "default": "assets/fonts/TsukuhouMincho-Regular.ttf"
  },
  "theme": {
    "use_material3": true,
    "default_mode": "light"
  }
}
```

---

## 5. requirements.txt（固定バージョン）

```
flet==0.28.2
pandas==2.2.2
reportlab==4.0.4
pypdf==4.0.1
```

※ 必要に応じてライブラリを追加可能（バージョン固定必須）

---

## 6. 操作ログ（v1.8 準拠）

- **ファイル：** `logs/actions.log`
- **書式：** `timestamp,user,action,target`
- **user 取得：** `getpass.getuser()`
- **書き込み時：** `.lock` でファイルロック

**例：**
```
2025-11-12 15:30:45,yamada,theme_change,dark_mode
2025-11-12 15:31:12,tanaka,component_add,custom_button
```

---

## 7. 排他制御（.lock）

ファイル操作時（ログ書き込み、設定変更など）は以下の手順：

1. `<filename>.lock` を生成
2. 処理実行
3. 完了または異常終了で削除
4. ロック中は「処理中」と表示

---

## 8. UI カスタマイズ検証項目

### ✅ テーマ（Material3）
- primary/secondary の色（config.json で管理）
- Typography（TextTheme）
- corner radius / elevation / padding

### ✅ コンポーネント装飾
- Container（shadow / border / gradient）
- 背景画像

### ✅ 状態別スタイル
- Hover / Focus / Pressed
- Disabled

### ✅ レスポンシブ
- ResponsiveRow（Bootstrap-like 12 カラム）

### ✅ フォント
- カスタムフォント（ttf/otf）
- config.json で一元管理

### ✅ 画像/SVG
- assets に配置して読み込み

### ✅ デザイントークン
- Figma の色・影・角丸を config.json に変換
- Python コードで参照

---

## 9. 起動方法

```bash
# 開発モード
flet run main.py

# EXE 化（配布用）
flet pack main.py --name fletui_demo
```

---

## 10. Figma → Flet トークン変換

Figma のデザイントークン（色・影・角丸）を `config.json` に自動変換するスクリプトを使用可能。

**例：**
```bash
python utils/figma_to_config.py --input design_tokens.json --output config.json
```

---

## 11. 受け入れ基準（UAT）

✅ config.json からテーマが正しく読み込まれる
✅ カスタムフォントが反映される
✅ レスポンシブレイアウトが機能する
✅ 操作ログが正しく記録される
✅ ロック機構が正常に動作する
✅ flet pack で EXE が正常に生成される

---

## 12. 非機能要件

- オフライン動作
- 軽快な UI レスポンス
- 日本語フォントの正しい表示
- EXE 配布（flet pack）

---

## ✅ 最終まとめ

本プロジェクトは：

✅ **v1.8 ルールに完全準拠**
✅ **Flet 0.28.2 固定**
✅ **config.json で設定一元化**
✅ **複数形フォルダ構成（views, utils, assets）**
✅ **排他・ログ・フォント・色管理**
✅ **1 画面 1 機能の UI 設計**

すべて満たしています。
