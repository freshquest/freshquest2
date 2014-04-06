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

    var add_assignments_to_stalls = function (stalls, assignment, vendors) {
        var stalls_map = {};
        _(stalls).each(function (item) {
            stalls_map[item.stall_id] = item;
        });
        var vendors_map = {};
        _(vendors).each(function (item) {
            vendors_map[item.vendor_id] = item;
        });

        _(assignment).each(function (item) {
            var stall = stalls_map[item.stall_id];
            if (stall) {
                item.vendor = vendors_map[item.vendor_id];
                stall.assignment = item;
            }
        });
    }

    Vendor.query(function (vendors) {
        Assignment.query(function (assignments) {
            Stall.query(function (stalls) {

                stalls = _(stalls).where({'building': 'c_shed'});
                stalls = _(stalls).sortBy(function (item) { return item.stall_number; });
                stalls = _(stalls).reverse();

                add_assignments_to_stalls(stalls, assignments, vendors);

                $scope.slots_left_top = filter_stalls(stalls, 33, 62, 'even');
                $scope.slots_right_top = filter_stalls(stalls, 33, 62, 'odd');
                $scope.slots_left_bottom = filter_stalls(stalls, 1, 32, 'even');
                $scope.slots_right_bottom = filter_stalls(stalls, 1, 32, 'odd');
            });
        });
    });


})

;
