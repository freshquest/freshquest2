angular.module('autoComplete', [])

.directive('autoComplete', function ($timeout) {

    return function (scope, iElement, iAttrs) {
        scope.$watch(iAttrs.uiItems, function (items) {
            iElement.autocomplete('option', { source: items });
        })
        iElement.autocomplete({
            select: function() {
                $timeout(function() {
                    iElement.trigger('input');
                }, 0);
            },
        });
    };

});
        