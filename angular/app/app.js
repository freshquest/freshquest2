angular.module('freshquest2', [
	'ngResource',
	'autoComplete',
	'ui.router',
])

.config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

;
