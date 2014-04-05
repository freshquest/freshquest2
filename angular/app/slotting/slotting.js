angular.module('freshquest2')

.controller('SlottingPage', function ($scope, Vendor) {
	$scope.vendors = Vendor.query();
})

;
