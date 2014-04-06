angular.module('freshquest2')

.config(function($stateProvider) {
    $stateProvider.state('slotting', {
        url: '/slotting',
        controller: 'SlottingPage',
        templateUrl: '/static/app/slotting/slotting.html',
    });
})

.controller('SlottingPage', function ($scope, Vendor, MarketDay) {
    $scope.vendors = Vendor.query();
    $scope.market_day = MarketDay.current;
})

;
