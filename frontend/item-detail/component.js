angular.module('itemsApp').component('itemDetail', {
	templateUrl: 'item-detail/template.html',
	controller: ['$window', '$http', '$routeParams',
		function ItemDetailController($window, $http, $routeParams) {
			var self = this;
			$http.get('/api/info/' + $routeParams.itemId).then(function(response) {
				self.item = response.data;
			});
			
			this.delete_item = function (item_id) {
				console.log("delete "+item_id);
				
				$http.get('/api/delete/' + item_id).then(function(response) {
					if (response.data["status"] == "deleted") {
						$window.location.href = '#!';
					}
				});
			};
		}
	]
});
