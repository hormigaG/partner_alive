# -*- coding: utf-8 -*-
import base64

from openerp import SUPERUSER_ID
from openerp import http
from openerp.tools.translate import _
import openerp.http as http

from openerp.http import request


from openerp.addons.website.models.website import slug

from datetime import datetime
from dateutil.parser import parse
import uuid

import re

import logging

_logger = logging.getLogger(__name__) 




class partner_alive(http.Controller):

    @http.route('/partner_alive/<model("res.partner"):partner>/<alive_public_id>', methods=['GET'] ,type='http', auth="public", website=True)
    def ping(self, partner,alive_public_id):
        error = {}
        default = {}
        if partner.check_alive_server== True and  partner.alive_public_id== alive_public_id : 
            wsgienv = req.httprequest.environ


            _logger.info(wsgienv['HTTP_HOST'])
            return wsgienv['HTTP_HOST']


