# import datetime
import bitmex
from time import sleep

from database import BitmexAccount

MAIN_ACCOUNT = BitmexAccount.objects(is_main=True).first()
MAIN_ACCOUNT_API_ID = MAIN_ACCOUNT.api_key
MAIN_ACCOUNT_API_SECRET = MAIN_ACCOUNT.api_secret

# add 'validate_swagger_spec': False to bitmex -> config

hierarchy = {
    'main_account': {
        'api_key': MAIN_ACCOUNT_API_ID,
        'api_secret': MAIN_ACCOUNT_API_SECRET,
        # 'last_order_id': ""
    },
    'child_accounts':
        {
            0: {
                'api_key': "HHeN13ttQRPy0N0kANkYAxaW",
                'api_secret': "0W1kCxgWft4v8YAyQ-oBHYDTIJESzOrl-Xwr2pK6xQn_oHXe",
            },
            1: {
                'api_key': "pwR_8OpiKiw0IpefnFeFnvvL",
                'api_secret': "ooMBABzFxgJmeQi4sCfYLM5qs2CR-0O7r7VSgQP_NvfsEefp",
            },
            2: {
                'api_key': "gApV35utD2WWtxedeEy5k8BA",
                'api_secret': "JoHMcOrrEg0mwRsJX53XbYTOnmx0rtDwjRETeszAX--OjpHY",
            },

        }
}

while True:
    main_acc = bitmex.bitmex(test=True, api_key=hierarchy['main_account']['api_key'],
                             api_secret=hierarchy['main_account']['api_secret'])
    main_acc_result, main_acc_status = main_acc.Order.Order_getOrders(reverse=True).result()

    main_acc_order_id = main_acc_result[0]['orderID']
    main_acc_symbol = main_acc_result[0]['symbol']
    main_acc_side = main_acc_result[0]['side']
    main_acc_orderQty = main_acc_result[0]['orderQty']
    main_acc_price = main_acc_result[0]['price']

    if 'last_order_id' not in hierarchy['main_account']:
        hierarchy['main_account']['last_order_id'] = main_acc_order_id
    else:
        if hierarchy['main_account']['last_order_id'] == main_acc_order_id:
            sleep(3)
            continue
        else:
            hierarchy['main_account']['last_order_id'] = main_acc_order_id

    print(
        '\nLast order main_acc:\n\t\torder_id: {order}\n'
        '\t\tside: {side}\n'
        '\t\tsymbol: {symbol}\n'
        '\t\torderQty: {qty}\n'
        '\t\tprice: {price}\n\n'.format(order=main_acc_order_id, side=main_acc_side,
                                        symbol=main_acc_symbol, qty=main_acc_orderQty, price=main_acc_price
        ))

    for key, value in hierarchy['child_accounts'].items():
        child_acc = bitmex.bitmex(test=True, api_key=value['api_key'], api_secret=value['api_secret'])
        child_acc_result, child_acc_status = child_acc.Order.Order_new(
            symbol=main_acc_symbol, side=main_acc_side, orderQty=main_acc_orderQty, price=main_acc_price).result()
        if child_acc_status.status_code == 200:
            print(f"Order was successfully for api: {value['api_key']}")

    sleep(3)
