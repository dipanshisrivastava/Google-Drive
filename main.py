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
fourth_id =[]

# Open the CSV file
with open('input.csv', mode='r', newline='') as file:
    csv_reader = list(csv.reader(file)) 
    folder_names = csv_reader[2]
    for idx in range(11, 15):
      folder_names_list.append(folder_names[idx])
      os.makedirs(folder_names[idx], exist_ok=True)
    for idx in range(3, len(csv_reader)):
      for col in range(11, 15):
        try:
          img_url = csv_reader[idx][col]
          id = img_url.split('/d/')[1].split('/view')[0]
          if(col==11):
            first_id.append(id)
          if(col==12):
            second_id.append(id)
          if(col==13):
            third_id.append(id)
          if(col==14):
            fourth_id.append(id)
        except Exception as e:
          print(f"No url: {e}")
          
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

for idx, file_id in enumerate(fourth_id):
    each_folder_name = folder_names_list[3]
    file = drive.CreateFile({'id': file_id})
    try:
      file.FetchMetadata()
      file_name = file['title'] if 'title' in file else f"file_{file_id}"
      file_path = os.path.join(each_folder_name, file_name)
      file.GetContentFile(file_path)
      print('File downloaded in', each_folder_name + ':', file_name)
    except Exception as e:
      print(f"Error downloading: {e}")