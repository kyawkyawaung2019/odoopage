odoo.define('pos_reason.db', function (require) {
    "use strict";
    var posdb = require('point_of_sale.db');

    posdb.include({
        init: function(options){
//             var self = this;
             this._super();
             this.reason_by_id = {};
        },
        add_reasons : function(reasons){
            var reason;
            for(var i = 0, len = reasons.length; i < len; i++){
                reason = reasons[i];
                this.reason_by_id[reason.id] = reason;
            }
        },
        get_reason_by_id: function(id){
           return this.reason_by_id[id];
        },
    });

    return posdb;
});
