import uuid

common_data_containers =[{ 
    "stat": {
        "Buffer" : "ARRAY [0..10] of DINT ",
        "FP" : "ARRAY [0..10] of BOOL ",
    },
    "temp" : {
        "run" : "BOOL",
        "x" : "BOOL",
        "tmp_real" : "REAL"
    }

}]

units = [
    {
        "id" : uuid.uuid4(),
        "name" : "PID801_MTR",
        "version" : "0.1",
        "comment": "ynit check",
        "commonData" : common_data_containers[0],
        "networks" : [],
    }
]


network_type_common_data_containers =[{ 
    "stat": {
        "tagname" : "_MTR",
        "tagname_ILK" : "_ILK",
    },
    "temp" : {
        "tagname_x" : "BOOL"        
    }

}]

network_types = [
    {
        "id" : uuid.uuid4(),
        "name" : "_MTR",
        "version" : "0.1",
        "comment": "motor check",
        "commonData" : network_type_common_data_containers[0],
        "tags" : {
            "tagname" : "BOOL",
            "tagname_iRun": "BOOL",
            "tagname_AO"  : "WORD",
        },
        "rows": [

        ]
    }
]


networks = [
    {
        "id" : uuid.uuid4(),
        "networkType" : "_MTR",
        "title" : "tagname : MTR x ",
        "parametersFromParametrizedColumns" : {
            "tagname" : "ST010101",
            "cell" : "PID801"
        }
    }
]