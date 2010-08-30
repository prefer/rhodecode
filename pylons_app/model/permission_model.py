#!/usr/bin/env python
# encoding: utf-8
# Model for permissions
# Copyright (C) 2009-2010 Marcin Kuzminski <marcin@python-works.com>
 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 2
# of the License or (at your opinion) any later version of the license.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.
"""
Created on Aug 20, 2010
Model for permissions
@author: marcink
"""

from pylons.i18n.translation import _
from pylons_app.model.db import User, Permission, UserToPerm, RepoToPerm
from pylons_app.model.meta import Session
import logging
import traceback
log = logging.getLogger(__name__)


class PermissionModel(object):

    def __init__(self):
        self.sa = Session() 
    
    def get_default(self):
        return self.sa.query(User).filter(User.username == 'default').scalar()
    
    def get_permission(self, id):
        return self.sa.query(Permission).get(id)
    
    def get_permission_by_name(self, name):
        return self.sa.query(Permission)\
        .filter(Permission.permission_name == name).scalar()
    
    
    def update(self, form_result):
        perm_user = self.sa.query(User)\
                .filter(User.username == form_result['perm_user_name']).scalar()
        u2p = self.sa.query(UserToPerm).filter(UserToPerm.user == perm_user).all()
        if len(u2p) != 3:
            raise Exception('There is more than 3 defined \
            permissions for defualt user. This should not happen please verify\
            your database')
        
        try:
            #stage 1 change defaults    
            for p in u2p:
                if p.permission.permission_name.startswith('repository.'):
                    p.permission = self.get_permission_by_name(form_result['default_perm'])
                    self.sa.add(p)
                    
                if p.permission.permission_name.startswith('hg.register.'):
                    p.permission = self.get_permission_by_name(form_result['default_register'])
                    self.sa.add(p)
                    
                if p.permission.permission_name.startswith('hg.create.'):
                    p.permission = self.get_permission_by_name(form_result['default_create'])
                    self.sa.add(p)
            #stage 2 update all default permissions for repos if checked
            if form_result['overwrite_default'] == 'true':
                for r2p in self.sa.query(RepoToPerm).filter(RepoToPerm.user == perm_user).all():
                    r2p.permission = self.get_permission_by_name(form_result['default_perm'])
                    self.sa.add(r2p)
            
            self.sa.commit()
        except:
            log.error(traceback.format_exc())
            self.sa.rollback()
            raise               
        
        
        
        
        