import pandas as pd
import os
import testfunc
from sklearn.model_selection import train_test_split
# Read data locally 

# Check for calling a local file.
testfunc.check_function()

print('Start processing')

print('Current Directory is :')
print(os.getcwd())

print('Contents of Current Directory is : ')
arr = os.listdir('.')
print(arr)


input_data_path = os.path.join('/opt/ml/processing/input', 'census-income.csv')
# Preprocess the data set
df=pd.read_csv(input_data_path)
downsampled = df

print("shape of data is:")
print(downsampled.shape)
# Split data set into training, validation, and test
train, test = train_test_split(downsampled, test_size=0.2)
train, validation = train_test_split(train, test_size=0.2)
# Create local output directories
try:
    os.makedirs('/opt/ml/processing/output/train')
    os.makedirs('/opt/ml/processing/output/validation')
    os.makedirs('/opt/ml/processing/output/test')
    print('Successfully created directories')
except Exception as e:
    #if the Processing call already creates these directories (or directory otherwise cannot be created)
    print(e)
    print('Could Not Make Directories, Maybe directories already exist')
    pass

# Save data locally
try:
    train.to_csv("/opt/ml/processing/output/train/train.csv")
    validation.to_csv("/opt/ml/processing/output/validation/validation.csv")
    test.to_csv("/opt/ml/processing/output/test/test.csv")
    print('Files Successfully Written')
except Exception as e:
    print('Could Not Write the Files')
    print(e)
    pass

print('Finished running processing job')
