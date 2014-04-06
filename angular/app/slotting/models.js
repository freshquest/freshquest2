angular.module('freshquest2')

.factory('Vendor', function ($resource) {
    return $resource('/api/vendor/:id', { id: '@id' });
})

.service('MarketDay', function ($resource) {
	var MarketDay = $resource('/api/market_day', { id: '@id' });
	return {
		current: MarketDay.get(),
	};
})

;
