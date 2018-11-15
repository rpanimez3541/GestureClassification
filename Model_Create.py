from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import plot_model

model = Sequential()
visible = (512,512, 1)

model.add(Conv2D(32, (3, 3), input_shape=visible))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.25))

# 5 types
model.add(Dense(5))
model.add(Activation('sigmoid'))

# summarize layers
print(model.summary())
# plot graph
plot_model(model, to_file='gesture_classification.png')