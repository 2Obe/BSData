# Instruction dataset split 

The authors of this dataset provide 3 types of different dataset splits.<br>
To get the data split you have to run the python script `split_dataset.py`.<br>
Script inputs:
- split-type (mandatory)
- output directory (mandatory)


### different split-types:
1. `train_test_split`: splits dataset into train and test data (80%/20%)
2. `wear_dev_split`: splits dataset into 27 wear-developments 
3. `type_split`: splits dataset into different BSD types


### example:
`python split_dataset.py --split_type=train_test_split --output_dir=BSD_split_folder`<br>


**Result:**<br>
`./BSD_slit_folder/train/` and `./BSD_slit_folder/test/`


