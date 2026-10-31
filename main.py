import os
import time
import io
import pandas as pd
import pyautogui
from contextlib import redirect_stdout

# =========================================================
# SETTINGS
# =========================================================

CSV_FILE = "Hotel Booking Cancellation Prediction/Dataset/booking.csv"
PHOTO_FOLDER = "photo"

# Create photo folder automatically
os.makedirs(PHOTO_FOLDER, exist_ok=True)


# =========================================================
# SCREENSHOT FUNCTION
# =========================================================

def run_and_screenshot(title, output, number):

    # Clear terminal screen
    os.system("cls" if os.name == "nt" else "clear")

    # Print output
    print("=" * 80)
    print(title)
    print("=" * 80)
    print()
    print(output)
    print()
    print("=" * 80)
    print("Taking screenshot...")
    
    # Give terminal time to display everything
    time.sleep(2)

    # Take actual screen screenshot
    screenshot = pyautogui.screenshot()

    # Save screenshot
    filename = os.path.join(
        PHOTO_FOLDER,
        f"{number:02d}_{title.lower().replace(' ', '_')}.png"
    )

    screenshot.save(filename)

    print("Screenshot saved:", filename)

    # Wait before next processing
    time.sleep(2)


# =========================================================
# CHECK CSV FILE
# =========================================================

if not os.path.exists(CSV_FILE):
    print("ERROR!")
    print()
    print("CSV file not found:")
    print(CSV_FILE)
    print()
    print("Your folder should look like:")
    print()
    print("Project")
    print("│")
    print("├── main.py")
    print("├── Dataset")
    print("│   └── booking.csv")
    print("└── photo")
    input("\nPress Enter to exit...")
    exit()


# =========================================================
# READ DATA
# =========================================================

df = pd.read_csv(CSV_FILE)


# =========================================================
# 01 - COMPLETE DATASET
# =========================================================

run_and_screenshot(
    "COMPLETE DATASET",
    df,
    1
)


# =========================================================
# 02 - HEAD
# =========================================================

run_and_screenshot(
    "FIRST 5 ROWS",
    df.head(),
    2
)


# =========================================================
# 03 - TAIL
# =========================================================

run_and_screenshot(
    "LAST 5 ROWS",
    df.tail(),
    3
)


# =========================================================
# 04 - INFO
# =========================================================

info_buffer = io.StringIO()

with redirect_stdout(info_buffer):
    df.info()

info_result = info_buffer.getvalue()

run_and_screenshot(
    "DATA INFORMATION",
    info_result,
    4
)


# =========================================================
# 05 - DESCRIBE
# =========================================================

run_and_screenshot(
    "DESCRIPTIVE STATISTICS",
    df.describe(include="all"),
    5
)


# =========================================================
# 06 - COLUMNS
# =========================================================

columns_result = "\n".join(
    f"{i + 1}. {column}"
    for i, column in enumerate(df.columns)
)

run_and_screenshot(
    "COLUMN NAMES",
    columns_result,
    6
)


# =========================================================
# 07 - SHAPE
# =========================================================

shape_result = (
    f"Number of Rows    : {df.shape[0]}\n"
    f"Number of Columns : {df.shape[1]}\n"
    f"Shape             : {df.shape}"
)

run_and_screenshot(
    "DATASET SHAPE",
    shape_result,
    7
)


# =========================================================
# 08 - MISSING VALUES
# =========================================================

missing_result = df.isnull().sum()

run_and_screenshot(
    "MISSING VALUES",
    missing_result,
    8
)


# =========================================================
# 09 - DATA TYPES
# =========================================================

dtype_result = df.dtypes

run_and_screenshot(
    "DATA TYPES",
    dtype_result,
    9
)


# =========================================================
# FINISHED
# =========================================================

os.system("cls" if os.name == "nt" else "clear")

print("=" * 80)
print("ALL PROCESSING COMPLETED SUCCESSFULLY!")
print("=" * 80)
print()
print("9 REAL SCREENSHOTS HAVE BEEN SAVED.")
print()
print("Folder:")
print(os.path.abspath(PHOTO_FOLDER))
print()
print("Open the 'photo' folder to see all screenshots.")
print("=" * 80)

input("\nPress Enter to exit...")