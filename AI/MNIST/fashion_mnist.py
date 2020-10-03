import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt

# print("load dfasion_mnist data")


class FashionMnistClassificationModel(tf.keras.Model):
    def __init__(self, name=None):
        super(FashionMnistClassificationModel, self).__init__(name=name)
        self.dense = keras.layers.Flatten(input_shape=(28, 28))
        self.dense1 = keras.layers.Dense(128, activation='relu')
        self.pred_layer = keras.layers.Dense(10, activation='softmax')
        (self.train_images, self.train_labels), (self.test_images,
                                                 self.test_labels) = keras.datasets.fashion_mnist.load_data()
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                            'Ankle boot']
        self.train_images = self.train_images / 255.0
        self.test_images = self.test_images / 255.0

    def call(self, inputs):
        x = self.dense(inputs)
        x = self.dense1(x)
        return self.pred_layer(x)

    def get_model(self):
        return FashionMnistClassificationModel(name="3_layer_mlp")

    def get_train_data(self):
        return self.train_images, self.train_labels

    def get_test_data(self):
        return self.test_images, self.test_labels

    def get_label_names(self):
        return self.class_names

    def get(self):
        pass


def random_visualization_fashion_data(train_images, train_labels, class_names):
    i = int(tf.random.uniform([1], 0, train_images.shape[0]))
    print(i)
    plt.figure()
    plt.title(class_names[train_labels[i]])
    plt.imshow(train_images[i])
    plt.colorbar()
    plt.grid(False)
    plt.show()


def model_compile():
    print("compile")
    fashionMnistClass = FashionMnistClassificationModel()
    train_images, train_labels = fashionMnistClass.get_train_data()
    model = fashionMnistClass.get_model()
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=5)
    model.summary()
    return model


def model_prediction():
    fashionMnistClass = FashionMnistClassificationModel()
    test_images, test_labels = fashionMnistClass.get_test_data()
    fashion_model = model_compile()
    test_loss, test_acc = fashion_model.evaluate(
        test_images, test_labels, verbose=2)
    predictions = fashion_model.predict(test_images)
    num_rows = 5
    num_cols = 3
    num_images = num_rows * num_cols
    plt.figure(figsize=(2 * 2 * num_cols, 2 * num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
        plot_image(i, predictions, test_labels, test_images)
        plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
        plot_value_array(i, predictions, test_labels)
    print("show")
    plt.show()


def plot_image(i, predictions_array, true_label, img):
    fashionMnistClass = FashionMnistClassificationModel()
    class_names = fashionMnistClass.get_label_names()
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


# random_visualization_fashion_data()


# model_prediction()
