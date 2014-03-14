// * Copyright 2014, Geospatial Information Authority of Japan, released
// under the FreeBSD
// * license. Please see

// Dataset map module
ckan.module('tile-base', function (jQuery, _) {
return {
  initialize: function () {
    jQuery.proxyAll(this, /_on/);
      this.el.ready(this._onReady);
  },
  _onReady: function(fn) {
    $(this).delay(3000).queue(function() {
    var layers_arr = {};
    for (var val in this.options.tile_config) {
      layers_arr[$.trim(val)] = L.tileLayer(this.options.tile_config[val]["url"], {attribution: $.trim(this.options.tile_config[val]["attribution"])});
    }

    map.options.attributionControl = true;
    L.control.layers(layers_arr).addTo(map);
    });
  }
}
// dataset-map-attribution
});

