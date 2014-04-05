angular.module('freshquest2')

.config(function($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/home');
    $stateProvider.state('home', {
        url: '/home',
        controller: 'Home',
        templateUrl: '/static/app/home/home.html',
    });
})

.controller('Home', function ($scope, Vendor) {
    $scope.vendors = Vendor.query();
})

;
