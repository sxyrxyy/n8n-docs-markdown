# n8n-docs-markdown
A simple Python tool that clones the [n8n documentation repository](https://github.com/n8n-io/n8n-docs) and merges all markdown files into a single consolidated document.

## What it does

- 📥 Clones the n8n-docs repository
- 🔍 Finds all markdown files in the docs directory
- 📄 Merges them into a single `merged_output.md` file
- 🧹 Cleans up temporary files automatically

## Requirements

- Python 3.x
- Git

## Usage

```bash
python n8n_docs_merger.py
```

The script will create a `merged_output.md` file containing all the n8n documentation in one place.

## Output

The merged file includes:
- All markdown files from the n8n docs
- Clear section headers showing the original file names and locations
- Proper formatting and organization

## License

This tool is for personal use and documentation purposes. The n8n documentation content belongs to [n8n.io](https://n8n.io).
