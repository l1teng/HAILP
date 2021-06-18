import os
import glob

base_url = 'http://172.18.220.5/_public/'
public_path = '/media/disk1/nas/ail/public/'
workspace_path = '/media/disk1/nas/ail/ail_page/docs/public/'
exclude_section = ['imgs']

def update_public_index(fold_path):
    public_index = '## File Browser\n'
    public_index += '\n> Current path: {}\n'.format(base_url)
    fold_list = glob.glob(fold_path + '*')
    for item in fold_list:
        cur_item = item.split('/')
        if cur_item[-1] in exclude_section:
            continue
        item_md = '\n- [{}]({})\n'.format(cur_item[-1], base_url + cur_item[-1])
        public_index += item_md
    with open(workspace_path + 'index.md', 'w') as f:
        f.write(public_index)

def get_title_link_list(fold_path):
    glob.glob(fold_path + '*')


if __name__ == '__main__':
    update_public_index(public_path)