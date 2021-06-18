import os
import re
import glob
from posixpath import curdir

base_url = 'http://172.18.220.5/_public/'
md_base_url = 'http://172.18.220.5/public/'
public_path = '/media/disk1/nas/ail/public/'
workspace_path = '/media/disk1/nas/ail/ail_page/docs/public/'
exclude_section = ['imgs']

def update_public_index(fold_path):
    public_index = '## File Browser\n'
    public_index += '\n> Current path: {}\n'.format('public')
    fold_list = glob.glob(fold_path + '*')
    for item in fold_list:
        cur_item = item.split('/')
        if cur_item[-1] in exclude_section:
            continue
        item_md = '\n- [**{}**]({})\n'.format(cur_item[-1], md_base_url + cur_item[-1])
        public_index += item_md
    with open(workspace_path + 'index.md', 'w') as f:
        f.write(public_index)

def update_dataset_index(fold_path, base_url):
    dataset_index = '## File Browser\n'
    dataset_index += '\n> Current path: {}\n'.format('public/datasets')
    datasets_list = glob.glob(fold_path + '*')
    for cur_dataset in datasets_list:
        cur_dataset_splited = cur_dataset.split('/')
        dataset_index += '\n#### [**{}**]({})\n'.format(cur_dataset_splited[-1], base_url + cur_dataset_splited[-1])
        file_list = glob.glob(fold_path + cur_dataset_splited[-1] + '/*')
        for cur_file in file_list:
            cur_file_splited = cur_file.split('/')
            dataset_index += '\n- [{}]({})\n'.format(cur_file_splited[-1], base_url + cur_dataset_splited[-1] + '/' + cur_file_splited[-1])
    with open(workspace_path + 'datasets.md', 'w') as f:
        f.write(dataset_index)

def update_books_index(fold_path, base_url):
    dataset_index = '## File Browser\n'
    dataset_index += '\n> Current path: {}\n'.format('public/books')
    datasets_list = glob.glob(fold_path + '*')
    for cur_dataset in datasets_list:
        cur_dataset_splited = cur_dataset.split('/')
        file_name = cur_dataset_splited[-1].split('.')[0]
        dataset_index += '\n- [**{}**]({})\n'.format(file_name, base_url + cur_dataset_splited[-1])
    with open(workspace_path + 'books.md', 'w') as f:
        f.write(dataset_index)

def update_software_index(fold_path, base_url):
    software_index = '## File Browser\n'
    software_index += '\n> Current path: {}\n'.format('public/softwares')
    software_arch_list = glob.glob(fold_path + '*')
    # print(software_arch_list)
    for cur_soft_arch in software_arch_list:
        software_arch = cur_soft_arch.split('/')[-1]
        software_index += '\n### **{}**\n'.format(software_arch)
        cur_arch_software_list = glob.glob(cur_soft_arch + '/*.*')
        cur_arch_software_list += glob.glob(cur_soft_arch + '/*/*.*')
        cur_arch_software_list += glob.glob(cur_soft_arch + '/*/*/*.*')
        cur_arch_software_list += glob.glob(cur_soft_arch + '/*/*/*/*.*')
        cur_arch_software_list += glob.glob(cur_soft_arch + '/*/*/*/*/*.*')
        pre_path_len = len('/media/disk1/nas/ail/public/softwares/')
        for software_path in cur_arch_software_list:
            software_rela_path = software_path[pre_path_len:]
            software_link = base_url + software_rela_path
            software_name = ''.join(software_rela_path.split('/')[-1].split('.')[:-1])
            software_index += '\n- [{}]({})\n'.format(software_name, software_link)
    # print(workspace_path + 'softwares.md')
    with open(workspace_path + 'softwares.md', 'w') as f:
        f.write(software_index)


def update_hfut_courses_index():
    pass

if __name__ == '__main__':
    update_public_index(public_path)
    update_dataset_index(public_path + 'datasets/', base_url + 'datasets/')
    update_books_index(public_path + 'books/', base_url + 'books/')
    update_software_index(public_path + 'softwares/', base_url + 'softwares/')
