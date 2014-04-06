angular.module('freshquest2')

.config(function($stateProvider) {
    $stateProvider.state('slotting_c', {
        url: '/slotting_c',
        controller: 'Slotting-C-Page',
        templateUrl: '/static/app/slotting/slotting_c.html',
    });
})

.controller('Slotting-C-Page', function ($scope, Vendor, MarketDay, Stall, Assignment) {
    $scope.vendors = Vendor.query();
    $scope.market_day = MarketDay.current;

    // Return stalls in the range min -> max
    // If parity is 'even', or 'odd' returns only the even or odd items
    var filter_stalls = function (stalls, min, max, parity) {
        var filter = function (item) {
            if (item.stall_number < min)
                return false;
            else if (item.stall_number > max)
                return false;
            else if (parity == 'even')
                return item.stall_number % 2 == 0;
            else
                return item.stall_number % 2 == 1;
        }
        return _(stalls).filter(filter);
    }

    Stall.query(function (stalls) {
        stalls = _(stalls).where({'building': 'c_shed'});
        stalls = _(stalls).sortBy(function (item) { return item.stall_number; });
        stalls = _(stalls).reverse();

        $scope.left_top = filter_stalls(stalls, 33, 62, 'even');
        $scope.right_top = filter_stalls(stalls, 33, 62, 'odd');
        $scope.left_bottom = filter_stalls(stalls, 1, 32, 'even');
        $scope.right_bottom = filter_stalls(stalls, 1, 32, 'odd');

        console.log($scope.right_bottom);
    });

})

;
