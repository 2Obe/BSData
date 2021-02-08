import os , os.path, glob, shutil, json, argparse
import pathlib
"""
script to sort images of dataset, depending on what you want to do.
to run this script you have to give the split-type and a output directory.

you can create the following splits:
- train_test_split          | used training test split from the paper
- wear_dev_split            | ideal for analyse wear developments
- type_split                | split by BSD type

Example:
python sort_dataset.py --split_type=train_test_split \
                       --output_dir=BSD_split

"""

def mogli(split_type, output_dir):

    # paths
    path_data = './data/'
    path_label = './label/'
    image_data = 'image_data.json'
    path_data = pathlib.Path(path_data)
    path_label = pathlib.Path(path_label)
    path_output_dir = pathlib.Path(output_dir)
    path_image_data = pathlib.Path(image_data)
    data_paths_sorted = sorted(list(path_data.glob("*.jpg")))
    label_paths_sorted = sorted(list(path_label.glob("*.json")))

    # open json
    with open(path_image_data, 'r') as f:
        dict_data = json.load(f)

    # check output
    if not str(path_output_dir).endswith('/'):
        path_output_dir = str(path_output_dir) + '/'
    else:
        path_output_dir = str(path_output_dir)

    # run through image-data
    for i in range(len(dict_data['images'])):
        filename = dict_data['images'][i]['filename']
        split = dict_data['images'][i]['train_test_split']
        type = dict_data['images'][i]['type']
        wear_dev = dict_data['images'][i]['wear_dev']
        annotations = dict_data['images'][i]['annotations']
        # search for filename in path_data
        for file in data_paths_sorted:
            filename_data = os.path.basename(file)
            if filename_data == filename:
                if split_type == 'wear_dev_split':
                    wear_dev_split(file, path_output_dir, wear_dev)
                elif split_type == 'train_test_split':
                    train_test_split(file, path_output_dir, split)
                elif split_type == 'type_split':
                    type_split(file, path_output_dir, type)

        # search for label in path_label
        for file in label_paths_sorted:
            filename_data = os.path.basename(file)
            if filename_data == annotations:
                if split_type == 'wear_dev_split':
                    wear_dev_split(file, path_output_dir, wear_dev)
                elif split_type == 'train_test_split':
                    train_test_split(file, path_output_dir, split)
                elif split_type == 'type_split':
                    type_split(file, path_output_dir, type)


def wear_dev_split(input, output, wear_dev):
 
    for i in range(len(wear_dev)):
        folder = output + wear_dev[i]

        if not os.path.exists(folder):
            os.makedirs(folder)
    
        shutil.copy2(input, folder)


def train_test_split(input, output, split):

    folder1 = str(output) + 'train'
    folder2 = str(output) + 'test'

    if not os.path.exists(folder1):
        os.makedirs(folder1)
    if not os.path.exists(folder2):
        os.makedirs(folder2)

    if split == 'train':
        shutil.copy2(input, folder1)
    elif split == 'test':
        shutil.copy2(input, folder2)


def type_split(input, output, type):

    folder1 = str(output) + 'BSD_type_1'
    folder2 = str(output) + 'BSD_type_2'

    if not os.path.exists(folder1):
        os.makedirs(folder1)
    if not os.path.exists(folder2):
        os.makedirs(folder2)

    if type == 1:
        shutil.copy2(input, folder1)
    elif type == 2:
        shutil.copy2(input, folder2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--split_type', help='split type: wear_dev_split | train_test_split | type_split', type=str, required=True)
    parser.add_argument('--output_dir', help='ouput_dir', type=str, required=True)
    opt = parser.parse_args()
    mogli(opt.split_type, opt.output_dir)
