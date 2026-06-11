import os

export_dir = r"C:\Users\Ananya Lakkaraju\Downloads\Healthcare-Analytics-Project\powerbi_exports"

print("Folder exists:", os.path.exists(export_dir))
print("\nFiles found:")
for file in os.listdir(export_dir):
    full_path = os.path.join(export_dir, file)
    print(f"  {full_path}")