import os
from utils import extract_text_from_resume, clean_text, extract_info, tokenize
import pandas as pd

resume_folder = "data/resumes"
parsed_data = []

# Extract and process resumes
for file_name in os.listdir(resume_folder):
    file_path = os.path.join(resume_folder, file_name)
    if os.path.isfile(file_path):
        raw_text = extract_text_from_resume(file_path)
        clean = clean_text(raw_text)
        info = extract_info(clean)
        info['filename'] = file_name
        parsed_data.append(info)

# Save to CSV
df = pd.DataFrame(parsed_data)
df.to_csv("parsed/resume_data.csv", index=False)
print("✅ Resume data extracted and saved.")
