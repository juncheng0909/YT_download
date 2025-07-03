import tkinter as tk
from tkinter import messagebox, filedialog
from pytubefix import YouTube
from downloader import download_audio, download_video
from utils import update_status

# --- GUI Functions ---

def fetch_info():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("錯誤", "請輸入網址")
        return
    update_status(status_label, "🔍 正在抓取資訊，請稍候...", window)

    try:
        yt = YouTube(url)
        title_label.config(text=f"🎬 標題：{yt.title}")
        length_label.config(text=f"⏱ 時長：{yt.length // 60} 分 {yt.length % 60} 秒")
        views_label.config(text=f"👁️ 觀看次數：{yt.views:,}")
        status_label.config(text="✅ 資訊抓取完成！")
    except Exception as e:
        messagebox.showerror("抓取錯誤", str(e))
        status_label.config(text="❌ 抓取失敗")

def download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("錯誤", "請輸入 YouTube 網址")
        return
    update_status(status_label, "🚀 準備下載中...", window)

    try:
        yt = YouTube(url)
        choice = quality_var.get()

        if choice == "音訊 (MP3)":
            download_audio(yt, status_label, window)
        else:
            download_video(yt, choice, status_label, window)

    except Exception as e:
        messagebox.showerror("下載錯誤", str(e))
        status_label.config(text="❌ 下載失敗")

# --- GUI Setup ---

window = tk.Tk()
window.title("🎥 YouTube 影片下載器")
window.geometry("550x450")
window.configure(bg="#f0f0f0")

main_frame = tk.Frame(window, padx=20, pady=20, bg="#f0f0f0")
main_frame.pack(expand=True, fill="both")

tk.Label(main_frame, text="🔗 輸入 YouTube 網址：", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w")
url_entry = tk.Entry(main_frame, width=60, font=("Arial", 10))
url_entry.pack(fill="x", pady=5)

tk.Button(main_frame, text="📄 抓取影片資訊", command=fetch_info, font=("Arial", 10, "bold"), bg="#007BFF", fg="white").pack(fill="x", pady=5)

info_frame = tk.LabelFrame(main_frame, text="影片資訊", padx=10, pady=10, bg="#f0f0f0", font=("Arial", 10))
info_frame.pack(fill="x", pady=10)

title_label = tk.Label(info_frame, text="🎬 標題：", bg="#f0f0f0")
title_label.pack(fill="x")
length_label = tk.Label(info_frame, text="⏱ 時長：", bg="#f0f0f0")
length_label.pack(fill="x")
views_label = tk.Label(info_frame, text="👁️ 觀看次數：", bg="#f0f0f0")
views_label.pack(fill="x")

tk.Label(main_frame, text="⚙️ 選擇畫質 / 格式：", font=("Arial", 12), bg="#f0f0f0").pack(anchor="w", pady=(10, 0))
quality_var = tk.StringVar()
quality_options = ["1080p", "720p", "480p", "360p", "音訊 (MP3)"]
quality_var.set("1080p")
quality_menu = tk.OptionMenu(main_frame, quality_var, *quality_options)
quality_menu.config(font=("Arial", 10), bg="white")
quality_menu.pack(fill="x", pady=5)

tk.Button(main_frame, text="⬇️ 下載", command=download, font=("Arial", 12, "bold"), bg="#28A745", fg="white", height=2).pack(fill="x", pady=10)

status_label = tk.Label(window, text="歡迎使用！", bd=1, relief="sunken", anchor="w", padx=5)
status_label.pack(side="bottom", fill="x")

window.mainloop()
