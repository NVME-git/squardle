import os
import shutil
from config import OUTPUT_DIR


def clear_output_directory() -> None:
    """Clear and recreate the output directory."""
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
