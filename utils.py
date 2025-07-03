def update_status(label, text, window=None):
    label.config(text=text)
    if window:
        window.update_idletasks()
