from datetime import datetime, UTC
from pathlib import Path
from tkinter import Tk, filedialog
import shutil

timestamp_ms = int(datetime.now(UTC).timestamp() * 1000)

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

if source_file:
    # Preserve original extension
    destination_file = Path.cwd() / f"{source_file.stem}-{timestamp_ms}{source_file.suffix}"

    shutil.copy2(source_file, destination_file)

    print(f"Copied to: {destination_file}")