angular.module('itemsApp').component('itemList', {
	templateUrl: 'item-list/template.html',
	controller: ['$http', '$interval', 'Item', function($http, $interval, Item) {
		var self = this;
		this.api_list = function(){
			self.items = Item.query();
		};
		
		$interval(self.api_list, 10000);
		this.api_list();
		
		this.delete_item = function (item_id) {
			var self = this;
			$http.get('/api/delete/' + item_id).then(function(response) {
				if (response.data["status"] == "deleted") {
					delete self.items[item_id];
				}
			});
		};
		
		// Reset new data model
		this.Reset = function (form) {
			form.newName = '';
			form.newURL = "";
			form.newType = 0;
		};
		
		// Add new data
		this.Add = function (form) {
			var data = {
				"name": form.newName,
				"type": form.newType
			};
			
			if (form.newURL) {
				data["url"] = form.newURL
			}
			
			this.Reset(form);
			
			var self = this;
			$http.post('/api/new', data).then(function(response) {
				if (response.data["status"] == "Processing") {
					self.items[response.data["id"]] = response.data;
				}
			});
		}
	}],
});
