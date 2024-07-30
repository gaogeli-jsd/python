import yaml

with open('sample.yaml', 'r') as filehandle:
    data = yaml.load(filehandle,Loader=yaml.Loader)
    print(data)
    print(data['settings']['language']) # jp