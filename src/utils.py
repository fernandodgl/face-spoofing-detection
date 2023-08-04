# import necessary libraries
import os
import glob
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# set path to the dataset
base_dir = '/data'

def load_data():
    # ... existing code ...

    # split data into training, validation, and test sets
    train_val_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])
    train_df, val_df = train_test_split(train_val_df, test_size=0.25, random_state=42, stratify=train_val_df['label'])

    return train_df, val_df, test_df

def create_data_generators(df):
    # ... existing code ...

    # load and iterate over the dataset
    it = datagen.flow_from_dataframe(df,
                                     x_col='filepath',
                                     y_col='label',
                                     target_size=(224, 224),
                                     color_mode='rgb',
                                     class_mode='binary',
                                     batch_size=64,
                                     shuffle=False) # set as data

    return it
