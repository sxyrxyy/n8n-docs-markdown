import os
import shutil
import subprocess

REPO_URL = "https://github.com/n8n-io/n8n-docs.git"
CLONE_DIR = "n8n-docs"
DOCS_SUBDIR = os.path.join(CLONE_DIR, "docs")
OUTPUT_FILE = "merged_output.md"

def clone_repo():
    print(f"📥 Cloning repository from {REPO_URL}...")
    subprocess.run(["git", "clone", REPO_URL], check=True)
    print("✅ Repository cloned successfully.")

def merge_markdown_files(root_dir, output_file):
    markdown_files = []

    print(f"🔍 Searching for markdown files in: {root_dir}")
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in sorted(filenames):
            if filename.lower().endswith('.md'):
                full_path = os.path.join(dirpath, filename)
                markdown_files.append(full_path)

    print(f"📄 Found {len(markdown_files)} markdown file(s).")

    merged_count = 0
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in markdown_files:
            relative_path = os.path.relpath(file_path, root_dir)
            folder = os.path.dirname(relative_path)

            outfile.write(f"\n\n---\n\n")
            outfile.write(f"### 📄 `{os.path.basename(file_path)}` (found in `{folder}`)\n\n")

            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n")
            merged_count += 1

    print(f"✅ Successfully merged {merged_count} markdown file(s) into '{output_file}'.")

def cleanup():
    if os.path.exists(CLONE_DIR):
        print(f"🧹 Deleting cloned repository: {CLONE_DIR}")
        shutil.rmtree(CLONE_DIR)
        print("✅ Cleanup complete.")

if __name__ == '__main__':
    try:
        clone_repo()
        merge_markdown_files(DOCS_SUBDIR, OUTPUT_FILE)
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        cleanup()
