angular.module('itemsApp').component('itemList', {
	templateUrl: 'item-list/template.html',
	controller: function() {
		this.records = [
			{ name: 'item 1', url: "http://my-test.com/1", type:"Type-1", status:"OK", include: false },
			{ name: 'item-2', url: "http://my-test.com/2", type:"Type-1", status:"Error", include: false },
			{ name: 'item-2', url: "http://my-test.com/2", type:"Type-1", status:"Processing", include: false },
			{ name: 'item-2', url: "http://my-test.com/2", type:"Type-1", status:"Offline", include: false }
		];
		// Delete data
		this.Delete = function (index) {
			this.records.splice(index, 1);
		};
		// Reset new data model
		this.Reset = function (form) {
			form.newName = '';
			form.newURL = "";
			form.newType = 0;
		}
		// this.Reset();
		// Add new data
		this.Add = function (form) {
			// Add to main records
			this.records.push({
				name: form.newName,
				type: form.newType,
				url: form.newURL,
				status: "Processing",
				include: false
			});
			// See this.Reset...
			this.Reset(form);
		}
	}
});
