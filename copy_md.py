import os
import shutil

DOCS_DIR = "docs"
SITE_DIR = "site"
MD_SUBFOLDER = "md"
LLMS_FILE = "llms.txt"

# Copy llms.txt to site root
if os.path.exists(LLMS_FILE):
    dest_llms = os.path.join(SITE_DIR, "llms.txt")
    os.makedirs(os.path.dirname(dest_llms), exist_ok=True)
    shutil.copy2(LLMS_FILE, dest_llms)

# Copy .md files into site/md/
for root, _, files in os.walk(DOCS_DIR):
    for f in files:
        if f.endswith(".md"):
            src_path = os.path.join(root, f)
            # Keep relative path inside DOCS_DIR
            rel_path = os.path.relpath(src_path, DOCS_DIR)
            # Destination path inside site/md/
            dest_path = os.path.join(SITE_DIR, MD_SUBFOLDER, rel_path)

            # Ensure the directory exists
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(src_path, dest_path)