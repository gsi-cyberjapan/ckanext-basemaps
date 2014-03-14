# * Copyright 2014, Geospatial Information Authority of Japan, released
# under the FreeBSD
# * license. Please see

import os
import re

from logging import getLogger

from ckan import plugins as p
from ckan.lib.helpers import json

from pylons import config



log = getLogger(__name__)


class LayerBasemapsPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)

    def update_config(self, config):
        ''' Set up the resource library, public directory and
        template directory for the preview
        '''

        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'ckanext-basemaps')

    def get_helpers(self):
        from ckanext.basemaps import helpers as tiles_helpers
        return {
                'get_tile_layer_config' : tiles_helpers.get_tile_layer_config,
                }
