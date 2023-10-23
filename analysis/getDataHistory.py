from iqoptionapi.stable_api import IQ_Option
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

def getHistory(login, password, count):
    I_want_money=IQ_Option(login, password)
    I_want_money.connect()
    I_want_money.change_balance("PRACTICE")
    return I_want_money.get_optioninfo(count)

