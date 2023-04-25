for keys in ecg_dict.keys():
    ecg_dict[keys] = {key.replace('ECG_', ''): ecg_dict[keys].pop(key) for key in list(ecg_dict[keys].keys())}
