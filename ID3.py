import math

# returns list of values for the given attribute
def get_values(data, attr):
    values = []
    for record in data:
        if record[attr] not in values:
            values.append(record[attr])
    return values

# returns dictionary ( key: attr, value: frequency of the value in data)
def valFreq(data, attr):
    val_freq = {}
    # Calculate the frequency of each of the values
    for record in data:
        if (val_freq.has_key(record[attr])):  # checks for the key
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]]  = 1.0
    return val_freq
    
# returns most common value for an attribute
def majority_value(data, attr):
    val_freq = valFreq(data, attr)
    # sort dictionary by value and return the key corresp to the largest value
    attr_value = sorted(val_freq, key = val_freq.get).pop()
    return attr_value 

# returns the entropy of the given attribute 
def entropy(data, attr):
    val_freq = valFreq(data, attr) 
    data_entropy = 0.0
    length = sum(val_freq.values())
    for freq in val_freq.values():
        data_entropy += (-freq/length) * math.log(freq/length, 2)        
    return data_entropy

# returns information gain resulting from splitting data on the chosen attribute attr 
def gain(data, attr, target_attr):   
    val_freq = valFreq(data, target_attr)
    subsetEntropy = 0
    for key in val_freq.keys():
        # compute relative frequency of the value
        valratio = val_freq[key] / sum(val_freq.values())
        subsetdata = [entry for entry in data if entry[target_attr] == key] 
        subsetEntropy += valratio * entropy(subsetdata, attr) 
    return (entropy(data, attr) - subsetEntropy)

# returns information gain ratio to minimize splitting
def gain_ratio(data, attr, target_attr):
    val_freq = valFreq(data, target_attr)
    splitinfo = 0
    for key in val_freq.keys():
        valratio = val_freq[key] / sum(val_freq.values())
        splitinfo += (-valratio) * math.log(valratio, 2)
    return (gain(data, attr, target_attr)/splitinfo) 

# returns best attribute according to gain_ratio
def choose_attribute(data, attributes, attr):
    attributes = [entry for entry in attributes if entry != attr]
    best = attributes[0]
    bestGain = 0
    for target_attr in attributes:
        newGain = gain_ratio(data, attr, target_attr)
        if newGain > bestGain:
            bestGain = newGain
            best = target_attr
    return best

# returns  data examples corresponding the best attribute's value  
def get_data(data, best, value):
    newdata = [entry for entry in data if entry[best] == value] 
    return newdata

# main decision tree function 
def create_decision_tree(data, attributes, target_attr):

    data = data[:]                                       # copy of the data
    vals = [entry[target_attr] for entry in data]        # list of all values of the target attribute 
                                                            
    default = majority_value(data, target_attr)
    # If the data set is empty or the attributes list is empty, return the
    # default value. 
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in the data set have the same value, return that value
    elif vals.count(vals[0]) == len(vals): # count the number of vals[0] in the list of vals 
        return vals[0]
    else:
        # Choose the next best attribute to classify data
        best = choose_attribute(data, attributes, target_attr)
        print "-----------"
        print "Choose the next best attribute to split on:", best
        print "-----------"
        # Create a new decision tree/node with the best attribute and an empty dictionary object
        tree = {best:{}}
        # Create a new decision tree/sub-node for each of the values in the best attribute field
        for value in get_values(data, best):
            print "-----------"
            print "value to split on in a substree:", value
            print "-----------" 
            # Create a subtree for the current value under the "best" field
            # recursive function call
            print "-----------"
            print "Get all example corresp to best value:", get_data(data, best, value), "length:", len(get_data(data, best, value))
            print "-----------"
            subtree = create_decision_tree(get_data(data, best, value), [attr for attr in attributes if attr != best], target_attr)
            print "-----------"
            print "subtree:", subtree
            print "-----------"
            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][value] = subtree

    return tree

# function outputs the decision tree to the console         
def print_tree(tree, string):
    if type(tree) == dict:
        print "%s%s" % (string, tree.keys()[0])
        for item in tree.values()[0].keys():
            print "%s\t%s" % (string, item)
            print_tree(tree.values()[0][item], string + "\t")
    else:
        print "%s\t->\t%s" % (string, tree)        

def main():
    with open('tennis.txt', 'r') as f:
        first_line = f.readline()
    
    attributes = first_line.strip().split('\t')
    
    # list of dictionaries of data                               
    data = []                                         
    with open('tennis.txt', 'r') as f:
        next(f)
        for line in f:
            temp=line.strip().split('\t')
            mydic = {}
            count = 0
            for key in attributes:
                    mydic[key] = temp[count]
                    count += 1
            data.append(mydic)
               
    tree = create_decision_tree(data, attributes, "playtennis")
    
    print_tree(tree, "")
    
        
if __name__ == '__main__':
    main()       
    
    