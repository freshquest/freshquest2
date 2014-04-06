angular.module('freshquest2')

.config(function($stateProvider) {
    $stateProvider.state('slotting', {
        url: '/slotting',
        controller: 'SlottingPage',
        templateUrl: '/static/app/slotting/slotting.html',
    });
})

.controller('SlottingPage', function ($scope, Vendor, MarketDay, Stall, Assignment) {
    $scope.vendors = Vendor.query();
    $scope.market_day = MarketDay.current;
    $scope.message="a message.."

    Stall.query(function (stalls) {
        stalls = _(stalls).where({'building': 'c_shed'});
        stalls = _(stalls).sortBy(function (item) { return item.stall_number; });
        $scope.left_1 = stalls;
        console.log(stalls);
    });

    $scope.run_test = function () {
        var assignment = new Assignment();
        assignment.market_day_id = $scope.market_day.market_day_id;
        assignment.stall_id = '9e8e8f673578488da3a09a16d4a106b0';
        assignment.vendor_id = 'ef7c176c49cc4e6dac6222f2fd18a819';
        assignment.$save();
        // console.log(assignment);
    };

})

;
