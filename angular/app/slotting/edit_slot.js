angular.module('freshquest2')

.directive('editSlot', function ($timeout, Vendor) {

    var template =
        '<div class="edit-slot" ng-click="enableEditor()">' +
            '<div class="stall_number">{{ slot.stall_number }}</div>' +
            '<div ng-hide="isEditing">' +
                '{{ slot.assignment.vendor.name }} ' +
            '</div>' +
            '<div class="text-box" ng-show="isEditing">' +
                '<input ng-model="editableValue" auto-complete ui-items="vendorNames">' +
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
            vendors: "=vendors",
            vendorNames: "=vendorNames",
        },

        controller: function ($scope) {
            var noReEnableHack = false;

            $scope.isEditing = false;
            $scope.editableValue = $scope.slot.assignment ? $scope.slot.assignment.vendor.name : '';

            var vendor_names = null;
            var get_vendor_names = function () {
                return vendor_names;
            }

            $scope.enableEditor = function () {
                if ($scope.editorEnabled || noReEnableHack) return;
                $scope.isEditing = true;
                $scope.editableValue = $scope.slot.assignment ? $scope.slot.assignment.vendor.name : '';
            };

            $scope.disableEditor = function () {
                $scope.isEditing = false;
                noReEnableHack = true;
                $timeout(function () {
                    noReEnableHack = false;
                }, 0);
            };

            $scope.save = function () {
                var new_value = $scope.editableValue.trim();
                if (new_value.length)
                    if ($scope.slot.assignment) {
                        $scope.slot.assignment.$delete();
                        $scope.slot.assignment = null;
                    }
                else {

                    console.log("Saving with value: ");
                    console.log($scope.editableValue);
                }
                $scope.disableEditor();
            };
        },

    };
})

;
