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

.factory('Assignment', function ($resource) {
    return $resource('/api/assignment/:id', { id: '@id' });
})

;
