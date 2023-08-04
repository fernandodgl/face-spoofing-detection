# import necessary libraries
from tensorflow.keras.applications import ResNet50V2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

# function to build the ResNet50V2 model, excluding the top layer
def build_model():
    base_model = ResNet50V2(include_top=False, weights='imagenet', input_shape=(224, 224, 3))

    # freeze the base model's layers
    for layer in base_model.layers:
        layer.trainable = False

    # add new layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    # a logistic layer for two classes (real and fake)
    predictions = Dense(1, activation='sigmoid')(x)

    model = Model(inputs=base_model.input, outputs=predictions)
    return model
