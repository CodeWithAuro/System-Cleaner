import os

def clean_system():
    print("--- Starting System Clean-up ---")
    print("Searching for files larger than 50MB in the current directory...\n")
    
    found_any = False
        for root, dirs, files in os.walk("."):
        for name in files:
            filepath = os.path.join(root, name)
            try:
                file_size = os.path.getsize(filepath) / (1024 * 1024)
                
                if file_size > 50:
                    print(f"FOUND: {filepath} ({file_size:.2f} MB)")
                    found_any = True
            except OSError:
                continue 

    if not found_any:
        print("No files larger than 50MB found.")
        
    print("\n--- Clean-up Complete ---")

if __name__ == "__main__":
    clean_system()