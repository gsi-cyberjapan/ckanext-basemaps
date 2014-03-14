#* Copyright 2014, Geospatial Information Authority of Japan, released
#under the FreeBSD
#* license. Please see

import logging

from ckan import plugins as p
from ckan.lib import helpers as h

from pylons import config

log = logging.getLogger(__name__)

def get_tile_layer_config():
    '''
        Returns a dict with all configuration options related to the common
        base map (ie those starting with 'ckanext.basemaps.layers')
    '''

    namespace = 'ckanext.basemaps.laylers.'
    conf_dict = dict([(k.replace(namespace, ''), v) for k, v in config.iteritems() if k.startswith(namespace)])
    if conf_dict:
        arr_name = conf_dict['names']. split(',')
        arr_url = conf_dict['urls']. split(',')
        arr_attribution = conf_dict['attributions']. split(',')
        json_dict = {}
        for x in xrange(0,len(arr_name)):
            tmp_dict = {}
            tmp_dict['url'] = arr_url[x]
            try:
              tmp_dict['attribution'] = arr_attribution[x]
            except IndexError:
              tmp_dict['attribution'] = ""

            json_dict[arr_name[x]] = tmp_dict
        return json_dict
    else:
        return conf_dict
