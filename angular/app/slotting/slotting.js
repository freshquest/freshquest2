angular.module('freshquest2')

.config(function($stateProvider) {
    $stateProvider.state('slotting', {
        url: '/slotting',
        templateUrl: '/static/app/slotting/slotting.html',
    });
})

.controller('SlottingPage', function ($scope, Vendor) {
    $scope.vendors = Vendor.query();
})

;
