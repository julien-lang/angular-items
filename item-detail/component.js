angular.module('itemDetail', [
	'ngRoute'
]);

angular.module('itemDetail').component('itemDetail', {
	templateUrl: 'item-detail/template.html',
	controller: ['$http', '$routeParams',
 		function PhoneDetailController($http, $routeParams) {
			var self = this;
			$routeParams.itemId = 1; // dev process
			$http.get('item-detail/data-' + $routeParams.itemId + '.json').then(function(response) {
				self.item = response.data;
			});
		}
	]
});
