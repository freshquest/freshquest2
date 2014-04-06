angular.module('freshquest2', [
	'ngResource',
	'ui.router',
	'autoComplete',
	'clickToEdit',
])

.config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})

;
