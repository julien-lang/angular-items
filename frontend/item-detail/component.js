angular.module('itemsApp').component('itemDetail', {
	templateUrl: 'item-detail/template.html',
	controller: ['$http', '$routeParams',
 		function($http, $routeParams) {
			var self = this;
			$http.get('/api/info/' + $routeParams.itemId).then(function(response) {
				self.item = response.data;
			});
		}
	]
});
