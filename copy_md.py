import os
import shutil

DOCS_DIR = "docs"
DEST_DIR = os.path.join(DOCS_DIR, "md")
LLMS_FILE = "llms.txt"

# Ensure destination root exists
os.makedirs(DEST_DIR, exist_ok=True)

# Copy llms.txt into docs/md/
if os.path.exists(LLMS_FILE):
    dest_llms = os.path.join(DEST_DIR, "llms.txt")
    shutil.copy2(LLMS_FILE, dest_llms)

# Copy all .md files from docs/ into docs/md/, preserving structure
for root, _, files in os.walk(DOCS_DIR):
    for f in files:
        if f.endswith(".md"):
            src_path = os.path.join(root, f)

            # Preserve relative path inside docs/
            rel_path = os.path.relpath(src_path, DOCS_DIR)
            dest_path = os.path.join(DEST_DIR, rel_path)

            # Ensure destination subdirectory exists
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the file
            shutil.copy2(src_path, dest_path)
