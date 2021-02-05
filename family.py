''' 
  @Author: Uthsavi KP
  @Date: 2021-02-03 13:15:20
  @Last Modified by:  Uthsavi KP
  @Last Modified time: 2021-02-03 21:03:42
  @Title: Azure cosmosDB using python
'''

import uuid
def get_andersen_family_item():
    andersen_item = {
    'id': 'Andersen_' + str(uuid.uuid4()),
    'lastName': 'Andersen',
    'district': 'WA5',
    'parents': [
        {
            'familyName': None,
            'firstName': 'Thomas'
        },
        {
            'familyName': None,
            'firstName': 'Mary Kay'
        }
    ],
    'children': None,
    'address': {
        'state': 'WA',
        'county': 'King',
        'city': 'Seattle'
    },
    'registered': True
}
    return andersen_item