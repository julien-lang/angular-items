angular.module('itemsApp', [
	'ngRoute'
]);

angular.module('itemsApp').config([
	'$locationProvider', '$routeProvider',
	function config($locationProvider, $routeProvider) {
		$locationProvider.hashPrefix('!');
		
		$routeProvider.
			when('/items', {
				template: '<item-list></item-list>'
			}).
			when('/item/:itemId', {
				template: '<item-detail></item-detail>'
			}).
			otherwise('/items');
		}
]);
