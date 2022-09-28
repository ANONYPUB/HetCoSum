import json
dataset_names=['java','python','python_GypSum']
raw_data_names=['train','valid','test']

for dataset_name in dataset_names:
    for raw_data_name in raw_data_names:
        whole_raw_data_path='../data/{}/raw_data/{}_data.json'.format(dataset_name,raw_data_name)
        sample_raw_data_path='../data/{}/raw_data/{}_data_sample.json'.format(dataset_name,raw_data_name)
        with open(whole_raw_data_path,'r') as f:
            whole_raw_data=json.load(f)
        with open(sample_raw_data_path,'w') as f:
            json.dump(whole_raw_data[:100],f,indent=4,ensure_ascii=False)
