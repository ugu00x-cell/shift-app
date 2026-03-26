# 介護シフト自動作成アプリ

介護施設向けのシフト自動生成Webアプリケーションです。
OR-Tools（Google製の最適化ソルバー）を使い、複雑な制約条件を満たすシフトを自動で作成します。

## 機能

### シフト自動生成
- **介護職員**と**調理職員**を独立したソルバーで処理し、結果をマージ
- OR-Tools CP-SAT（制約充足・最適化）ソルバーを使用
- 祝日判定対応（jpholiday）

### 勤務パターン
| パターン | 時間帯 |
|---------|-------|
| デイ① | 8:30〜17:30 |
| デイ② | 9:00〜16:00 |
| デイ③ | 8:30〜12:30（午前半日） |
| デイ④ | 13:30〜17:30（午後半日） |
| 訪問介護午前 | AM |
| 訪問介護午後 | PM |
| 兼務パターンA | ③デイ + PM訪問 |
| 兼務パターンB | AM訪問 + ④デイ |

### 制約条件
- スタッフごとの希望休・NG日
- 資格に基づく配置ルール
- 連勤制限
- 各ポジションの必要人数
- 調理担当の組み合わせルール

### その他の機能
- スタッフ管理（登録・編集・資格管理）
- シフトカレンダー表示
- Excel / CSV エクスポート
- 設定画面（各種パラメータの調整）

## セットアップ

### 必要な環境
- Python 3.10以上

### インストール

```bash
pip install -r requirements.txt
```

必要なライブラリ:
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- OR-Tools（Google製最適化ソルバー）
- openpyxl（Excel出力用）
- jpholiday（祝日判定）

### 起動

**Windows（簡単）:**
```
setup_and_start.bat をダブルクリック
```
ライブラリのインストールとアプリ起動が自動で行われます。

**手動起動:**
```bash
python app.py
```

ブラウザで http://localhost:5050 を開いてください。

## 使い方

1. **スタッフ登録** — スタッフ一覧画面で名前・資格・勤務可能パターンを登録
2. **希望休の入力** — カレンダー画面で各スタッフの希望休・NG日を設定
3. **シフト生成** — 「シフト生成」ボタンで自動作成（数秒〜数十秒）
4. **確認・調整** — カレンダーで結果を確認。手動調整も可能
5. **出力** — Excel / CSV でエクスポート

## ファイル構成

```
shift-app/
├── app.py              ← Flaskアプリケーション本体
├── solver.py           ← OR-Toolsシフト生成エンジン
├── models.py           ← SQLAlchemyデータモデル
├── config.py           ← 設定（DB接続など）
├── export.py           ← Excel / CSVエクスポート
├── requirements.txt    ← 必要ライブラリ
├── setup_and_start.bat ← Windows用セットアップ＆起動
├── run/
│   └── start_windows.bat
├── static/
│   ├── css/style.css
│   └── js/app.js
└── templates/
    ├── base.html
    ├── index.html
    ├── calendar.html
    ├── staff_list.html
    ├── staff_form.html
    └── settings.html
```

## 技術スタック

| 技術 | 用途 |
|------|------|
| Flask | Webフレームワーク |
| SQLite | データベース |
| SQLAlchemy | ORM |
| OR-Tools CP-SAT | 制約充足・最適化ソルバー |
| openpyxl | Excel出力 |
| jpholiday | 日本の祝日判定 |

## ライセンス

MIT License
