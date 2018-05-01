from wekapy import *
print("hola")
model = Model(classifier_type = "trees.J48")
model.train(training_file = "/wekapy_data/arff/train.arff")
model.test(test_file = "/wekapy_data/arff/test.arff")

for prediction in model.predictions:
    print(prediction)
