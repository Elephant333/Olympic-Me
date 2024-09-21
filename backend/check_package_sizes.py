import os
import subprocess

def get_package_sizes(requirements_file='requirements.txt'):
    # Create a directory to store downloaded packages
    download_dir = "package_downloads"
    os.makedirs(download_dir, exist_ok=True)

    # Use pip to download the packages from the requirements file
    subprocess.run(['pip', 'download', '-r', requirements_file, '-d', download_dir])

    # Calculate and display the size of each package
    total_size = 0
    print(f"\n{'Package':<40} {'Size (MB)':>10}")
    print('-' * 50)

    for package_file in os.listdir(download_dir):
        file_path = os.path.join(download_dir, package_file)
        file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB
        total_size += file_size_mb
        print(f"{package_file:<40} {file_size_mb:>10.2f}")

    print('-' * 50)
    print(f"{'Total Size':<40} {total_size:>10.2f} MB")

if __name__ == "__main__":
    get_package_sizes()
