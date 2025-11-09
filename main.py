import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import threading
import platform
import sys
import shlex

try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
except ImportError:
    messagebox.showerror(
        "Eksik Kütüphane",
        "Lütfen 'tkinterdnd2' kütüphanesini yükleyin.\n\nTerminal'e 'pip install tkinterdnd2' yazın."
    )
    exit()

try:
    import sv_ttk
except ImportError:
    messagebox.showerror(
        "Eksik Kütüphane",
        "Lütfen 'sv-ttk' kütüphanesini yükleyin.\n\nTerminal'e 'pip install sv-ttk' yazın."
    )
    exit()


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def center_window(win, width=630, height=720):
    win.update_idletasks()
    screen_w = win.winfo_screenwidth()
    screen_h = win.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")


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

        if options_entry.get().strip():
            suggested_output = os.path.splitext(file_path)[0] + "_converted.mp4"

        output_entry.delete(0, tk.END)
        output_entry.insert(0, suggested_output)


def select_output_file():
    suggested_name = os.path.basename(output_entry.get())
    if not suggested_name:
        input_path = input_entry.get()
        if input_path:
            if options_entry.get().strip():
                suggested_name = os.path.splitext(os.path.basename(input_path))[0] + "_converted.mp4"
            else:
                suggested_name = os.path.splitext(os.path.basename(input_path))[0] + "_whatsapp.mp4"
        else:
            suggested_name = "output_converted.mp4"

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
    custom_options = options_entry.get().strip()

    if not input_file or not os.path.exists(input_file):
        messagebox.showerror("Hata", "Lütfen geçerli bir giriş video dosyası seçin.")
        return
    if not output_file:
        messagebox.showerror("Hata", "Lütfen geçerli bir çıktı dosyası yolu belirtin.")
        return

    toggle_controls(enabled=False)
    progressbar.start()

    if custom_options:
        status_label.config(text="Özel dönüştürme işlemi sürüyor...", style="Primary.TLabel")
    else:
        status_label.config(text="Varsayılan (WhatsApp) dönüştürme sürüyor...", style="Primary.TLabel")

    thread = threading.Thread(
        target=run_ffmpeg_conversion,
        args=(input_file, output_file, custom_options),
        daemon=True
    )
    thread.start()


def run_ffmpeg_conversion(input_file, output_file, custom_options):
    command = []

    if not custom_options:
        command = [
            "ffmpeg", "-i", input_file,
            "-vcodec", "libx264", "-acodec", "aac", "-preset", "veryfast",
            "-movflags", "+faststart", "-pix_fmt", "yuv420p", "-strict", "-2",
            output_file, "-y"
        ]
    else:
        try:
            parsed_options = shlex.split(custom_options)
            command = ["ffmpeg", "-i", input_file]
            command.extend(parsed_options)
            command.extend([output_file, "-y"])
        except Exception as e:
            error_msg = f"Özel parametre hatası:\n{str(e)}"
            root.after(0, on_conversion_complete, False, error_msg)
            return

    try:
        startupinfo = None
        if platform.system() == "Windows":
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESTDHANDLES
            startupinfo.wShowWindow = subprocess.SW_HIDE

        subprocess.run(command, check=True, capture_output=True, text=True, encoding='utf-8', startupinfo=startupinfo)
        root.after(0, on_conversion_complete, True, output_file)

    except FileNotFoundError:
        error_msg = "Hata: FFmpeg bulunamadı.\nPATH değişkenine eklediğinizden emin olun."
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
        status_label.config(text="Durum: İşlem tamamlandı.", style="Success.TLabel")
    else:
        messagebox.showerror("Hata", message)
        status_label.config(text="Durum: Hata oluştu.", style="Error.TLabel")


def toggle_controls(enabled=True):
    state = tk.NORMAL if enabled else tk.DISABLED
    for w in (input_entry, input_browse_btn, output_entry, output_browse_btn, options_entry, convert_btn, theme_toggle):
        w.config(state=state)

    if enabled:
        drop_frame.bind("<Button-1>", select_file)
        drop_label_icon.bind("<Button-1>", select_file)
        drop_label_text.bind("<Button-1>", select_file)
        drop_frame.config(cursor="hand2")
    else:
        drop_frame.unbind("<Button-1>")
        drop_label_icon.unbind("<Button-1>")
        drop_label_text.unbind("<Button-1>")
        drop_frame.config(cursor="arrow")

def on_drag_and_drop(event):
   
    if convert_btn['state'] == tk.DISABLED:
        return 

    try:
    
        data_str = event.data

        file_paths = []
        
      
        if data_str.startswith('{') and data_str.endswith('}'):
           
            file_paths = root.tk.splitlist(data_str)
        else:
         
            file_paths = [data_str]

        if file_paths:
          
            first_path = file_paths[0]
            
       
            if first_path.startswith('{') and first_path.endswith('}'):
                first_path = first_path[1:-1]
            
          
            select_file(path=first_path)
            
    except Exception as e:
        # Hata ayıklama için konsola yazdırmak iyi bir fikirdir
        print(f"Sürükle-bırak hatası: {e}")
        print(f"Alınan event.data: {event.data}")

