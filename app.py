import streamlit as st
from pathlib import Path
import os
import shutil

st.set_page_config(page_title="File Manager", layout="centered")

st.title("📁 File & Folder Manager")

# ================= FUNCTIONS ================= #

def list_items():
    p = Path('.')
    return [item for item in p.iterdir()]

def create_folder(name):
    p = Path(name)
    if not p.exists():
        p.mkdir()
        return "Folder created successfully ✅"
    return "Folder already exists ❌"

def delete_folder(name):
    p = Path(name)
    if p.exists() and p.is_dir():
        shutil.rmtree(p)
        return "Folder deleted successfully 🗑️"
    return "No such folder ❌"

def create_file(name, data):
    p = Path(name)
    if not p.exists():
        with open(p, "w") as f:
            f.write(data)
        return "File created successfully ✅"
    return "File already exists ❌"

def read_file(name):
    p = Path(name)
    if p.exists() and p.is_file():
        return p.read_text()
    return "No such file ❌"

def delete_file(name):
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        return "File deleted successfully 🗑️"
    return "No such file ❌"

# ================= UI ================= #

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "List Files/Folders",
        "Create Folder",
        "Delete Folder",
        "Create File",
        "Read File",
        "Delete File"
    ]
)

# -------- LIST -------- #
if menu == "List Files/Folders":
    st.subheader("📄 Files & 📁 Folders")
    for item in list_items():
        st.write(item)

# -------- CREATE FOLDER -------- #
elif menu == "Create Folder":
    name = st.text_input("Enter folder name")
    if st.button("Create Folder"):
        st.success(create_folder(name))

# -------- DELETE FOLDER -------- #
elif menu == "Delete Folder":
    name = st.text_input("Enter folder name to delete")
    if st.button("Delete Folder"):
        st.warning(delete_folder(name))

# -------- CREATE FILE -------- #
elif menu == "Create File":
    name = st.text_input("Enter file name with extension")
    data = st.text_area("Write content")
    if st.button("Create File"):
        st.success(create_file(name, data))

# -------- READ FILE -------- #
elif menu == "Read File":
    name = st.text_input("Enter file name to read")
    if st.button("Read File"):
        st.code(read_file(name))

# -------- DELETE FILE -------- #
elif menu == "Delete File":
    name = st.text_input("Enter file name to delete")
    if st.button("Delete File"):
        st.warning(delete_file(name))

       