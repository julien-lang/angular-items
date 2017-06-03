var myApp = angular.module('myApp', []);

myApp.controller('ItemController', function ItemController($scope) {
	$scope.records = [
		{ name: 'item 1', url: "http://my-test.com/1", type:"Type-1", status:"OK", include: false },
		{ name: 'item-2', url: "http://my-test.com/2", type:"Type-1", status:"Error", include: false },
		{ name: 'item-2', url: "http://my-test.com/2", type:"Type-1", status:"Processing", include: false },
		{ name: 'item-2', url: "http://my-test.com/2", type:"Type-1", status:"Offline", include: false }
	];
	// Delete data
	$scope.Delete = function (index) {
		$scope.records.splice(index, 1);
	};
	// Reset new data model
	$scope.Reset = function () {
		$scope.newName = '';
		$scope.newURL = "";
		$scope.newType = 0;
	}
	$scope.Reset();
	// Add new data
	$scope.Add = function () {
		// Add to main records
		$scope.records.push({
			name: $scope.newName,
			type: $scope.newType,
			url: $scope.newURL,
			status: "Processing",
			include: false
		});
		// See $Scope.Reset...
		$scope.Reset();
	}
});
