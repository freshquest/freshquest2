angular.module('freshquest2')

.factory('Vendor', function ($resource) {
    return $resource('/api/vendor/:id', { id: '@id' });
})

;
