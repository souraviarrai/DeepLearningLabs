
import numpy as np

# sigmoid activation 
def activationFunction(model, type ="sigmoid"):
    return {
	"sigmoid": 1 / (1 + np.exp(-model))
}[type]

# designing perceptron model
def perceptronModel(weights, inputs, bias):
    model = np.add(np.dot(inputs, weights), bias)
    logic = activationFunction(model, type ="sigmoid")
    return np.round(logic)

# computation model
def compute(data, logicGate, weights, bias):
    weights = np.array(weights)
    output = np.array([ perceptronModel(weights,
			datum, bias) for datum in data ])
    return output

# Print Output
def printOutput(dataset, name, data):
    print("Logic Function: {}".format(name.upper()))
    print("X1\tX2\tX3\tY")
    toPrint = ["{1}\t{2}\t{3}\t{0}".format(output, *datas)
			for datas, output in zip(dataset, data)]
    for i in toPrint:
	    print(i)

# main function
def main():

    dataset = np.array([
	    [0, 0, 0],
	    [0, 0, 1],
	    [0, 1, 0],
	    [0, 1, 1],
	    [1, 0, 0],
	    [1, 0, 1],
	    [1, 1, 0],
	    [1, 1, 1]
])


    logicGate = {
	"and": compute(dataset, "and", [1, 1, 1], -2),
	"or": compute(dataset, "or", [1, 1, 1], -0.9),
	
}
    for gate in logicGate:
	    printOutput(dataset, gate, logicGate[gate])

if __name__ == '__main__':
    main()

