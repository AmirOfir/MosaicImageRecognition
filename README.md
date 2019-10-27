# Mosaic Image Recognition

The aiming was to check if a regular convolutional neural network that uses filters of size 3x3 or 4x4 would identify images built as mosaic of tiles. \
The idea behind was to understand how neural network will condense with having varying tiles - each has a different texture, (+ colors, lines) \
and only not deep levels will be able to unveil the data that is crucial for understanding the photo meaning.

The aiming was to track the general process of recognition in a NN: \
1. Have a (small) dataset divided to training data and validation data. \
2. Start with a heavylifted learned weights (started with resnet18) \
3. Replace with the last layer and cost function of the dataset with relevant to the scenario. \
4. Learning of the weights in the last layer or continue training the entire network. 

I chose to start with learning of the last layer \
Those are my steps: \
1. Picked free images off the web (see MosaicImages.zip)
2. Converted to single format of 20x20 pixels (tried with 40x40 and 30x30 first, it was too big for my Google Cloud...) (see tilemaker.py)
3. Downloaded "hymenoptera_data" off pytorch's guide
4. Converted the images to mosaics (see fauxaic.py)
5. Wrote simple transfer learning code (see transfer_learning_mosaics.py)
The process Had a best run of 0.89 accuracy

Simple images:
https://drive.google.com/file/d/1dd2c9uG-Si0sVUkdzhCK5nDKIQUa632K/view?usp=sharing
https://drive.google.com/file/d/1XUe5X7Qg4kE6mzGAmpPHScnGWVy4tpZ6/view?usp=sharing


