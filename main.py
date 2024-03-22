from data import get_input_data, get_output_data, convert_image
from model import train_and_evaluate
import numpy as np

# Split the data into input (X) and output (y)
X = get_input_data('roll-detection/input')
y = np.array(get_output_data('roll-detection/output/rolls.xml')[['die_one', 'die_two']])
y = y.reshape(750, 2)

# Train and evaluate the model
model = train_and_evaluate(X, y)

# Predict the output for a new image
new_image = convert_image('roll-detection/input', '234.png', 1024, 1024)
new_image = new_image.reshape(1, -1)
prediction = model.predict(new_image)
print(prediction)
