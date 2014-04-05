angular.module('freshquest2')

.config(function($stateProvider, $urlRouterProvider) {
    $stateProvider.state('home', {
        url: '/home',
        templateUrl: '/static/app/home/home.html',
    });
    $urlRouterProvider.otherwise('/home');
})

.controller('Home', function ($scope) {

})

;
