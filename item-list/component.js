angular.module('itemsApp').component('itemList', {
	templateUrl: 'item-list/template.html',
	controller: function($http) {
		this.items = [];
		var self = this;
		
		$http.get('item-list/data.json').then(function(response) {
			self.items = response.data;
		});
		
		// Delete data
		this.Delete = function (index) {
			this.items.splice(index, 1);
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
			// Add to main items
			this.items.push({
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
