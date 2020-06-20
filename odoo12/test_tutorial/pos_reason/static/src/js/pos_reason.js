odoo.define('pos_reason.buying_reason', function (require) {
    "use strict";
    var core = require('web.core');
    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var _t = core._t;

    var _super_order = models.Order.prototype;
    var _super_PosModel = models.PosModel.prototype;

    models.PosModel = models.PosModel.extend({
        get_reason: function() {
            var order = this.get_order();
            if (order) {
                return order.get_reason();
            }
            return null;
        },
    });

    models.Order = models.Order.extend({
        initialize: function(attr, options) {
            _super_order.initialize.call(this,attr,options);
            this.set({ reason: null });
        },

        set_reason: function(reason){
            this.assert_editable();
            this.set('reason',reason);
        },
        get_reason: function(){
           return this.get('reason');

        },
        get_reason_name: function(){
            var reason = this.get('reason');
            return reason ? reason.name : "";
        },

        set_reason_id : function(reason_id){
            this.reason_id = reason_id;
            var reason = this.pos.db.get_reason_by_id(reason_id);
            this.set_reason(reason);
            this.trigger('change', this);
        },

        init_from_JSON: function(json) {
            var reason;
            _super_order.init_from_JSON.apply(this,arguments);
            if (json.reason_id) {
                reason = this.pos.db.get_reason_by_id(json.reason_id);
                if (!reason) {
                    console.error('ERROR: trying to load a reason not available in the pos');
                }
            } else {
                reason = null;
            }
            this.set_reason(reason);
        },
        export_as_JSON: function(){
            var json = _super_order.export_as_JSON.call(this);
            json.reason_id = this.get_reason() ? this.get_reason().id : false;
            return json;
        },
    });

    var BuyingReasonButton = screens.ActionButtonWidget.extend({
        template : 'BuyingReasonButton',
        button_click : function(){
            var self = this;
            var list = [];
            var reasons = this.pos.db.reason_by_id;
            for (var reason in self.pos.db.reason_by_id){
                list.push({
                    'label': reasons[reason].name,
                    'item': reasons[reason].id,
                });
            }

            this.gui.show_popup('selection',{
                'title': _t('Select Buying Reason'),
                list: list,
                'confirm': function(item) {
                    self.apply_buying_reason(item);
                    self.renderElement();
                },
            });
        },

        apply_buying_reason: function(reason) {
            var order = this.pos.get_order();
            order.set_reason_id(reason);
        },
    });

    screens.define_action_button({
        'name': 'buying_reason',
        'widget' :BuyingReasonButton,
    });

    models.load_models({
            model: 'pos.reason',
            fields: ['name'],
            loaded: function(self,reasons){
                self.reasons = reasons;
                self.db.add_reasons(reasons);
            },
        });

    return {
        BuyingReasonButton : BuyingReasonButton,
    }
});