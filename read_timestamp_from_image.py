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

potential_timestamp = str(source_file.stem)[str(source_file.stem).rfind("-") + 1:]
timestamp_ms = int(potential_timestamp)

dt = datetime.fromtimestamp(timestamp_ms / 1000, UTC)

print("The UTC date/time corresponding to the timestamp in the file name of the image you provided is:", dt)