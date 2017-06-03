angular.module('itemsApp').component('itemList', {
	templateUrl: 'item-list/template.html',
	controller: function($http) {
		this.records = [];
		var self = this;
		
		$http.get('item-list/data.json').then(function(response) {
			self.records = response.data;
		});
		
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
