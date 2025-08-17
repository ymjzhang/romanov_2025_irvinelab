import os

# Get current working directory (should be 'hto_output')
base_dir = os.getcwd()

# Loop over all subdirectories
for subdir in os.listdir(base_dir):
    subdir_path = os.path.join(base_dir, subdir)

    # Skip if not a directory
    if not os.path.isdir(subdir_path):
        continue

    # Loop over files in subdirectory
    for filename in os.listdir(subdir_path):
        # Skip if already prefixed
        if filename.startswith(f"{subdir}_"):
            continue

        old_path = os.path.join(subdir_path, filename)
        new_filename = f"{subdir}_{filename}"
        new_path = os.path.join(subdir_path, new_filename)

        # Rename file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_filename}")

