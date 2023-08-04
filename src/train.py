# import necessary libraries
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint
from tensorflow.keras.optimizers import Adam
from datetime import datetime

# import helper functions and model builder
from utils import load_data, create_data_generators
from model import build_model

# load data
train_df, val_df, test_df = load_data()

# create data generators
train_it, val_it, test_it = create_data_generators(train_df, val_df, test_df)

# build the model
model = build_model()

# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# create callbacks
log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=3)
model_save_callback = ModelCheckpoint('model.h5', save_best_only=True, monitor='val_loss', mode='min')

# train the model
history = model.fit(train_it,
                    validation_data=val_it,
                    steps_per_epoch=train_it.samples // train_it.batch_size,
                    validation_steps=val_it.samples // val_it.batch_size,
                    epochs=30,
                    callbacks=[tensorboard_callback, early_stopping_callback, model_save_callback])
