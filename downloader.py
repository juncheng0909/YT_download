import os
import subprocess
from tkinter import messagebox, filedialog
from utils import update_status

def download_audio(yt, status_label, window):
    stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    if not stream:
        messagebox.showerror("錯誤", "找不到任何音訊串流。")
        update_status(status_label, "❌ 下載失敗", window)
        return

    save_path = filedialog.asksaveasfilename(
        title="儲存 MP3",
        defaultextension=".mp3",
        filetypes=[("MP3 files", "*.mp3")],
        initialfile=f"{yt.title}.mp3"
    )

    if save_path:
        update_status(status_label, "📥 正在下載音訊並轉換為 MP3...", window)
        temp_file = stream.download()

        try:
            subprocess.run([
                "ffmpeg", "-i", temp_file, "-vn", "-ab", "192k", "-ar", "44100", "-y", save_path
            ], check=True, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
            os.remove(temp_file)
            messagebox.showinfo("完成", "音訊下載並轉換為 MP3 成功！")
            update_status(status_label, "✅ MP3 下載完成！", window)
        except subprocess.CalledProcessError:
            messagebox.showerror("FFmpeg 錯誤", "轉檔失敗，請檢查 FFmpeg 是否安裝")
            update_status(status_label, "❌ FFmpeg 轉檔失敗", window)

def download_video(yt, resolution, status_label, window):
    video_stream = yt.streams.filter(res=resolution, file_extension="mp4", only_video=True).first()
    if not video_stream:
        messagebox.showerror("錯誤", f"無法取得 {resolution} 畫質的影片。")
        update_status(status_label, "❌ 找不到指定畫質", window)
        return

    audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").order_by('abr').desc().first()

    save_path = filedialog.asksaveasfilename(
        title=f"儲存 {resolution} 影片",
        defaultextension=".mp4",
        filetypes=[("MP4 files", "*.mp4")],
        initialfile=f"{yt.title} ({resolution}).mp4"
    )

    if save_path:
        temp_video = "temp_video.mp4"
        temp_audio = "temp_audio.mp4"

        update_status(status_label, f"📥 正在下載 {resolution} 影像...", window)
        video_stream.download(filename=temp_video)

        update_status(status_label, "📥 正在下載音訊...", window)
        audio_stream.download(filename=temp_audio)

        update_status(status_label, "🔄 正在合併影音檔案...", window)
        try:
            subprocess.run([
                "ffmpeg", "-i", temp_video, "-i", temp_audio, "-c:v", "copy", "-c:a", "copy", "-y", save_path
            ], check=True, creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
            os.remove(temp_video)
            os.remove(temp_audio)
            messagebox.showinfo("完成", f"{resolution} 影片下載成功！")
            update_status(status_label, f"✅ {resolution} 影片下載完成！", window)
        except subprocess.CalledProcessError:
            messagebox.showerror("FFmpeg 錯誤", "影音合併失敗，請檢查 FFmpeg 是否安裝")
            update_status(status_label, "❌ FFmpeg 合併失敗", window)
