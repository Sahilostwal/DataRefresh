import streamlit as st

# ---------------------- ORIGINAL FUNCTIONS (NO CHANGE) ----------------------

def insert_string_at_position(original_string, position, insert_string):
    parts = original_string.split('|')
    if position < 1 or position > len(parts) + 1:
        return original_string
    parts.insert(position - 1, insert_string)
    return '|'.join(parts)

def delete_string_at_position(original_string, position):
    parts = original_string.split('|')
    if position < 1 or position > len(parts):
        return original_string
    parts.pop(position - 1)
    return '|'.join(parts)

# ---------------------- STREAMLIT UI ----------------------

st.title("Table Repair Automation")

uploaded_file = st.file_uploader("Upload your .S file", type=["S", "txt"])

option = st.selectbox(
    "Choose an action",
    ("Insert", "Delete")
)

position = None
insert_string = None
append_string = None

if option == "Insert":
    position = st.number_input("Enter position to insert", min_value=1, step=1)
    insert_string = st.text_input("Enter string to insert")

elif option == "Delete":
    position = st.number_input("Enter position to delete", min_value=1, step=1)

if uploaded_file is not None and st.button("Process"):
    lines = uploaded_file.read().decode().splitlines()
    modified_lines = []

    for line in lines:
        line = line.strip()

        if option == "Insert":
            modified_lines.append(insert_string_at_position(line, position, insert_string))

        elif option == "Delete":
            modified_lines.append(delete_string_at_position(line, position))

    output_content = "\n".join(modified_lines)

    st.success("File processed successfully!")

    st.download_button(
        label="Download Result File",
        data=output_content,
        file_name="result.S",
        mime="text/plain"
    )


