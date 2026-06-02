from datetime import datetime, UTC
from pathlib import Path
from tkinter import Tk, filedialog

# Select image
root = Tk()
root.withdraw()

source_file = Path(
    filedialog.askopenfilename(
        title="Select an image",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff *.webp"),
            ("All files", "*.*")
        ]
    )
)

root.destroy()

timestamp_ms = int(source_file[source_file.stem.rfind("-"):])

dt = datetime.fromtimestamp(timestamp_ms / 1000, UTC)

print("The date/time corresponding to the timestamp in the file name of the image you provided is:", dt)