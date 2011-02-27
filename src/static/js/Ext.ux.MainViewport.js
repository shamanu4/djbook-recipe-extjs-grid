Ext.ux.MainViewport = Ext.extend(Ext.Viewport, {
    renderTo: Ext.getBody(),

    initComponent: function(){
        var config = {
            layout: 'border',
            defaults: {
                frame: true
            },
            items: [
                {
                    id: 'tab-panel',
                    region: 'center',
                    tbar: new Ext.TabPanel({
                        items: [
                            {
                                xtype: 'ext:ux:city-grid'
                            },{
                                xtype: 'ext:ux:street-grid'
                            }
                        ]
                    })
                }
            ]
        }
        Ext.apply(this, Ext.apply(this.initialConfig, config));
        Ext.ux.MainViewport.superclass.initComponent.apply(this, arguments);
    }//initComponent
});