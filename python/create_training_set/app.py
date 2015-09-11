import csv
import imp
import create_training_set
import reader


samplecreator = imp.load_source('random_sample_from_dataset','../random_sample_from_dataset.py')
add_user_id = imp.load_source('add_user_id_to_choosen_dataset', '../add_user_id_to_choosen_dataset.py')


# sample = add_user_id.addUserID('../../roq-ad-data-set/learning-set/requests.csv','../../roq-ad-data-set/learning-set/labels.csv')
# sample = samplecreator.getSample(sample, 0.02, 0)

sample = samplecreator.getSample('../../roq-ad-data-set/learning-set/requests.csv', 0.02, 1)
sample = add_user_id.addUserID(sample, '../../roq-ad-data-set/learning-set/labels.csv', 0)



reader = reader.Reader()
data = reader.readFromTable(sample)



training_set_creator = create_training_set.Training_set_creator(data)
print training_set_creator.training_data
print 'end'
#print training_set_creator.data
#print training_set_creator.values_maps['device_id'].value_to_number
#print training_set_creator.values_maps['device_id'].number_to_value
#print training_set_creator.keys_map.value_to_number
#print training_set_creator.keys_map.number_to_value
