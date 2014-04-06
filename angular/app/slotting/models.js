angular.module('freshquest2')

.factory('Vendor', function ($resource) {
    return $resource('/api/vendor/:id', { id: '@id' });
})

.service('MarketDay', function ($resource) {
	var MarketDay = $resource('/api/market_day');
	return {
		current: MarketDay.get(),
	};
})

.factory('Stall', function ($resource) {
    return $resource('/api/stall/:id', { id: '@id' });
})

.factory('Assignment', function ($resource) {
    return $resource('/api/assignment/:assignment_id', { assignment_id: '@assignment_id' });
})

;