def toggle_theme():
    if theme_toggle_var.get():
        sv_ttk.set_theme("dark")
    else:
        sv_ttk.set_theme("light")
        apply_soft_light_theme()


root = TkinterDnD.Tk()
root.title("")
center_window(root, 630, 720)
root.resizable(False, False)

sv_ttk.set_theme("light")

style = ttk.Style()
def apply_soft_light_theme():
    light_bg = "#f7f7f7"
    light_card = "#ffffff"
    light_text = "#222222"
    light_secondary = "#666666"

    root.configure(bg=light_bg)
    style.configure("TFrame", background=light_bg)
    style.configure("TLabelFrame", background=light_bg)
    style.configure("Card.TFrame", background=light_card)
    style.configure("TLabel", background=light_bg, foreground=light_text)
    style.configure("Secondary.TLabel", background=light_bg, foreground=light_secondary)
    style.configure("Large.TLabel", background=light_bg, foreground=light_text)
    style.configure("Icon.TLabel", background=light_bg)
    style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"))

apply_soft_light_theme()

style.configure("Success.TLabel", foreground="green")
style.configure("Error.TLabel", foreground="red")
style.configure("Primary.TLabel", foreground="#007acc")
style.configure("Icon.TLabel", font=("Segoe UI Symbol", 28))
style.configure("Large.TLabel", font=("Segoe UI", 12))

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

header_frame = ttk.Frame(main_frame, padding=(20, 15))
header_frame.pack(side=tk.TOP, fill=tk.X)
ttk.Label(header_frame, text="Modern Video Dönüştürücü", style="Large.TLabel").pack(side=tk.LEFT)

theme_toggle_var = tk.BooleanVar()
theme_toggle = ttk.Checkbutton(
    header_frame,
    text="Koyu Mod",
    variable=theme_toggle_var,
    command=toggle_theme,
    style="Switch.TCheckbutton"
)
theme_toggle.pack(side=tk.RIGHT)

content_frame = ttk.Frame(main_frame, padding=(20, 0))
content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

files_frame = ttk.LabelFrame(content_frame, text="Adım 1: Dosyaları Seçin", padding="15", style="Card.TFrame")
files_frame.pack(fill=tk.X, expand=True, pady=(0, 15))

drop_frame = ttk.Frame(files_frame, height=100, style="Card.TFrame")
drop_frame.pack(fill=tk.X, expand=True, pady=5)
drop_frame.drop_target_register(DND_FILES)
drop_frame.dnd_bind('<<Drop>>', on_drag_and_drop)
drop_frame.bind("<Button-1>", select_file)
drop_frame.config(cursor="hand2")

drop_label_icon = ttk.Label(drop_frame, text="📥", style="Icon.TLabel", cursor="hand2")
drop_label_icon.place(relx=0.5, rely=0.35, anchor="center")
drop_label_text = ttk.Label(
    drop_frame,
    text="Video Dosyasını Buraya Sürükleyin veya Tıklayın",
    style="Secondary.TLabel",
    cursor="hand2"
)
drop_label_text.place(relx=0.5, rely=0.75, anchor="center")
drop_label_icon.bind("<Button-1>", select_file)
drop_label_text.bind("<Button-1>", select_file)

input_row = ttk.Frame(files_frame)
input_row.pack(fill=tk.X, expand=True, pady=(15, 0))
input_entry = ttk.Entry(input_row)
input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
input_browse_btn = ttk.Button(input_row, text="Gözat", command=select_file)
input_browse_btn.pack(side=tk.LEFT)

output_row = ttk.Frame(files_frame)
output_row.pack(fill=tk.X, expand=True, pady=10)
output_entry = ttk.Entry(output_row)
output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
output_browse_btn = ttk.Button(output_row, text="Kaydet", command=select_output_file)
output_browse_btn.pack(side=tk.LEFT)

options_frame = ttk.LabelFrame(content_frame, text="Adım 2: Ayarlar (Opsiyonel)", padding="15", style="Card.TFrame")
options_frame.pack(fill=tk.X, pady=0)
options_label = ttk.Label(options_frame, text="Özel FFmpeg Parametreleri (Boş bırakılırsa varsayılan kullanılır):")
options_label.pack(anchor="w", padx=2, pady=(0, 5))
options_entry = ttk.Entry(options_frame)
options_entry.pack(fill=tk.X, expand=True)

footer_frame = ttk.Frame(main_frame, padding=20, style="Card.TFrame")
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
convert_btn = ttk.Button(
    footer_frame,
    text="Dönüştürmeyi Başlat",
    command=start_conversion_thread,
    style="Accent.TButton",
    padding=(10, 10)
)
convert_btn.pack(fill=tk.X, pady=(0, 15))

status_label = ttk.Label(footer_frame, text="Durum: Beklemede", anchor="w")
status_label.pack(fill=tk.X)
progressbar = ttk.Progressbar(footer_frame, mode='indeterminate')
progressbar.pack(fill=tk.X, pady=(5, 0))
sv_ttk.set_theme("light")
root.mainloop()