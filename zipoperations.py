import os
import zipfile

def backup_to_zip(folder):
    # Ensure folder exists
    if not os.path.isdir(folder):
        print("Error: Folder not found!")
        return

    # Create a unique ZIP filename
    zip_filename = folder + "_backup.zip"

    print(f"Creating backup ZIP file: {zip_filename}")

    # Create the zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        # Walk through the folder
        for foldername, subfolders, filenames in os.walk(folder):
            # Add current folder to ZIP
            backup_zip.write(foldername)

            # Add individual files
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                backup_zip.write(file_path)

    print("Backup completed successfully!")


# -------------------------------
# Main Program
# -------------------------------
folder_name = input("Enter the folder name to back up: ")
backup_to_zip(folder_name)
