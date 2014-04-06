angular.module('freshquest2')

.directive('editSlot', function ($timeout, Vendor, Assignment, MarketDay) {

    var template =
        '<div class="edit-slot" ng-click="enableEditor()">' +
            '<div class="stall_number">{{ slot.stall_number }}</div>' +
            '<div ng-hide="isEditing">' +
                '{{ slot.assignment.vendor.name }}' +
            '</div>' +
            '<div class="text-box" ng-show="isEditing">' +
                '<input ng-model="editableValue" auto-complete ui-items="vendorNames">' +
                '<div class="entry_edit">'+
                    '<a ng-click="save()"><span class="fa fa-save"></span> </a>' +
                    ' or ' +
                    '<a ng-click="delete()"><span class="fa fa-ban"></span> </a>' +
                '</div>' +
            '</div>' +
            '<div ng-show="slot.assignment && !isEditing && !slot.assignment.is_checked_in" class="entry_edit"> ' +
                '<a ng-click="set_checked_in(true)"><span class="fa fa-check"></span> </a> ' +
            '</div>' +
            '<div ng-show="slot.assignment && !isEditing && slot.assignment.is_checked_in" class="entry_edit"> ' +
                '<a ng-click="set_checked_in(false)"><span class="fa fa-pencil"></span> </a> ' +
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

            $scope.delete = function () {
                if ($scope.slot.assignment) {
                    $scope.slot.assignment.$delete(function (success) {
                        $scope.slot.assignment = null;
                        $scope.disableEditor();
                    }, function (error) {
                        console.log("Error deleting:")
                        console.log(error);
                    });
                }
            }

            $scope.save = function () {
                var new_value = $scope.editableValue.trim();
                if (new_value.length) {
                    if ($scope.slot.assignment && $scope.slot.assignment.vendor.name === new_value) {
                        $scope.disableEditor();
                        return;
                    }
                    var vendor = _($scope.vendors).findWhere({name: new_value});
                    if (vendor) {
                        var assignment = new Assignment();
                        assignment.market_day_id = MarketDay.current.market_day_id;
                        assignment.stall_id = $scope.slot.stall_id;
                        assignment.vendor_id = vendor.vendor_id;
                        assignment.$save(function (success) {
                            $scope.slot.assignment = assignment;
                            assignment.vendor = vendor;
                            $scope.disableEditor();
                        }, function (error) {
                            console.log("Error updating:")
                            console.log(error);
                        });
                    }
                } else {
                    $scope.delete();
                }
            };

            $scope.set_checked_in = function (new_value) {
                var assignment = $scope.slot.assignment;
                if (! assignment) return;
                assignment.is_checked_in = new_value;
                var vendor = assignment.vendor;
                assignment.$partial_update(function (success) {
                    // Replace this after the update
                    assignment.vendor = vendor;
                }, function (error) {
                    console.log("Error updating:")
                    console.log(error);
                });
                noReEnableHack = true;
                $timeout(function () {
                    noReEnableHack = false;
                }, 0);
            };

        },

    };
})

;
