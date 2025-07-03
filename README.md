# 🎬 YouTube 影片下載器 (使用 tkinter + pytubefix)

這是一個簡單易用的 YouTube 影片下載器 GUI 工具，支援影片資訊查詢、畫質選擇、音訊轉 MP3、影片音訊合併下載，透過 Python + tkinter + pytubefix 製作，並使用 FFmpeg 進行影音轉檔。

---

## 🚀 使用方式

1. 確保你已安裝 Python 3.x
2. 安裝必要套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 執行主程式：
   ```bash
   python main.py
   ```
4. 若要下載 MP3 或合併影音，請先安裝 [FFmpeg](https://ffmpeg.org/) 並加入系統環境變數

---

## 📁 專案結構說明

| 檔案             | 說明 |
|------------------|------|
| `main.py`        | 主程式入口，建立 tkinter GUI，處理按鈕事件、顯示影片資訊與使用者互動 |
| `downloader.py`  | 封裝下載功能，包含下載 MP3（音訊）與影片畫質（1080p 等）合併流程 |
| `utils.py`       | 共用工具函式，例如更新 GUI 狀態文字 `update_status()` |
| `requirements.txt` | 記錄本專案所需套件，目前包含 `pytubefix`（YouTube 下載函式庫） |

---

## 🖼 功能特色

- ✅ YouTube 影片網址輸入
- ✅ 顯示影片標題、長度、觀看次數
- ✅ 支援下載音訊（MP3）與多種畫質（1080p, 720p, ...）
- ✅ 使用 FFmpeg 自動合併音訊與影片
- ✅ GUI 介面直覺簡單（tkinter）

---

## 📦 依賴套件

- [`pytubefix`](https://pypi.org/project/pytubefix/) - 安定版 YouTube 下載函式庫
- [`tkinter`](https://docs.python.org/3/library/tkinter.html) - 內建 GUI 工具（Python 標準庫）

---

## 📎 備註

- 若你在執行轉檔時出現錯誤，請檢查是否已安裝 FFmpeg 並正確設定至系統環境變數中。
- 可使用 `PyInstaller` 或 `auto-py-to-exe` 將本工具打包為執行檔（如 `.exe`）。

---

## 🧑‍💻 作者

本專案由 [juncheng0909](https://github.com/juncheng0909) 開發，歡迎協作或提出建議！
