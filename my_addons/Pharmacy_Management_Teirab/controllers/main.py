"""# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

import hashlib
import json
import logging
import werkzeug
import werkzeug.exceptions
import werkzeug.utils

from odoo import http, SUPERUSER_ID, _
from odoo.exceptions import AccessError, AccessDenied
from odoo.http import request
from odoo.tools import config
from odoo.tools.translate import _

from odoo.addons.bus.controllers.main import BusController
from odoo.addons.web.controllers.main import Home, ensure_db

_logger = logging.getLogger(__name__)


class Home(Home):

    @http.route('/web/login', type='http', auth="none", sitemap=False)
    def web_login(self, redirect=None, **kw):
        res = super(Home, self).web_login(redirect, **kw)
        if request.params['login_success']:
            uid = request.session.authenticate(request.session.db, request.params['login'],
                                               request.params['password'])
            user = request.env['res.users'].browse([uid])
            if user.login_with_pos_screen:
                session_obj = request.env['pos.session']
                pos_session = session_obj.sudo().search([
                    ('config_id', '=', user.default_pos.id),
                    ('state', '=', 'opened')
                ])
                if pos_session:
                    if pos_session.user_id.id == uid:
                        return http.redirect_with_hash('/pos/web')
                    else:
                        new_error_message = "The given 'POS Config' is been used by someone else. Contact Administrator!"

                        if uid in [SUPERUSER_ID] \
                            or user.has_group('base.group_system'):
                            request.session['new_error_message'] = new_error_message
                            return res
                        else:
                            request.session.uid = False
                            request.params['login_success'] = False

                            values = request.params.copy()
                            try:
                                values['databases'] = http.db_list()
                            except AccessDenied:
                                values['databases'] = None

                            if 'login' not in values and request.session.get('auth_login'):
                                values['login'] = request.session.get('auth_login')

                            if not config['list_db']:
                                values['disable_database_manager'] = True

                            # otherwise no real way to test debug mode in template as ?debug =>
                            # values['debug'] = '' but that's also the fallback value when
                            # missing variables in qweb
                            if 'debug' in values:
                                values['debug'] = True

                            values['error'] = _(new_error_message)

                            response = request.render('web.login', values)
                            response.headers['X-Frame-Options'] = 'DENY'
                            return response
                else:
                    session_id = user.default_pos.open_session_cb()
                    pos_session = session_obj.sudo().search([
                        ('config_id', '=', user.default_pos.id),
                        ('state', '=', 'opening_control')
                    ])
                    if user.default_pos.cash_control:
                        pos_session.write({'opening_balance': True})
                    pos_session.action_pos_session_open()
                    return http.redirect_with_hash('/pos/web')
            else:
                return res
        else:
            return res

    # ideally, this route should be `auth="user"` but that don't work in non-monodb mode.
    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        ensure_db()
        if not request.session.uid:
            return werkzeug.utils.redirect('/web/login', 303)
        if kw.get('redirect'):
            return werkzeug.utils.redirect(kw.get('redirect'), 303)

        request.uid = request.session.uid
        try:
            context = request.env['ir.http'].webclient_rendering_context()
            if request.session.get('new_error_message'):
                tmp_dict = json.loads(context['session_info'])
                tmp_dict['new_error_message'] = request.session.new_error_message

                context['session_info'] = json.dumps(tmp_dict)

            response = request.render('web.webclient_bootstrap', qcontext=context)
            response.headers['X-Frame-Options'] = 'DENY'
            return response
        except AccessError:
            return werkzeug.utils.redirect('/web/login?error=access')


class DataSet(http.Controller):

    @http.route('/web/dataset/get_country', type='http', auth="user")
    def get_country(self, **kw):
        cr, uid, context = request.cr, request.uid, request.context
        county_code = kw.get('country_code')
        country_obj = request.env['res.country']
        country_id = country_obj.search([('code', '=', county_code)])
        if country_id:
            #             return json.dumps(country_id.read())
            data = country_id.read()
            data[0].pop('create_date')
            data[0].pop('__last_update')
            data[0].pop('write_date')
            data[0]['image'] = False
            return json.dumps(data)
        else:
            return False

    @http.route('/web/dataset/load_products', type='http', auth="user", methods=['POST'], csrf=False)
    def load_products(self, **kw):
        cr, uid, context = request.cr, request.uid, request.context
        product_ids = eval(kw.get('product_ids'))
        fields = eval(kw.get('fields'))
        if product_ids and fields:
            records = request.env['product.product'].search_read([('id', 'in', product_ids)], fields)
            if records:
                for each_rec in records:
                    new_date = each_rec['write_date']
                    each_rec['write_date'] = new_date.strftime('%Y-%m-%d %H:%M:%S')
                return json.dumps(records)
        return json.dumps([])

    # Store data to cache
    @http.route('/web/dataset/store_data_to_cache', type='http', auth="user", methods=['POST'], csrf=False)
    def store_data_to_cache(self, **kw):
        cache_data = json.loads(kw.get('cache_data'))
        result = request.env['pos.config'].store_data_to_cache(cache_data, [])
        return json.dumps([])

    # Load Customers
    @http.route('/web/dataset/load_customers', type='http', auth="user", methods=['POST'], csrf=False)
    def load_customers(self, **kw):
        cr, uid, context = request.cr, request.uid, request.context
        partner_ids = eval(kw.get('partner_ids'))
        records = []
        fields = []
        if eval(kw.get('fields')):
            fields = eval(kw.get('fields'))
        domain = [('id', 'in', partner_ids), ('customer', '=', True)]
        try:
            records = request.env['res.partner'].search_read(domain, fields)
            if records:
                for each_rec in records:
                    if each_rec['birth_date']:
                        client_birth_date = each_rec['birth_date']
                        each_rec['birth_date'] = client_birth_date.strftime('%Y-%m-%d')
                    if each_rec['anniversary_date']:
                        client_anniversary_date = each_rec['anniversary_date']
                        each_rec['anniversary_date'] = client_anniversary_date.strftime('%Y-%m-%d')
                    if each_rec['write_date']:
                        client_write_date = each_rec['write_date']
                        each_rec['write_date'] = client_write_date.strftime('%Y-%m-%d %H:%M:%S')
                return json.dumps(records)
        except Exception as e:
            print ("\n Error......", e)
        return json.dumps([])

    # #load background
    # @http.route('/web/dataset/load_products', type='http', auth="user")
    # def load_products(self, **kw):
    #     domain = str(kw.get('domain'))
    #     domain = domain.replace('true', 'True')
    #     domain = domain.replace('false', 'False')
    #     domain = eval(domain)
    #     temp = int(kw.get('product_limit')) - 1000
    #     domain += [('id','<=',kw.get('product_limit')),('id','>=',temp)]
    #
    #     ctx1 = str(kw.get('context'))
    #     ctx1 = ctx1.replace('true', 'True')
    #     ctx1 = ctx1.replace('false', 'False')
    #     ctx1 = eval(ctx1)
    #     records = []
    #     fields = eval(kw.get('fields'))
    #     cr, uid, context = request.cr, request.uid, request.context
    #     Model = kw.get('model')
    #     context = dict(context)
    #     context.update(ctx1)
    #     try:
    #         records = request.env[Model].with_context(context).search_read(domain, fields, limit=1000)
    #     except Exception as e:
    #         _logger.error('Error .... %s',e)
    #     return json.dumps(records)


class TerminalLockController(BusController):

    def _poll(self, dbname, channels, last, options):
         #Add the relevant channels to the BusController polling.

        if options.get('pos.calendar'):
            channels = list(channels)
            ticket_channel = (
                request.db,
                'pos.calendar',
                options.get('pos.calendar')
            )
            channels.append(ticket_channel)

        if options.get('customer.display'):
            channels = list(channels)
            ticket_channel = (
                request.db,
                'customer.display',
                options.get('customer.display')
            )
            channels.append(ticket_channel)

        if options.get('lock.data'):
            channels = list(channels)
            lock_channel = (
                request.db,
                'lock.data',
                options.get('lock.data')
            )
            channels.append(lock_channel)

        return super(TerminalLockController, self)._poll(dbname, channels, last, options)


class PosMirrorController(http.Controller):

    @http.route('/web/customer_display', type='http', auth='user')
    def white_board_web(self, **k):
        config_id = False
        pos_sessions = request.env['pos.session'].search([
            ('state', '=', 'opened'),
            ('user_id', '=', request.session.uid),
            ('rescue', '=', False)])
        if pos_sessions:
            config_id = pos_sessions.config_id.id
        context = {
            'session_info': json.dumps(request.env['ir.http'].session_info()),
            'config_id': config_id,
        }
        return request.render('flexi_spa_salon.customer_display_index', qcontext=context)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
"""