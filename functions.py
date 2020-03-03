import pandas as pd
import json as js

def save_data(var, filename, datatype='3D'):
    '''
    Save the variable of var to file.json of filename.
    The variable should be a dict with key as the stock code and value as the 
    dataframe with index as datetime and columns as data-items.

    Parameters
    ----------
    var : dict
        DESCRIPTION.
    filename : str
        String of filename or absolute path of the file.
    datatype : TYPE, optional
        DESCRIPTION. The default is '3D'.

    Returns
    -------
    None.

    '''
    if not datatype=='3D':
        print('当前数据类型尚未开发！')
        return
    for_storage=to_dicts(var)
    with open(filename, 'w') as f:
        js.dump(for_storage,f)
        
def load_data(filename, datatype='3D'):
    '''
    It is paired with save_data.

    Parameters
    ----------
    filename : str
        'str.json'
    datatype : TYPE, optional
        DESCRIPTION. The default is '3D'.

    Returns
    -------
    TYPE dict of dataframes
        DESCRIPTION.

    '''
    if not datatype=='3D':
        print('当前数据类型尚未开发！')
        return
    with open(filename,'r') as f:
        loadfile=js.load(f)
    return to_frames(loadfile)



def to_dicts(data_df):
    data_dict=dict()
    if isinstance(list(data_df.keys())[0], int):
        data_dict['type_flag_1']=1
    data_dict['type_flag_2']=dict()
    for k,v in data_df.items():
        data_dict[k]=v.to_dict()
        data_dict['type_flag_2'][k]=1 if isinstance(v.index[0], int) else 0
    return data_dict

def to_frames(data_dict):
    data_df=dict()
    if data_dict['type_flag_1']==1:
        for k, v in data_dict.items():
            if k in ['type_flag_1', 'type_flag_2']:
                continue
            if data_dict['type_flag_2'][k]==1:
                data_df[int(k)]=pd.DataFrame(v)
                data_df[int(k)].index=data_df[int(k)].index.astype('int')
            else:
                data_df[int(k)]=pd.DataFrame(v)
    else:
        for k,v in data_dict.items():
            if k in ['type_flag_1', 'type_flag_2']:
                continue
            if data_dict['type_flag_2'][k]==1:
                data_df[k]=pd.DataFrame(v)
                data_df[k].index=data_df[k].index.astype('int')
            else:
                data_df[k]=pd.DataFrame(v)
    return data_df

def equalss(data1, data2):
    for k in data1.keys():
        if any(data1[k].index!=data2[k].index):
            return False
        if any(data1[k].columns!=data2[k].columns):
            return False
        if not data1[k].equals(data2[k]):
            return False
    return True


# =============================================================================
# cars=pd.read_csv('cars.csv')
# titanic=pd.read_csv('titanic.csv')
# original_data={1:cars, 2:titanic}
# 
# save_data(original_data, 'data.json')
# 
# lala=load_data('data.json')
# 
# equalss(lala, original_data)
# =============================================================================
