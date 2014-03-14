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
    var layers_arr = {};
    var tille;
    for (var val in this.options.tile_config) {
      if (val && this.options.tile_config[val]["url"]) {
        if (this.options.tile_config[val]["attribution"]) {
          //console.log($.trim(this.options.tile_config[val]["attribution"]));
          layers_arr[$.trim(val)] = L.tileLayer(this.options.tile_config[val]["url"], {attribution: $.trim(this.options.tile_config[val]["attribution"])});
        } else {
          //console.log("aaaa");
          layers_arr[$.trim(val)] = L.tileLayer(this.options.tile_config[val]["url"]);
        }
      }
    }
    //console.log(layers_arr);
    //console.log(Object.keys(layers_arr).length);
    if (Object.keys(layers_arr).length) {
      L.control.layers(layers_arr).addTo(map);
    }
  }
}
// dataset-map-attribution
});

