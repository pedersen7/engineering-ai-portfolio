# GitHub Public-Copy Cleanup

These two files are cleaned public-repository copies of the working RAG Demo files.

## Removed / changed
- Removed hard-coded Google API keys from `core_rag.py`.
- Replaced D: drive machine-specific paths with repository-relative paths.
- Made the YOLO model path configurable with `YOLO_MODEL_PATH`, defaulting to `models/best.pt`.
- Made prompt/config paths repository-relative.
- Made the Water Main engineering exhibit optional so a proprietary image does not need to be committed.
- Removed a number of development-history comments that are useful locally but not necessary in the public code.

## Keep private
Do not commit:
- `.env`
- `cert.pem`
- `key.pem`
- proprietary `SOPs/`
- proprietary `prompts/`
- proprietary `reference/`
- proprietary source PDFs used to build the vector database
- proprietary/vector-database contents if they contain derived private material
- private engineering exhibits such as the Water Main diagram
- private model weights unless you intentionally want to publish them

The cleaned files are intended to be copied into the GitHub repository, while the original working files on the D: drive remain your development versions.
