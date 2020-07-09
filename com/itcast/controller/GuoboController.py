from flask import Blueprint
from com.itcast.service import  guobo_service
guobo = Blueprint("guobo", __name__)


@guobo.route('/getTicket')
def get_ticket():

    return guobo_service.get_ticket_list()
