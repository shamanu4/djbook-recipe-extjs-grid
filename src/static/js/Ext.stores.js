Ext.ux.cities_store = new Ext.data.DirectStore({
    api: {
        read: CityGrid.read,
        create: CityGrid.create,
        update: CityGrid.update,
        destroy: CityGrid.destroy
    },
    restful: true,
    autoLoad: true,
    autoSave: false,
    storeId: 'cities-store',    
    reader: new Ext.data.JsonReader({
        root: 'data',
        totalProperty: 'total',
        //idProperty: 'id',
        fields: [
            'id',
            'name',
        ]
    }),
    writer: new Ext.data.JsonWriter({        
        encode: false,
        writeAllFields: true,
        listful: true
    }),
    baseParams : {
        start:0,
        limit:10,
        filter_fields:['name'],
        filter_value:''
    }
});

Ext.ux.cities_combo_store = new Ext.data.DirectStore({
    api: {
        read: CityGrid.read,
        create: CityGrid.create,
        update: CityGrid.update,
        destroy: CityGrid.destroy
    },
    restful: true,
    autoLoad: true,
    autoSave: false,
    storeId: 'cities-combo-store',
    reader: new Ext.data.JsonReader({
        root: 'data',
        totalProperty: 'total',
        //idProperty: 'id',
        fields: [
            'id',
            'name',
        ]
    }),
    baseParams : {
        filter_fields:['name'],
        filter_value:'',
        filter:''
    }
});

var cities_ds_model = Ext.data.Record.create([
    'id',
    'name',
]);

Ext.ux.streets_store = new Ext.data.DirectStore({
    api: {
        read: StreetGrid.read,
        create: StreetGrid.create,
        update: StreetGrid.update,
        destroy: StreetGrid.destroy
    },
    restful: true,
    autoLoad: true,
    autoSave: false,
    storeId: 'streets-store',
    reader: new Ext.data.JsonReader({
        root: 'data',
        totalProperty: 'total',
        //idProperty: 'id',
        fields: [
            'id',
            'city',
            'name',
        ]
    }),
    writer: new Ext.data.JsonWriter({
        encode: false,
        writeAllFields: true,
        listful: true
    }),
    baseParams : {
        start:0,
        limit:10,
        filter_fields:['name','city__name'],
        filter_value:''
    }
});

var streets_ds_model = Ext.data.Record.create([
    'id',
    'city',
    'name',
]);
