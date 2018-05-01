from wekapy import *

model = Model(classifier_type = "trees.J48")
model.train(training_file = "train.arff")
model.test(test_file = "test.arff")

predictions = model.predictions
for prediction in predictions:
    print prediction
    


