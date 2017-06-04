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
		return $resource('/api/list', {}, {
			query: {
				method: 'GET'
				//params: {itemId: 'items'},
				//isArray: true
			}
		});
	}
]);

// angular.module('itemsApp').factory('loadItem', [
// 	'$resource',
// 	function($resource) {
// 		return $resource('/api/info/', {}, {
// 			query: {
// 				method: 'GET',
// 				//params: {itemId: 'items'},
// 				isArray: true
// 			}
// 		});
// 	}
// ]);

//var User = $resource('/user/:userId', {userId:'@id'});
