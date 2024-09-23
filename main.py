import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)


folder_names_list = []
first_id = []
second_id = []
third_id = []

# Open the CSV file
with open('input.csv', mode='r', newline='') as file:
    csv_reader = list(csv.reader(file)) 
    folder_names = csv_reader[0]
    for folder in folder_names:
      folder_names_list.append(folder)
      os.makedirs(folder, exist_ok=True)
    for idx in range(1, len(csv_reader)):
      id1 = csv_reader[idx][0].split('/d/')[1].split('/view')[0]
      first_id.append(id1)
      id2 = csv_reader[idx][1].split('/d/')[1].split('/view')[0]
      second_id.append(id2)
      id3 = csv_reader[idx][2].split('/d/')[1].split('/view')[0]
      third_id.append(id3)

# print("Folder Names List:", folder_names_list)
# print("First IDs:", first_id)
# print("Second IDs:", second_id)
# print("Third IDs:", third_id)

for idx, file_id in enumerate(first_id):
    each_folder_name = folder_names_list[0]
    file = drive.CreateFile({'id': file_id})
    try:
      file.FetchMetadata()  # Fetch metadata to get title
      file_name = file['title'] if 'title' in file else f"file_{file_id}"
      # Construct the file path
      file_path = os.path.join(each_folder_name, file_name)
      file.GetContentFile(file_path)
      print('File downloaded in', each_folder_name + ':', file_name)
    except Exception as e:
      print(f"Error downloading: {e}")

for idx, file_id in enumerate(second_id):
    each_folder_name = folder_names_list[1]
    file = drive.CreateFile({'id': file_id})
    try:
      file.FetchMetadata()
      file_name = file['title'] if 'title' in file else f"file_{file_id}"
      file_path = os.path.join(each_folder_name, file_name)
      file.GetContentFile(file_path)
      print('File downloaded in', each_folder_name + ':', file_name)
    except Exception as e:
      print(f"Error downloading: {e}")

for idx, file_id in enumerate(third_id):
    each_folder_name = folder_names_list[2]
    file = drive.CreateFile({'id': file_id})
    try:
      file.FetchMetadata()
      file_name = file['title'] if 'title' in file else f"file_{file_id}"
      file_path = os.path.join(each_folder_name, file_name)
      file.GetContentFile(file_path)
      print('File downloaded in', each_folder_name + ':', file_name)
    except Exception as e:
      print(f"Error downloading: {e}")