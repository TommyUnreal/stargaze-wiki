import os
import re
import shutil

def copy_files(source_dirs, destination_dir):
    shutil.rmtree(destination_dir)

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for source_dir in source_dirs:
        destination_path = os.path.join(destination_dir, os.path.basename(source_dir))
        shutil.copytree(source_dir, destination_path)
        print(f"Copied {source_dir} to {destination_path}")

def process_md_file(file_path):
    # Read the content of the .md file
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline()
        content = file.read()

    if "#" in first_line and "# " not in first_line:
        tags_match = [tag.strip() for tag in first_line.split("#")]
        prefix = "---\ntags:\n"
        prefix += "".join([f"  - {tag}\n" for tag in tags_match if tag])
        prefix += "---\n\n"
        content = prefix + content
        # Write the modified content back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

def generate_folder_content(root_dir, current_dir, base_level=0):
    content = []
    for item in sorted(os.listdir(current_dir)):
        full_path = os.path.join(current_dir, item)
        level = base_level
        if os.path.isdir(full_path):
            indent = "  " * level
            content.append(f"{indent}* {item}")
            # Recursively get content for subdirectories
            subdir_content = generate_folder_content(root_dir, full_path, level + 1)
            content.extend(subdir_content)
        elif item.endswith(".md") and item != "index.md" and not item.endswith(os.path.basename(current_dir) + ".md"):
            indent = "  " * (level + 1)
            file_name = item[:-3]  # Remove .md extension
            content.append(f"{indent}* [[{file_name}]]")
    return content

def should_create_index(folder_path):
    # Check if folder has any .md files (excluding index.md and folder's own .md)
    folder_name = os.path.basename(folder_path)
    md_files = [f for f in os.listdir(folder_path)
                if f.endswith(".md")
                and f != "index.md"
                and f != f"{folder_name}.md"]
    return len(md_files) == 0

def create_folder_indexes(destination_dir, top_dir):
    for root, dirs, files in os.walk(os.path.join(destination_dir, top_dir)):
        if root == destination_dir:
            continue

        folder_name = os.path.basename(root)
        if should_create_index(root):
            # Generate content starting from this folder
            content = generate_folder_content(root, root)
            if content:  # Only create file if there's content to write
                index_path = os.path.join(root, f"{folder_name}.md")
                with open(index_path, "w", encoding="utf-8") as file:
                    file.write("\n".join(content))
                print(f"Created index file: {index_path}")
            else:
                # Create empty file for folders with no content
                index_path = os.path.join(root, f"{folder_name}.md")
                with open(index_path, "w", encoding="utf-8") as file:
                    pass
                print(f"Created empty index file: {index_path}")

def generate_index_md(destination_dir, top_dir):
    def shortest_path(file_path):
        return file_path.replace("\\", "/").split("/")[-1][:-3]

    with open(os.path.join(destination_dir, "index.md"), "w", encoding="utf-8") as index_file:
        for root, dirs, files in os.walk(os.path.join(destination_dir, top_dir)):
            level = root.replace(destination_dir, "").count(os.sep)
            indent = "  " * level
            index_file.write(f"{indent}* {os.path.basename(root)}\n")
            subindent = "  " * (level + 1)
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.relpath(os.path.join(root, file), destination_dir)
                    index_file.write(f"{subindent}* [[{shortest_path(file_path)}]]\n")
                    if not file.endswith("index.md"):
                        process_md_file(os.path.join(root, file))

def main():
    main_dir = r"G:\.shortcut-targets-by-id\0B3tLbsCYv4OVZHZPLVZQV1lDbVE\vyprávěčka\Project  Stargaze\Obsidian Vault\Stargaze"
    source_dirs_rel = ["Veřejné"]
    source_dirs = [os.path.join(main_dir, d) for d in source_dirs_rel]
    destination_dir = "C:/Program Files/stargaze-wiki/content"

    copy_files(source_dirs, destination_dir)
    for rel_dir in source_dirs_rel:
        generate_index_md(destination_dir, rel_dir)
        # Add this line to create folder indexes
        create_folder_indexes(destination_dir, rel_dir)

if __name__ == "__main__":
    main()