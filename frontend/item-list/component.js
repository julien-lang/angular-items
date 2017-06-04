angular.module('itemsApp').component('itemList', {
	templateUrl: 'item-list/template.html',
	controller: ['$http', 'Item', function($http, Item) {
		this.items = Item.query();
		
		this.delete_item = function (item_id) {
			console.log("delete "+item_id);
			
			$http.get('/api/delete/' + item_id).then(function(response) {
				if (response.data["status"] == "deleted") {
					self.items = Item.query();
				}
			});
		};
	}],
		// // Delete data
		// this.Delete = function (index) {
		// 	this.items.splice(index, 1);
		// };
		// // Reset new data model
		// this.Reset = function (form) {
		// 	form.newName = '';
		// 	form.newURL = "";
		// 	form.newType = 0;
		// }
		// // this.Reset();
		// // Add new data
		// this.Add = function (form) {
		// 	// Add to main items
		// 	this.items.push({
		// 		name: form.newName,
		// 		type: form.newType,
		// 		url: form.newURL,
		// 		status: "Processing",
		// 		include: false
		// 	});
		// 	// See this.Reset...
		// 	this.Reset(form);
		// }
	// }
});
