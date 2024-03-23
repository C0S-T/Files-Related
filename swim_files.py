import swim_club
import os

SWIM_FOLDER = "swimdata/"
SWIMMERS_OUTPUT_FILE = 'swim_data_operated.txt'
os.remove(SWIMMERS_OUTPUT_FILE)

swim_files = sorted(os.listdir(SWIM_FOLDER))
swim_files.remove('.DS_Store')

def write_in_file(data):
    with open(SWIMMERS_OUTPUT_FILE, 'a') as output_file:
        output_file.write(str(data) +'\n')
        # for swimdata in data:
        #     output_file.write(swimdata)

        
def write_data(data):
    for d in data:
        print(d,end=', ')


for file in swim_files:
    print('\n'+ 'Processing : ',file)
    data = swim_club.read_swim_data(file)
    write_in_file(data)

    #write_data(data)
    
