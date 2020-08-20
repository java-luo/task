from flask import Blueprint
from com.itcast.service import  guobo_service
from com.itcast.splider import keji_spider
from com.itcast.utils import ServerResponse
guobo = Blueprint("guobo", __name__)


@guobo.route('/getTicket')
def get_ticket():

    return guobo_service.get_ticket_list()

@guobo.route('/getShouduTicket')
def get_shoudu_ticket():

    return guobo_service.get_shoudu_ticket_list()

@guobo.route('/getKejiTicket')
def get_keji_ticket():

    return ServerResponse.createSuccess(data=keji_spider.get_ticket_list())