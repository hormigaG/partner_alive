# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from datetime import datetime , timedelta 
from dateutil.relativedelta import relativedelta

from dateutil import parser

from openerp import models, fields, api ,  SUPERUSER_ID
from openerp import tools


from openerp.tools.translate import _
import re
import logging

_logger = logging.getLogger(__name__) 





class res_partner(models.Model):

    _inherit = 'res.partner'

    check_alive_server = fields.Boolean('check alive')
    alive_public_id = fields.Char('Id alive')  
    alive_ip = fields.Char('Ultima IP')  
    alive_datetime = fields.Datetime('Ultimo ping ')  
