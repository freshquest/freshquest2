angular.module('freshquest2')

.factory('Vendor', function ($reource) {
    return $resource('/api/vendor/:id', { id: '@id' });
})

;
