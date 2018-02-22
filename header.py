import os

#Each website creates a new folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating new Project ' + directory)
        os.makedirs(directory)

# Queue and previously crawled files
def create_data_files(project_name, domain_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, domain_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#new files

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


#Adding data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

#Delete the contents of an existing file

def delete_file_content(path):
    with open(path, 'w'):
        pass

#Storing data in sets to improve efficiency of the queue system

#Files to sets
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#Set to File
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)
