import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import threading
import platform
import sys

try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
except ImportError:
    messagebox.showerror(
        "Eksik Kütüphane",
        "Lütfen 'tkinterdnd2' kütüphanesini yükleyin.\n\nTerminal'e 'pip install tkinterdnd2' yazın."
    )
    exit()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def select_file(event=None, path=None):
    if path:
        file_path = path
    elif event:
        file_path = filedialog.askopenfilename(
            title="Video Seç",
            filetypes=[("Video Dosyaları", "*.mp4;*.mov;*.mkv;*.avi;*.flv;*.webm"),
                       ("Tüm Dosyalar", "*.*")]
        )
    else:
        return
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)
        suggested_output = os.path.splitext(file_path)[0] + "_whatsapp.mp4"
        output_entry.delete(0, tk.END)
        output_entry.insert(0, suggested_output)

def select_output_file():
    suggested_name = os.path.basename(output_entry.get())
    if not suggested_name:
        input_path = input_entry.get()
        if input_path:
            suggested_name = os.path.splitext(os.path.basename(input_path))[0] + "_whatsapp.mp4"
        else:
            suggested_name = "output_whatsapp.mp4"
    file_path = filedialog.asksaveasfilename(
        title="Nereye Kaydedilsin?",
        initialfile=suggested_name,
        filetypes=[("MP4 Video", "*.mp4")],
        defaultextension=".mp4"
    )
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)

def start_conversion_thread():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if not input_file or not os.path.exists(input_file):
        messagebox.showerror("Hata", "Lütfen geçerli bir giriş video dosyası seçin.")
        return
    if not output_file:
        messagebox.showerror("Hata", "Lütfen geçerli bir çıktı dosyası yolu belirtin.")
        return
    toggle_controls(enabled=False)
    progressbar.start()
    status_label.config(text="Dönüştürme işlemi sürüyor, lütfen bekleyin...", foreground="#007acc")
    thread = threading.Thread(
        target=run_ffmpeg_conversion,
        args=(input_file, output_file),
        daemon=True
    )
    thread.start()

def run_ffmpeg_conversion(input_file, output_file):
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", "libx264",
        "-acodec", "aac",
        "-preset", "veryfast",
        "-movflags", "+faststart",
        "-pix_fmt", "yuv420p",
        "-strict", "-2",
        output_file,
        "-y"
    ]
    try:
        startupinfo = None
        if platform.system() == "Windows":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESTDHANDLES
            startupinfo.wShowWindow = subprocess.SW_HIDE
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            startupinfo=startupinfo
        )
        root.after(0, on_conversion_complete, True, output_file)
    except FileNotFoundError:
        error_msg = "Hata: FFmpeg bulunamadı.\nLütfen FFmpeg'i yükleyin ve sistem 'PATH' değişkenine ekleyin."
        root.after(0, on_conversion_complete, False, error_msg)
    except subprocess.CalledProcessError as e:
        error_msg = f"FFmpeg Hatası:\n{e.stderr}"
        root.after(0, on_conversion_complete, False, error_msg)
    except Exception as e:
        error_msg = f"Beklenmedik bir hata oluştu:\n{str(e)}"
        root.after(0, on_conversion_complete, False, error_msg)

def on_conversion_complete(success, message):
    progressbar.stop()
    toggle_controls(enabled=True)
    if success:
        messagebox.showinfo("Başarılı", f"Dönüştürme tamamlandı!\n\nKaydedildi: {message}")
        status_label.config(text="Durum: İşlem tamamlandı.", foreground="green")
    else:
        messagebox.showerror("Hata", message)
        status_label.config(text="Durum: Hata oluştu.", foreground="red")

def toggle_controls(enabled=True):
    state = tk.NORMAL if enabled else tk.DISABLED
    input_browse_btn.config(state=state)
    output_browse_btn.config(state=state)
    convert_btn.config(state=state)
    input_entry.config(state=state)
    output_entry.config(state=state)

def on_drag_and_drop(event):
    try:
        file_paths = root.tk.splitlist(event.data)
        if file_paths:
            select_file(path=file_paths[0])
    except Exception as e:
        print(f"Sürükle-bırak hatası: {e}")

root = TkinterDnD.Tk()
root.title("Gelişmiş Video Dönüştürücü (WhatsApp Uyumlu)")
root.geometry("600x300")
root.resizable(False, False)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

center_window(root)

try:
    icon_path = resource_path("icon.png")
    if os.path.exists(icon_path):
        photo = tk.PhotoImage(file=icon_path)
        root.iconphoto(False, photo)
    else:
        print("İkon dosyası 'icon.png' bulunamadı.")
except Exception as e:
    print(f"İkon yüklenirken hata oluştu: {e}")

style = ttk.Style(root)
style.theme_use("clam")

main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

drop_frame = ttk.LabelFrame(main_frame, text="Video Dosyasını Buraya Sürükle Bırak")
drop_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind('<<Drop>>', on_drag_and_drop)
drop_frame.bind("<Button-1>", select_file)
drop_frame.config(cursor="hand2")

ttk.Label(drop_frame, text="veya 'Gözat' butonuna tıkla", foreground="#777", anchor="center").pack(pady=10)

input_label = ttk.Label(main_frame, text="Giriş Video Dosyası:")
input_label.grid(row=1, column=0, sticky="w", padx=2, pady=5)

input_entry = ttk.Entry(main_frame, width=70)
input_entry.grid(row=2, column=0, sticky="ew", padx=(0, 5))

input_browse_btn = ttk.Button(main_frame, text="Gözat", command=select_file)
input_browse_btn.grid(row=2, column=1, sticky="e")

output_label = ttk.Label(main_frame, text="Çıktı Dosyası Yolu:")
output_label.grid(row=3, column=0, sticky="w", padx=2, pady=(10, 5))

output_entry = ttk.Entry(main_frame, width=70)
output_entry.grid(row=4, column=0, sticky="ew", padx=(0, 5))

output_browse_btn = ttk.Button(main_frame, text="Kaydet", command=select_output_file)
output_browse_btn.grid(row=4, column=1, sticky="e")

style.configure("Convert.TButton", foreground="white", background="#4CAF50", font=('Helvetica', 10, 'bold'))
convert_btn = ttk.Button(
    main_frame,
    text="Dönüştür (H.264 + AAC)",
    command=start_conversion_thread,
    style="Convert.TButton",
    padding=(10, 10)
)
convert_btn.grid(row=5, column=0, columnspan=2, pady=20, sticky="ew")

status_label = ttk.Label(main_frame, text="Durum: Beklemede", foreground="#555")
status_label.grid(row=6, column=0, columnspan=2, sticky="w", pady=(10, 0))

progressbar = ttk.Progressbar(main_frame, mode='indeterminate')
progressbar.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(5, 10))

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=0)

root.mainloop()
