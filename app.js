angular.module('itemsApp', [
	'ngResource',
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

angular.module('itemsApp').factory('Item', [
	'$resource',
	function($resource) {
		return $resource('item/:itemId.json', {}, {
			query: {
				method: 'GET',
				params: {itemId: 'items'},
				isArray: true
			}
		});
	}
]);
