import os

UPLOAD_DIR = "data/uploads"

async def save_uploaded_file(uploaded_file):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    save_path = os.path.join(UPLOAD_DIR, uploaded_file.filename)

    with open(save_path, "wb") as f:
        contents = await uploaded_file.read()
        f.write(contents)

    return save_path