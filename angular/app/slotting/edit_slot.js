angular.module('freshquest2')

.directive('editSlot', function ($timeout) {
    var template =
        '<div class="edit-slot" ng-click="enableEditor()">' +
            '{{ slot.stall_number }}' +
            '<div ng-hide="isEditing">' +
                '{{ slot.assignment.vendor.name }} ' +
            '</div>' +
            '<div ng-show="isEditing">' +
                '<input ng-model="editableValue">' +
                '<a ng-click="save()">Save</a>' +
                ' or ' +
                '<a ng-click="disableEditor()">cancel</a>.' +
            '</div>' +
        '</div>';

    return {

        restrict: 'A',

        replace: true,

        template: template,

        scope: {
            slot: "=editSlot",
        },

        controller: function ($scope) {
            var noReEnableHack = false;

            $scope.isEditing = false;
            $scope.editableValue = $scope.slot.assignment ? $scope.slot.assignment.vendor.name : '';

            $scope.enableEditor = function() {
                if ($scope.editorEnabled || noReEnableHack) return;
                $scope.isEditing = true;
                $scope.editableValue = $scope.slot.assignment ? $scope.slot.assignment.vendor.name : '';
            };

            $scope.disableEditor = function() {
                $scope.isEditing = false;
                noReEnableHack = true;
                $timeout(function () {
                    noReEnableHack = false;
                }, 0);
            };

            $scope.save = function() {
                console.log("Saving with value: ");
                console.log($scope.editableValue);
                // $scope.value = $scope.view.editableValue;
                $scope.disableEditor();
            };
        },

    };
})

;
